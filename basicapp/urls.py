from . import views
from django.urls import path

urlpatterns = [
    path('view/' , views.view , name="view"),
    path('home/' , views.home , name="home"),
    path('detail/<int:id>' , views.detail , name="detail"),
]
