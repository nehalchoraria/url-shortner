from django.urls import path

from .views import index,redirectToUrl

urlpatterns = [
    path('<str:link>/', redirectToUrl, name='redirectToUrl'),
    path('', index, name='index')
]