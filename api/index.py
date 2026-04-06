import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')

# Get the WSGI application
app = get_wsgi_application()

# Vercel expects the app to be named 'app'
application = app