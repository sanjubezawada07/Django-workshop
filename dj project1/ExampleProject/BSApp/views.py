from django.shortcuts import render,redirect
from .models import Student,Employee
from .forms import EmForm
from django.contrib import messages


def home(request):
	return render(request,'home.html')
def about(request):
	return render(request,'about.html')
def student(request):
	m = Student.objects.all()
	if request.method == "POST":
		g = request.POST['a']
		k = request.POST['b']
		h = request.POST['c']
		t = Student(rn=g,sn=k,sy=h)
		t.save()
		return redirect('/std')
	return render(request,'student.html',{"s":m})
# Create your views here.
def stdup(request,k):
	c=Student.objects.get(id=k)
	if request.method == "POST":
		c.rn=request.POST['a']
		c.sn=request.POST['b']
		c.sy=request.POST['c']
		c.save()
		return redirect('/std')
	return render(request,'stup.html',{"v":c})
def stdel(request,n):
	y=Student.objects.get(id=n)
	if request.method =="POST":
		y.delete()
		return redirect('/std')
	return render(request,'del.html',{"h":y})
def emp(request):
	u=Employee.objects.all()
	if request.method == "POST":
		d=EmForm(request.POST)
		if d.is_valid():
			d.save()
			messages.success(request,"employee added successfully")
			return redirect('/empl')
	d=EmForm()
	return render(request,'empy.html',{"d":d,"ud":u})
def emupd(request,z):
	a=Employee.objects.get(id=z)
	if request.method =="POST":
		n=EmForm(request.POST,instance=a)
		if n.is_valid():
			n.save()
			messages.info(request,"employee data updated successfully")
			return redirect('/empl')
	n=EmForm(instance=a)
	return render(request,'emupdate.html',{"b":n})
def emdelete(request,o):
	p=Employee.objects.get(id=o)
	if request.method =="POST":
		p.delete()
		messages.warning(request,"employee record deleted succesfully")
		return redirect('/empl')
	return render(request,'emdt.html',{"c":p})