from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
import app.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MBBS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}), 
    (r'^login/$', views.Login ),
    (r'^acc_login/$', views.acc_login),
    (r'^logout/$', views.logout_view),    
    url(r'', include(app.urls)),
)
