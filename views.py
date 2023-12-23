from django.shortcuts import render,redirect
from .models import Employee
#from django.http import HttpResponse

# Create your views here.
def index(request):
    data=Employee.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        gender=request.POST.get("gender")
        print(name,email,number,gender)
        query=Employee(name=name,email=email,number=number,gender=gender)
        query.save()
        return redirect("/")
    return render(request,"index.html")
def updateData(request,id):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        number=request.POST["number"]  
        gender=request.POST["gender"]

        edit=Employee.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.number=number
        edit.gender=gender
        edit.save()
        return redirect("/")   
        #return HttpResponse(f'Updating data for ID {id}')  
    d=Employee.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)
def deleteData(request,id):
    d=Employee.objects.get(id=id)
    d.delete()
    return redirect("/")

def about(request):
    return render(request,"about.html")