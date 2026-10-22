from django.shortcuts import render, redirect
from .models import Product, Service, AppointmentRequest, ContactMessage

def home(request):
    return render(request, 'home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def grooming(request):
    
    services = Service.objects.filter(is_published=True)

    if request.method == 'POST':
    
        service_id = request.POST.get('service')
        service_instance = Service.objects.get(id=service_id) if service_id else None

    
        AppointmentRequest.objects.create(
            owner_name=request.POST.get('owner_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            pet_name=request.POST.get('pet_name'),
            species=request.POST.get('species'),
            service=service_instance,
            preferred_date=request.POST.get('preferred_date'),
            preferred_time=request.POST.get('preferred_time'),
            notes=request.POST.get('notes')
        )
        
        return redirect('grooming')

    return render(request, 'grooming.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        
        return redirect('contact')
        
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')