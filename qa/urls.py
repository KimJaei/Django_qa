"""qa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.post_index, name='post_index'),
    path('post_create', app.views.post_create, name='post_create'),
    path('post_new', app.views.post_new, name='post_new'),
    path('post_detail/<int:qa_id>', app.views.post_detail, name='post_detail'),
    path('post_update/<int:qa_id>', app.views.post_update, name='post_update'),
    path('post_updat/<int:qa_id>', app.views.post_updat, name='post_updat'),
    path('post_delete/<int:qa_id>', app.views.post_delete, name='post_delete'),
    path('ccreate', app.views.ccreate, name='ccreate'),
    path('cdelete/<int:comment_id>/', app.views.cdelete, name='cdelete'),
]
