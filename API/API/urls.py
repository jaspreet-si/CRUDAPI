"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from appi import views
from appi import GenericView
from appi import modelvieset

from appi import Viewset

router=DefaultRouter()

router.register('viewapi',Viewset.studentView,basename="api")

router.register('studentmodelapi',modelvieset.studentapi,basename="model")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit/<int:id>',views.make_changes_api), #function based url
    path('api/',views.api),
    path('student/',views.StudentApi.as_view()),
    path('student/<int:id>',views.StudentApi.as_view()),#class url
    path("generic",GenericView.studentCP.as_view()),
    path("generic/<int:pk>",GenericView.RUDAPI.as_view()),
    path("abc/",GenericView.studentgeneric.as_view()),
    path('abc/<int:pk>',GenericView.RUD.as_view()),
    path('',include(router.urls)) ,#router url
    path('',include(router.urls))

    

]
