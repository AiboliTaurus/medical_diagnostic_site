from django.shortcuts import render
from django.http import JsonResponse
from apps.feedback.forms import ContactForm
from apps.services.models import Service
from apps.pages.models import CompanyInfo, Doctor
from django.contrib import messages


def home(request):
    services = Service.objects.filter(is_active=True)[:6]
    company_info = CompanyInfo.objects.first()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение отправлено! Мы свяжемся с вами.')
            form = ContactForm()

    context = {
        'services': services,
        'company_info': company_info,
        'form': form,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    company_info = CompanyInfo.objects.first()
    doctors = Doctor.objects.all()
    context = {
        'company_info': company_info,
        'doctors': doctors,
    }
    return render(request, 'pages/about.html', context)


def contacts(request):
    company_info = CompanyInfo.objects.first()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение отправлено! Мы свяжемся с вами.')
            form = ContactForm()

    context = {
        'company_info': company_info,
        'form': form,
    }
    return render(request, 'pages/contacts.html', context)


def get_doctors_by_service(request):
    service_id = request.GET.get('service_id')
    if service_id:
        doctors = Doctor.objects.filter(services__id=service_id)
        data = {'doctors': list(doctors.values('id', 'name', 'specialty'))}
    else:
        data = {'doctors': []}
    return JsonResponse(data)
