from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def get_a_quote(request):
    return render(request, 'get_a_quote.html')
def index(request):
    return render(request, 'index.html')
def pricing(request):
    return render(request, 'pricing.html')
def service_details(request):
    return render(request, 'service_details.html')
def services(request):
    return render(request, 'services.html')
def starter_page(request):
    return render(request, 'starter-page.html')