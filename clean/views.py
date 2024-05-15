from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from clean.utils import send_email_with_html_body
from django.conf import settings
from datetime import datetime

from clean.models import Service, PhotoGallery

def service_list(request):
    user = request.user
    services = Service.objects.all()

    context = {
        'services':services,
        'user':user,
    }
    
    return render(request, 'index.html', context)

def services(request):
    user = request.user
    services = Service.objects.all()

    context = {
        'services':services,
        'user':user,
    }
    
    return render(request, 'services.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.all().order_by('-id')[:2]
    photo_gallery = PhotoGallery.objects.filter(service_id=service.id)

    context = {
        'service':service,
        'related_services':related_services,
        'photo_gallery':photo_gallery,
    }
    
    return render(request, 'services-detail.html', context)

def send_email(request):
    # TODO: ecrire la funtion permettant d'envoyer un email pour la prise de render-vous
    if request.method =="POST":
        template = 'contact.html'
        sender_username = request.POST.get('sender_username')
        sender_email = request.POST.get('sender_email')
        sender_message = request.POST.get('sender_message')
        receivers = [send_email]
        context = {
            'sender_email':sender_email,
            'sender_message':sender_message,
            'sender_username':sender_username,
            'date': datetime.today().date

        }

        has_send = send_email_with_html_body(
            subject=sender_message,
            receivers = receivers,
            template=template,
            context=context
        )
        if has_send:
            return redirect('list')        
        else:
            return redirect('contact')
    
    return render(request, 'contact.html', context)