
from django.contrib import admin
from django.contrib.auth import login
from django.urls import path, include

# noinspection PyUnresolvedReferences
from webProyecto2app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webProyecto2app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
