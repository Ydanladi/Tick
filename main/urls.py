from django.urls import path, include
from django.contrib import admin
from main.views import PostView,PostDetail,AddPost,UpdatePost,DeletePost,ProfileView, CommentPost,Question,Privacy,Terms,Contact

app_name='main'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PostView.as_view(), name='home'),
    path('create_post/', AddPost.as_view(), name="create" ),
    path('details/<int:pk>', PostDetail.as_view(), name="details"),
    path('detail/update/<int:pk>',UpdatePost.as_view(), name="update"),
    path('detail/<int:pk>/Delete',DeletePost.as_view(), name="Delete"),
    path('profile/',ProfileView, name='profile'),
    path('details/<int:pk>/comment', CommentPost.as_view(), name="add_comment"),
    path('about/',Question, name='about'),
    path('privacy/',Privacy, name='privacy'),
    path('terms/',Terms, name='terms'),
    path('contact',Contact, name='contact'),
]