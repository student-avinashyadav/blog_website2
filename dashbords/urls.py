from django.urls import path
from . import views

urlpatterns = [
    # path for categories
    path('',views.dashboard,name='dashboard'),
    path('categories/',views.categories,name='categories'),
    path('categories/add',views.add_categories,name='add_categories'),
    path('categories/edit/<int:pk>',views.edit_category,name='edit_category'),
    path('categories/delete/<int:pk>',views.delete_category,name='delete_category'),
    # path for posts
    path('posts',views.posts,name='posts'),
    path('posts/add',views.add_post,name='add'),
    path('posts/delete/<int:pk>',views.delete_post,name='delete_post'),
    path('post/edit/<int:pk>',views.edit_post,name='edit_post')
   
    
   
]