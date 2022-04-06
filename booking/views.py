from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm
import datetime
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from blogs.models import Category
# Create your views here.
def booking(request):
    if request.method == 'POST':
        date_valid = False
        mobile_valid = False
        form = BookForm(request.POST)
        if form.is_valid():
            EVD = int(''.join([str(form.cleaned_data['eventDate']).split('-')[i] for i in range(3)]))
            TODAY = int(''.join([str(datetime.date.today()).split('-')[i] for i in range(3)]))
            if TODAY >= EVD:
                valid = False
                messages.error(request, message='The date of event is invalid.')
            else:
                date_valid = True

            if form.cleaned_data['mobile'].isdigit():
                mobile_valid = True
            else:
                messages.error(request, message='The mobile must be digit. Eg. 09123456789')

            if date_valid and mobile_valid:
                print(form.cleaned_data['eventDate'])
                name = form.cleaned_data.get('client')
                phone = form.cleaned_data.get('mobile')
                to = form.cleaned_data.get('email')
                dueDate = form.cleaned_data.get('eventDate')
                subject = "Complete Booking"
                message = "Thank you for your choice."
                html_message =f'''
                <!doctype>
                <html>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;400&display=swap" rel="stylesheet"> 
                    <body style="font-family: 'Poppins', sans-serif;">
                        <h1>{subject}</h1>
                        <img src="../static/images/this_is_black.jpg">
                        <h2> Hi {name}</h2>
                        <span><strong> Please check your information! </strong></span>
                        <div style="padding: 20px; margin: 4px;background: black;color:white;">
                        <ul style="list-style:none;">
                            <li> Name - <span style="color: red; font-weight: 600;">{name}</span></li>
                            <li> Phone - <span style="color: red; font-weight: 600;">{phone}</span></li>
                            <li> Due Date - <span style="color: red; font-weight: 600;">{dueDate.strftime('%d-%m-%Y, %A')}</span></li>
                        </ul>
                        <br/>
                        <p>I am so excited to be working with you! I'll contact you later on please wait...</p>
                    </body>
                    
                </html>
                '''
                try:
                    form.save()
                    send_mail(subject, message=message,from_email='youaccount@email.com',
                              recipient_list=[to], auth_password= '------------',
                              fail_silently=False, html_message=html_message)
                    return redirect('thanks')
                except BadHeaderError:
                    return HttpResponse('Invalid Header Found.')


    context = {
        'form': BookForm,
        'categories': Category.objects.all,
    }
    return render(request, 'Black/booking.html', context=context)
