from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':77210,'b':3000,'c':400}
    return render(request,'condition.html',context=d)


def condition1(request):
    d={'a':77210,'b':3000,'c':400}
    return render(request,'condition1.html',context=d)
