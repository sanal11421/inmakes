# from django.http import HttpResponse
# from django.shortcuts import render
#
#
# # Create your views here.
# def home(request):
#     return HttpResponse("hello")
#
#
# def about(request):
#     name="india"
#     return render(request, "about.html",{'obj':name})
#
#
# def contact(request):
#     return HttpResponse("contact")
#
# def detail(request):
#     return render(request,'detail.html')
# def thanks(request):
#     return HttpResponse("THANK YOU")
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from csolarapp.models import Solar
from .forms import SolarForm

def index(request):
    solar=Solar.objects.all()
    context={
        'solar_list':solar
    }
    return render(request,"index.html",context)
def detail(request, solar_id):
    solar=Solar.objects.get(id=solar_id)
    return render(request,"detail.html",{'solar':solar})
def add_solar(request):

    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        solar=Solar(name=name,desc=desc,year=year,img=img)
        solar.save()

    return render(request,"add.html")
def update(request,id):
    solar=Solar.objects.get(id=id)
    form=SolarForm(request.POST or None, request.FILES,instance=solar)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render (request,'edit.html',{'form':form,'solar':solar})
def delete(request,id):
    if request.method=='POST':
        solar=Solar.objects.get(id=id)
        solar.delete()
        return redirect('/')
    return render(request,'delete.html')