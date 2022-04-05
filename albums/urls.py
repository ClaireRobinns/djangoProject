from django.urls import path
from .views import albums, category
urlpatterns = [
    path('', albums, name='albums'),
    path('<str:name>', category, name='category'),
]