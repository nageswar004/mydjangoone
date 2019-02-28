from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index2.html') # render loads template inside call html file
