"""
URL configuration for config project.

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
from django.urls import path
from hello.views import (
    home,
    edit_person,
    delete_person,
    peope_api,
    person_api
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('edit/<int:id>/', edit_person, name='edit_person'),
    path('delete/<int:id>/', delete_person, name='delete_person'),
    path('api/people/', peope_api, name='people_api'),
    path('api/people/<int:person_id>/', person_api, name="person_api"),
]
