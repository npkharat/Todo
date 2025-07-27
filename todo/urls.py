from django.urls import path
from django.contrib import admin


from todo  import views

urlpatterns =[
   
    path('',views.home, name='home'),
    path('add_todo',views.add_todo, name='add_todo'),
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name='mark_as_undone'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
]