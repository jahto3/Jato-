from typing import List, Dict, Set

class PermissionManager:
    """Manages user roles and permissions"""
    
    def __init__(self):
        self.roles: Dict[str, Set[str]] = {}
        self.default_roles: List[str] = ['user']
    
    def create_role(self, role_name: str, permissions: Set[str] = None):
        """Create a new role with permissions"""
        if permissions is None:
            permissions = set()
        self.roles[role_name] = permissions
    
    def add_permission(self, role_name: str, permission: str):
        """Add permission to a role"""
        if role_name in self.roles:
            self.roles[role_name].add(permission)
    
    def has_permission(self, role_name: str, permission: str) -> bool:
        """Check if role has permission"""
        if role_name in self.roles:
            return permission in self.roles[role_name]
        return False
    
    def has_any_role(self, user_roles: List[str], required_roles: List[str]) -> bool:
        """Check if user has any of the required roles"""
        if not required_roles:
            return True
        return any(role in user_roles for role in required_roles)
