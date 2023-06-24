from django.shortcuts import render,HttpResponse 
# from .models import UserInfo 
# Create your views here.

def index(request):
    if request.method == 'GET':
        # name = UserInfo.objects.get(id=1).name
        return HttpResponse("歡迎使用")
    

def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return render(request, "user_add.html")
