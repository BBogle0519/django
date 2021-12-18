from .base import *

DATABASES = { 
	'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django_local', 
        'USER': 'root', 
        'PASSWORD': 'kmrs12!@', 
        'HOST': 'localhost', 
        'PORT': '3306', 
     } 
}