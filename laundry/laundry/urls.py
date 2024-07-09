"""
URL configuration for laundry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from LAUND import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home',views.home),
    path('login', views.loginindex),
    path('services',views.services),
    path('about',views.about),
    path('contact',views.contact),
    path('admin_home',views.admin),
    path('employee',views.employee),
    path('adminviewuser',views.adminviewuser),
    path('adminviewemployee',views.adminviewemployee),
    path('adminviewwork',views.adminviewwork),
    path('adminviewservices',views.adminviewservices),
    # path('adminaddservices',views.adminaddservices),
    path('adminaddemployee',views.adminaddemployee),
    path('adminviewcustomerreview',views.adminviewcustomerreview),
    path('employeeviewuser',views.employeeviewuser),
    path('employeevieworder',views.employeevieworder),
    path('user',views.user),
    path('userhome',views.userhome),
    path('userabout',views.userabout),
    path('userservices',views.userservices),
    path('usercontact',views.usercontact),
    path('indexbook',views.indexbook),
    path('dlogin',views.dlogin),
    path('d_reg',views.delboy_reg),
    path('reg',views.u_reg),
    path('log',views.login),
    path('add_services',views.addservices),
    path('edit/<int:id>',views.edit),
    path('updating/<int:id>',views.updating),
    path('delete/<int:id>',views.delete),
    path('feedback',views.user_feedback),
    path('fdelete/<int:id>',views.fdelete),
    path('userprofile',views.usr_profile),
# --------------- USER-PROFILE -----------------
#     path('my_profile',views.),
    path('userprofile/<int:id>', views.pro_edit, name='userprofile'),
    path('userprofile/<int:id>',views.update_profile),
    path('vedelete/<int:id>',views.vedelete),
#---------------booking------------------
    path('single_razor/<int:id>', views.single_razor, name='single_razor'),
    path('uservieworder',views.uservieworder),
    path('statusup/<wal>',views.statusup,name="statusup"),
    path('send_review_form/<int:id>/', views.send_review_form, name='send_review_form'),
    path('send_reviews/<int:id>', views.send_reviews, name='send_reviews'),

    path('show_review', views.show_reviews),
    # path('book/',views.book),
    path('book/<int:id>', views.book, name='book'),  # URL for displaying products
    # payment
    path('payment/<int:s_price>/<int:pk>/',views.payment),
    path('u_bookreq_cancel/<int:id>', views.u_bookreq_cancel),

#-------------forgot password----------------
    path('forgot', views.forgot_password, name="forgot"),
    path('reset/<token>', views.reset_password, name='reset_password'),
    # payment
    # path('payment/<int:price>',views.payment),
    path('u_show',views.u_booking),

    #

    path('razor',views.razor),
    path('razor_pay/<int:s_price>',views.razorpaycheck),
    path('success/<int:id>/', views.success, name='success'),
    path('bookingdetails',views.bookingdetails),
    path('adminpaymentdetails',views.adminpaymentdetails),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
