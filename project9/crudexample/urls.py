"""crudexample URL Configuration

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
from django.urls import path,include 
from employee import views
from django.conf.urls.static import static

urlpatterns = [  
    path('signup/',views.signup,name="signup"),
    # path('login/',views.loginPage,name="login"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('employee.urls',namespace='accounts')),
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('admin/read',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('', views.dashboardPage),
    # path('', views.loginPage),
    path('admin/dashboard', views.dashboardPage, name='dashboard'),
    path('admin/create', views.adminCreatePage, name='admin-create'),
    path('admin/read', views.adminReadPage, name='admin-read'),
    path('admin/update', views.adminUpdatePage, name='admin-update'),
    # path('admin/delete', index.createAdminPage, name='admin-delete'),
    path('excel/uploads', views.simple_upload, name='excel-uploads'),
    path('accounts/profile/', views.dashboardPage, name='dashboard'),
]  