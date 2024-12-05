from django.shortcuts import render

app_name = 'dress'
# Create your views here.
def cloths(request):
    return render(request,'cloths.html')