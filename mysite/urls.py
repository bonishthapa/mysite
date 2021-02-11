"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name='register'),
    path('login',views.loginuser, name='login'),
    path('logout',views.logoutuser, name='logout'),
    path('', views.home, name ='home'),
    #path('createpost', views.CreatePost.as_view(),name='createpost'),
    path('createpost', views.createPost,name='createpost'),
    path('update/<int:pk>', views.updatePost,name = 'updatepost'),
    path('detailpost/<int:pk>', views.DetailPost.as_view(), name='detailpost'),
    path('mypost',views.mypost, name='mypost'),
    path('userdetail', views.userDetail, name='userdetail'),
    #path('deletepost/<int:pk>', views.DeletePost.as_view(), name='deletepost'),
    path('deletepost/<int:pk>', views.deletePost, name='deletepost'),
    path('userinfo_form',views.userInfo_form,name='userform'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)