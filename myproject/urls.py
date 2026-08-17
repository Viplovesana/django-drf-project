"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from myapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('student_list/', views.student_list, name='student_list'),
#     path('student_detail/<int:pk>/', views.student_detail, name='student_detail')
# ]

# ------COMBINE VIEWS-----------------------------------------------------------------------------------

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('combine_api/', views.combine_api, name='combine_api')
# ]

# ------API VIEWS-----------------------------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('protected_api/', views.protected_api, name='protected_api')
]