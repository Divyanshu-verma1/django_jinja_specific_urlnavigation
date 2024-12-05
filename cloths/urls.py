from django.urls import path
from cloths.views import *

urlpatterns = [
    path('cloths/',cloths,name='cloths')
]