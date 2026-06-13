from django.shortcuts import render, get_object_or_404
from .models import Service


def service_list(request):
    services = Service.objects.filter(is_active=True)
    categories = Service.CATEGORY_CHOICES

    category_filter = request.GET.get('category')
    if category_filter:
        services = services.filter(category=category_filter)

    context = {
        'services': services,
        'categories': categories,
        'selected_category': category_filter,
    }
    return render(request, 'services/service_list.html', context)


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk, is_active=True)
    return render(request, 'services/service_detail.html', {'service': service})
