from django.shortcuts import render

app_name = 'eat'

# Create your views here.
def food(request):
    return render(request,'food.html')