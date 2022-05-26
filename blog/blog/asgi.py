# -*- coding: utf-8 -*-
'''
File Name:asgi.py
Program IDE:PyCharm
Create FIle Time:2022/4/28 21:29
File Create By Author:"祖华"
'''
"""
ASGI config for ASGITEST project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
#from django.core.asgi import get_asgi_application
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()
#application = get_asgi_application()
application = get_default_application()
