import os, sys
sys.path.append('/home/web/svarochnyy.ru/project/')
sys.path.append('/home/web/svarochnyy.ru/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

os.environ['PYTHON_EGG_CACHE'] = '/home/web/.python-eggs'
