from typing import List, Dict, Optional
from dataclasses import dataclass, field

@dataclass
class MenuItem:
    """Represents a menu item"""
    id: str
    label: str
    url: str
    icon: Optional[str] = None
    parent_id: Optional[str] = None
    order: int = 0
    visible: bool = True
    required_roles: List[str] = field(default_factory=list)
    children: List['MenuItem'] = field(default_factory=list)
    
    def add_child(self, child: 'MenuItem'):
        """Add a child menu item"""
        child.parent_id = self.id
        self.children.append(child)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'label': self.label,
            'url': self.url,
            'icon': self.icon,
            'visible': self.visible,
            'children': [child.to_dict() for child in self.children]
        }

class MenuManager:
    """Manages menu structure and items"""
    
    def __init__(self):
        self.items: Dict[str, MenuItem] = {}
        self.root_items: List[MenuItem] = []
    
    def add_item(self, item: MenuItem):
        """Add a menu item"""
        self.items[item.id] = item
        
        if item.parent_id is None:
            self.root_items.append(item)
            self.root_items.sort(key=lambda x: x.order)
        else:
            parent = self.items.get(item.parent_id)
            if parent:
                parent.add_child(item)
                parent.children.sort(key=lambda x: x.order)
    
    def remove_item(self, item_id: str):
        """Remove a menu item"""
        item = self.items.pop(item_id, None)
        
        if item and item.parent_id is None:
            self.root_items.remove(item)
    
    def get_item(self, item_id: str) -> Optional[MenuItem]:
        """Get a menu item by ID"""
        return self.items.get(item_id)
    
    def get_menu(self, user_roles: List[str] = None) -> List[MenuItem]:
        """Get filtered menu based on user roles"""
        if user_roles is None:
            user_roles = []
        
        def filter_items(items):
            filtered = []
            for item in items:
                # Check visibility and permissions
                if not item.visible:
                    continue
                
                if item.required_roles and not any(role in user_roles for role in item.required_roles):
                    continue
                
                # Filter children
                item.children = filter_items(item.children)
                filtered.append(item)
            
            return filtered
        
        return filter_items(self.root_items)
    
    def to_dict(self, user_roles: List[str] = None) -> List[Dict]:
        """Convert menu to dictionary"""
        menu = self.get_menu(user_roles)
        return [item.to_dict() for item in menu]
