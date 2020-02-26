from django.shortcuts import render

# Create your views here.

#def home(request):
#    return render(request, 'home.html')

def calculator(request):
    if request.POST.get('x') and request.POST.get('y'):
        x = float(request.POST['x'])
        y = float(request.POST['y'])
        if request.POST.get('add'):
            result = x + y
        elif request.POST.get('sub'):
            result = x - y
        elif request.POST.get('mul'):
            result = x * y
        elif request.POST.get('div'):
            result = x / y
        return render(request , "home.html",{'result' : result} )
    return render(request , "home.html")
