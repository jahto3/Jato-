from app import create_app
from app.navigation import get_menu, get_navigation

app = create_app('development')

if __name__ == '__main__':
    # Initialize menu structure
    menu = get_menu()
    navigation = get_navigation()
    
    # Add root menu items
    from app.navigation.menu import MenuItem
    
    home = MenuItem(
        id='home',
        label='Home',
        url='/',
        icon='house',
        order=1
    )
    menu.add_item(home)
    
    dashboard = MenuItem(
        id='dashboard',
        label='Dashboard',
        url='/dashboard',
        icon='speedometer2',
        order=2,
        required_roles=['admin']
    )
    menu.add_item(dashboard)
    
    settings = MenuItem(
        id='settings',
        label='Settings',
        url='/settings',
        icon='gear',
        order=3,
        required_roles=['admin']
    )
    menu.add_item(settings)
    
    # Register routes
    navigation.register_route('/', 'home', menu_item_id='home')
    navigation.register_route('/dashboard', 'dashboard', menu_item_id='dashboard', required_roles=['admin'])
    navigation.register_route('/settings', 'settings', menu_item_id='settings', required_roles=['admin'])
    
    # Run the application
    app.run(debug=True, port=5000)
