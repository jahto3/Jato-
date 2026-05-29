# Jato - IOPn Navigation System

A Python web application navigation system with menu structure support.

## Features

- Hierarchical menu structure
- Dynamic route registration
- Role-based access control
- Menu item visibility control
- URL path management

## Project Structure

```
jato-navigation/
├── app/
│   ├── __init__.py
│   ├── navigation/
│   │   ├── __init__.py
│   │   ├── menu.py
│   │   ├── router.py
│   │   └── permissions.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   └── templates/
│       ├── base.html
│       └── menu.html
├── config.py
├── requirements.txt
├── main.py
└── tests/
    ├── __init__.py
    ├── test_menu.py
    └── test_router.py
```

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Documentation

See `/docs` for detailed documentation.
