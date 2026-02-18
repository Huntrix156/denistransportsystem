from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def pricing(request):
    return render(request, 'pricing.html')
def services_details(request):
    return render(request, 'services-details.html')
def services(request):
    return render(request, 'services.html')
def starter_page(request):
    return render(request, 'starter-page.html')