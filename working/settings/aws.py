from .base import *

DATABASES = { 
	'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'aws_server',
        'USER': 'test', 
        'PASSWORD': 'kmrs12', 
        'HOST': '3.36.135.85', 
        'PORT': '3306', 
     } 
}