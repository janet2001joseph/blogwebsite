from django.shortcuts import render

from .models import blog,slide



# Create your views here.
def home(request):
    obj=blog.objects.all()
    obj1 = slide.objects.all()
    return render(request,'index.html',{'data': obj,'values':obj1})
def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')