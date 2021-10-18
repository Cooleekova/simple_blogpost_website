from django.urls import path
from django.contrib.auth.decorators import login_required
from posts.views import PostView, DeletePostView, UpdatePostView, new_post

app_name = 'posts'

urlpatterns = [
    path('home/', login_required(PostView.as_view(template_name="home.html")), name='posts'),
    path('new/', login_required(new_post), name='add_post'),
    path('<int:pk>/update', login_required(UpdatePostView.as_view()), name='update_post'),
    path('<int:pk>/delete', login_required(DeletePostView.as_view()), name='delete_post'),
]
