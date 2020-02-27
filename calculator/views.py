from django.shortcuts import render
from .models import ResultHis
# Create your views here.

#def home(request):
#    return render(request, 'home.html')

def calculator(request):
    allHistory = None
    if request.POST.get('x') and request.POST.get('y'):
        x = float(request.POST['x'])
        y = float(request.POST['y'])

        if request.POST.get('add'):
            operation = '+'
            result = x + y
        elif request.POST.get('sub'):
            operation = '-'
            result = x - y
        elif request.POST.get('mul'):
            operation = '*'
            result = x * y
        elif request.POST.get('div'):
            operation = '/'
            result = x / y

        ResultHis.objects.create(num_x=x, num_y=y, operation=operation, num_result=result)
        allHistory = ResultHis.objects.all()
        return render(request , "home.html",{'result' : result,'allHistory': allHistory} )
    return render(request , "home.html",{'allHistory': allHistory} )
