from django.conf.urls import url

from My_project import settings
from main import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

     url('signup/', views.signup),
     url('signup_B/', views.signup_B),
     url('dashboard/', views.dashboard),
     url('login/', views.login),
     url('debit/',views.debit),
     url('credit/',views.credit),
     url('acc_state/',views.acc_state),
     url('transfer/',views.transfer),
     url('login_B/',views.login_B),
     url('dashboard_B/',views.dashboard_B),
     url('', views.Homepageview),
     ]
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)