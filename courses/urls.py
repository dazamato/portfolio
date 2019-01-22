from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:course_id>', views.detail, name='detail'),
    path('<int:course_id>/addlecture/', views.addlecture, name='addlecture'),
    # path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post')


]
