from django.urls import path
from . import views

urlpatterns = [
    path('', views.userList, name='index'),
    path('create/', views.create, name='create'),
    path('create/<int:pk>/deposit', views.deposit, name='deposit'),
    path('create/<int:pk>/expense', views.expense, name='expense'),
    path('detail/<int:pk>',views.detail, name='detail'),
    path('newUser/', views.newUser, name='newUser'),
    path('create/<int:pk>/edit', views.edit, name='edit'),

]
