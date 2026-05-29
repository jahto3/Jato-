from .menu import MenuManager
from .router import NavigationRouter
from .permissions import PermissionManager

_menu_manager = None
_nav_router = None
_permission_manager = None

def init_navigation(app):
    """Initialize navigation system"""
    global _menu_manager, _nav_router, _permission_manager
    
    _permission_manager = PermissionManager()
    _menu_manager = MenuManager()
    _nav_router = NavigationRouter(_menu_manager, _permission_manager)
    
    # Make navigation accessible in templates
    app.jinja_env.globals.update(
        get_menu=get_menu,
        get_navigation=get_navigation
    )

def get_menu():
    """Get menu manager instance"""
    return _menu_manager

def get_navigation():
    """Get navigation router instance"""
    return _nav_router

def get_permission_manager():
    """Get permission manager instance"""
    return _permission_manager
