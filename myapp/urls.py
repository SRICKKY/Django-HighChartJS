from django.urls import path, include
from myapp.views import ticket_class_view as index

urlpatterns = [
    path('', index, name='index')
]