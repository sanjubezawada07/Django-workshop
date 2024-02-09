from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
	return HttpResponse("<h1>sanjana</h1")
def greet(sd,n):
	return HttpResponse(f"Hi Welcome {n}")

def stdnt(request,a,b,c="VVIT"):
	return HttpResponse(f" college name:{c} <br>  student name:{a}\n <br> age:{b}")
def dis(request,a):
	return HttpResponse(f"<span>hey</span> <span style='color:red'>{a}</span")
def sam(request,n,a):
	return HttpResponse("<head><style>.b{color:red}</style>"+"hi"+f"<span class='b'> {n}</span>\n<span>i</span><span style='color:purple'> {a} you</span>")
def fln(self,a):
	return HttpResponse(f"<script>alert('{a}');</script>")
def ssm(request,a,b,c,d):
	return HttpResponse(f"<script>alert('welcome{a}');</script><table border='1'><tr><th>roll no</th><td>{b}</td></tr><tr><th>branch</th><td>{c}</td></tr><tr><th>year</th><td>{d}</td></tr></table>")
def abbs(request,a):
	return render(request,'sample.html')
def ass(request,a):
	return render(request,'demo.html',{'z':a})
def emp(request,a,b,c):
	return render(request,'employee.html',{'n':a,'s':b,'d':c})
def pps(request):
	if request.method == "POST":
		a=request.POST['sn']
		b=request.POST['sr']
		c=request.POST['sy']
		d=request.POST['sb']
		print(a)
		print(b)
		print(c)
		print(d)
		return render(request,'det.html',{'a':a,'b':b,'c':c,'d':d})
	return render(request,'std.html')