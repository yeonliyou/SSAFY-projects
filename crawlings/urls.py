from django.urls import path
from . import views


app_name = 'crawlings'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
