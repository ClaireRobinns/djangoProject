"""EiKhant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, thankyou
from booking.views import booking
from blogs.views import category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('myblog/', include('blogs.urls'), name='myblogs'),
    path('booking/', booking, name='booking'),
    path('albums/', include('albums.urls'), name='albums'),
    path('8cfed88cf0cae00f65a863094119dab4', thankyou, name='thanks'),

    # path('cat=<int:id>', category, name='cat')
]
