from django.urls import path 
from . import views

urlpatterns = [
    path('',views.sample),
    path('table/',views.table),
    path('task/',views.task),
    path('student/',views.student),
    path('task1/',views.data)
]
