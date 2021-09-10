from urlhandler.models import shorturl
from urlhandler.views import generate
from django.contrib import admin
from .models import shorturl

admin.site.register(shorturl)
