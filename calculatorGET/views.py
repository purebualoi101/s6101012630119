from django.shortcuts import render

# Create your views here.
def calculatorGET(request):
    if request.GET.get('x') and request.GET.get('y'):
        x = float(request.GET['x'])
        y = float(request.GET['y'])
        if request.GET.get('add'):
            operation = '+'
            result = x + y

        elif request.GET.get('sub'):
            operation = '-'
            result = x - y

        elif request.GET.get('mul'):
            operation = '*'
            result = x * y

        elif request.GET.get('div'):
            operation = '/'
            result = x / y

        return render(request , "home2.py.html",{'result':result})
    return render(request , "home2.py.html",)
