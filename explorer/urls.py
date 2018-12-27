from django.urls import include, path

from .views import home
app_name = 'explorer'

urlpatterns = [
    path('', home.home, name='home'),
]
