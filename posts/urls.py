from MyBlog import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
app_name = 'posts'
urlpatterns = [
    path('',index, name = 'index'),
    #path('new_post/', PostCreateView.as_view(), name='new_post'),
    #path("publishers/", PostListView.as_view(), name = 'index'),
    #path('details_post/<int:id>', details, name = 'details_post'),
    path('new_post/', new_post, name='new_post'),
    path('search_post/', search_post, name='search_post'),
    path('update_post/<int:id>', update_post, name='update_post'),
    path('delete_post/<int:id>', delete_post, name='delete_post'),
    path('create_comment/<int:id>', create_comment, name='create_comment'),
    path('update_comment/<int:id>', update_comment, name='update_comment'),
    path('delete_comment/<int:id>', delete_comment, name='delete_comment')

]
