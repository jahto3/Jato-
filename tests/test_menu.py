import pytest
from app.navigation.menu import MenuItem, MenuManager

class TestMenuItem:
    def test_create_menu_item(self):
        item = MenuItem(id='test', label='Test', url='/test')
        assert item.id == 'test'
        assert item.label == 'Test'
        assert item.url == '/test'
        assert item.visible == True
    
    def test_add_child(self):
        parent = MenuItem(id='parent', label='Parent', url='/parent')
        child = MenuItem(id='child', label='Child', url='/child')
        
        parent.add_child(child)
        
        assert len(parent.children) == 1
        assert parent.children[0] == child
        assert child.parent_id == 'parent'

class TestMenuManager:
    def test_add_item(self):
        manager = MenuManager()
        item = MenuItem(id='test', label='Test', url='/test')
        
        manager.add_item(item)
        
        assert manager.get_item('test') == item
        assert item in manager.root_items
    
    def test_get_menu_with_roles(self):
        manager = MenuManager()
        
        public = MenuItem(id='public', label='Public', url='/public')
        admin = MenuItem(id='admin', label='Admin', url='/admin', required_roles=['admin'])
        
        manager.add_item(public)
        manager.add_item(admin)
        
        # No roles - should only see public
        menu = manager.get_menu([])
        assert len(menu) == 1
        assert menu[0].id == 'public'
        
        # With admin role
        menu = manager.get_menu(['admin'])
        assert len(menu) == 2
