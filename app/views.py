from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='app:login')
def homeView(request):


    context = {}
    return render(request, 'app/home.html', context)