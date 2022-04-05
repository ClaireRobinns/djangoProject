from django.urls import path
from .views import Blogging, pageNo, createPost, category, albums

urlpatterns = [
    path('',Blogging, name='myblog'),
    path('id=<int:id>/', pageNo, name='id'),
    path('create/', createPost, name='createPost'),
    # path('albums/', albums, name='albums'),
    path('albums/', category, name='categ')

]