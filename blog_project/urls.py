"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('p/<slug:slug>/',views.post_detail_view,name='post-detail'),  
    path('post/new/',views.post_create_view,name='post-create'),
    path('post/<int:pk>/update/', views.post_update_view, name='post-update'),  
    path('post/<int:pk>/delete/',views.post_delete_view, name='post-delete'), 
    path('search/nccbuddies/', views.search_view, name='search'), 
    path('like/post',views.like_view,name='like'),
    path('report/post/',views.post_report_view,name='report'),
    path('report/user/',views.user_report_view,name='report-user'),
    path('<str:username>/notifications/',views.notifications_view,name='notifications'),
    path('<str:username>/notifications/update/',views.notifications_update_view,name='notifications-update'),
    path('<str:username>/notifications/count/',views.notifications_unread_count_view,name='notifications-count'),
]


