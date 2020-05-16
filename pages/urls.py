from django.urls import path
from . import views # Import all views from Pages App (Current)

urlpatterns = [
    #path('', views.index, name='index'),
    path('',views.index,{'pagename':''},name='home'),
    path('<str:pagename>',views.index, name='index'),
]