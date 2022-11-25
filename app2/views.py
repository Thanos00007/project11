from django.shortcuts import render

# Create your views here.
def condition3(request):
    d={'a':77210,'b':3000,'c':400}
    return render(request,'condition.html',context=d)

def condition4(request):
    d={'name':'Debasish'}
    return render(request,'condition4.html',d)