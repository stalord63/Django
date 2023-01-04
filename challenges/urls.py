from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>",views.index_number),
    path("<str:month>",views.index)
    
   
]