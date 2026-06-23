
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from blogs import views as blogsview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('category/',include('blogs.urls')),
    path('blogs/<slug:slug>/',blogsview.blogs,name='blogs'),
    path('blogs/search/',blogsview.search,name='search'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',include('dashbords.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
