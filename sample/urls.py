from django.contrib import admin
from django.urls import path
from .views import planet_view

admin.site.site_header = 'Солнечная система'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', planet_view)
]
