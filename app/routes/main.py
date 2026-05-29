from flask import render_template, request
from . import main_bp
from app.navigation import get_menu, get_navigation

@main_bp.route('/')
def index():
    """Home page"""
    menu = get_menu()
    navigation = get_navigation()
    
    # Get menu items for current user (no roles = public menu)
    menu_items = menu.get_menu([])
    
    return render_template('index.html', menu_items=menu_items)

@main_bp.route('/dashboard')
def dashboard():
    """Dashboard page"""
    menu = get_menu()
    navigation = get_navigation()
    
    menu_items = menu.get_menu(['admin'])
    breadcrumb = navigation.get_breadcrumb(request.path)
    active_item = navigation.get_active_menu_item(request.path)
    
    return render_template('dashboard.html', 
                         menu_items=menu_items,
                         breadcrumb=breadcrumb,
                         active_item=active_item)

@main_bp.route('/settings')
def settings():
    """Settings page"""
    menu = get_menu()
    navigation = get_navigation()
    
    menu_items = menu.get_menu(['admin'])
    breadcrumb = navigation.get_breadcrumb(request.path)
    active_item = navigation.get_active_menu_item(request.path)
    
    return render_template('settings.html',
                         menu_items=menu_items,
                         breadcrumb=breadcrumb,
                         active_item=active_item)
