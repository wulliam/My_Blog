from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from css3two_blog import views
from my_blog import views as my_blog_views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # css3two_blog
    url(r'^(?P<page>\d*)/$', views.home),
    url(r'^$', views.home),
    url(r'^blog/', include('css3two_blog.urls')),

    # admin
    url(r'^referral/', my_blog_views.referral)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'my_blog.views.handler404'
