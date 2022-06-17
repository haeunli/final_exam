from django.urls import path

from polls import views

urlpatterns = [
    path('test/',views.index, name='index'),
    path('test/information/', views.index1, name='index1'),
    path('test/algorithm/', views.index2, name='index2'),
    path('test/data/', views.index3, name='index3'),
]
