from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'blog2/demo.html')