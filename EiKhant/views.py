from django.shortcuts import render, redirect
from blogs.models import Category, Albums
def home(request):
    context={
        'categories': Category.objects.all,
        'albums': Albums.objects.all,
    }
    return render(request, 'base/main.html', context)



def thankyou(request):
    return render(request, 'accessories/thankyou_template.html')
