import pytest
from app.navigation.menu import MenuManager
from app.navigation.router import NavigationRouter
from app.navigation.permissions import PermissionManager

class TestNavigationRouter:
    def test_register_route(self):
        menu_mgr = MenuManager()
        perm_mgr = PermissionManager()
        router = NavigationRouter(menu_mgr, perm_mgr)
        
        router.register_route('/test', 'test', 'test_menu')
        
        route = router.get_route('/test')
        assert route is not None
        assert route['name'] == 'test'
        assert route['menu_item_id'] == 'test_menu'
    
    def test_get_active_menu_item(self):
        menu_mgr = MenuManager()
        perm_mgr = PermissionManager()
        router = NavigationRouter(menu_mgr, perm_mgr)
        
        router.register_route('/dashboard', 'dashboard', 'dashboard_menu')
        
        active = router.get_active_menu_item('/dashboard')
        assert active == 'dashboard_menu'
