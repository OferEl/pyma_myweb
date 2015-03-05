from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import main_page


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyma_myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
       (r"^main/$", main_page.as_view()),
       
       
       
)
