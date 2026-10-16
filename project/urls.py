"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from empmngt import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', views.news),
    path('home/', views.home),
    path('calender/', views.calender),
    path('viewemp/', views.viewemp, name='viewemp'),
    path('addnews/', views.addnews, name='addemp'),
    path('jobs/', views.jobs),
    path('jobopen/', views.jobopen),
    path('holidays/', views.holidays),
    path('addemp/', views.employee, name='add_employee'),
    path('hrmanager/', views.dashboardview, name='hrmanager'),
    path('empdash/', views.empdashboard),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('download/',views.download_csv),
    path('empupdate/<int:id>/',views.updateview, name='updateview'),
    path('empdelete/<int:id>/', views.deleteview),
    path('newsupdate/<int:id>/',views.newsupdate),
    path('newsdelete/<int:id>/',views.newsdelete),
    path('jobupdate/<int:id>/', views.jobupdate, name='jobupdate'),
    path('jobdelete/<int:id>/', views.jobdelete, name='jobdelete'),
    path("employee/<int:id>/",views.employee_detail,name="employee_detail"),
    path('deleteholiday/<int:id>/',views.deleteholiday),
    path('holidayupdate/<int:id>/', views.holidayupdate, name='holidayupdate'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)