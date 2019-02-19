from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request, 'main/index.html')

def shop(request):
   return render(request, 'main/shop-category.html')

def services(request):
   return render(request, 'main/services.html')
