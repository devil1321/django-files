from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path('',views.addFile,name="add-file"),
    path('get-file/<str:filename>/',views.getFile,name="getFile"),
    
]