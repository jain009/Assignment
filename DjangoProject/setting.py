# settings.py
INSTALLED_APPS = [
    # Other apps
    'channels',
    'chat',
]

# Channels configuration
ASGI_APPLICATION = 'chat_app.asgi.application'

# Add your database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
