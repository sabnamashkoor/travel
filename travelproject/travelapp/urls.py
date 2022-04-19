from . import views
from django.urls import path
urlpatterns = [
    path('', views.demo, name='demo'),

   # path('add/', views.addition, name='addition'),

    # path('home/', views.home, name='home'),
    #
    # path('contact/', views.contact, name='contact'),
    #
    # path('thanks/', views.thanks, name='thanks')

]


