from typing import Dict, Callable, List, Optional
from functools import wraps

class NavigationRouter:
    """Manages application routing and navigation"""
    
    def __init__(self, menu_manager, permission_manager):
        self.menu_manager = menu_manager
        self.permission_manager = permission_manager
        self.routes: Dict[str, Dict] = {}
    
    def register_route(self, path: str, name: str, menu_item_id: str = None, 
                      required_roles: List[str] = None, metadata: Dict = None):
        """Register a route with navigation metadata"""
        self.routes[path] = {
            'name': name,
            'menu_item_id': menu_item_id,
            'required_roles': required_roles or [],
            'metadata': metadata or {}
        }
    
    def get_route(self, path: str) -> Optional[Dict]:
        """Get route information"""
        return self.routes.get(path)
    
    def get_breadcrumb(self, path: str) -> List[Dict]:
        """Get breadcrumb navigation for a path"""
        breadcrumb = []
        route_info = self.get_route(path)
        
        if not route_info:
            return breadcrumb
        
        # Add root
        breadcrumb.append({
            'label': 'Home',
            'url': '/',
            'active': False
        })
        
        # Traverse menu to find path
        def find_menu_path(items, target_id, current_path=[]):
            for item in items:
                new_path = current_path + [item]
                if item.id == target_id:
                    return new_path
                
                result = find_menu_path(item.children, target_id, new_path)
                if result:
                    return result
            return None
        
        menu_item_id = route_info.get('menu_item_id')
        if menu_item_id:
            path_items = find_menu_path(self.menu_manager.root_items, menu_item_id)
            if path_items:
                for item in path_items:
                    breadcrumb.append({
                        'label': item.label,
                        'url': item.url,
                        'active': False
                    })
                # Mark last as active
                if breadcrumb:
                    breadcrumb[-1]['active'] = True
        
        return breadcrumb
    
    def get_active_menu_item(self, path: str) -> Optional[str]:
        """Get active menu item ID for current path"""
        route_info = self.get_route(path)
        if route_info:
            return route_info.get('menu_item_id')
        return None
