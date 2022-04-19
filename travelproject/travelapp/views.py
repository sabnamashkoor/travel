from operator import mul

from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()

    return render(request, "index.html",{'result':obj,'result1':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     y =int( request.GET['num2'])
#     sum=x+y
#     sub=x-y
#     mult=x*y
#     div=x/y
#     return render(request,"result.html",{'result1':sum,'result2':sub,'result3':mult,'result4':div})
#


# def about(request):
#     return render(request, "result.html")
# def home(request):
#     return render(request, "homes.html")
# def contact(request):
#     return render(request, "contact.html")
# def thanks(request):
#     return render(request, "thanks.html")



