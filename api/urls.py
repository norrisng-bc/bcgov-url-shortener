from django.urls import path
from . import views

# TODO: this means a valid url is https://{domain}/api/{shortcode}. We want to get rid of the api/ bit
urlpatterns = [
    path('<str:shortcode>', views.get_url)
]
