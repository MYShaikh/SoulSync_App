"""
URL configuration for DatingSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp.views import BooksView
from myapp.views import Homeview, UserFormview, ProductView, AllOurUsersView, DashboardView, SignUpView, LoginView, UserProfileView, UserDisplayView
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', BooksView.as_view(),name="MyBook"),
    path('nonesense/', Homeview.as_view(), name="Homeview" ),#name can be anything. which is the one in ''
    path('nonesenses/', UserFormview.as_view(), name="userFormview" ),
    path('product/', ProductView.as_view(), name="productView"),
    path('allusers/', AllOurUsersView.as_view(), name="allUsers"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('userinfo/<int:id>', UserProfileView.as_view(), name="userinfo"),
    path('userinfo/', UserProfileView.as_view(), name="userinfo"),
    path('userdisplay/', UserDisplayView.as_view(), name="userdisplay"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)