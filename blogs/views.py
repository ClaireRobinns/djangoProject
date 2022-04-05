from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blogging, Albums, Category
# Create your views here.
def Blogging(request):
    HttpResponse('<h1> This is blog site.</h1>')
def pageNo(request, id):
    pass
def createPost(request):
    pass

def category(request, id):
    pass

def albums(request):
    pass
