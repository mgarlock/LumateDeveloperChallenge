from django.conf.urls import patterns, include, url
from django.contrib import admin
from guestBook.views import GuestList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'guestBook.views.create'),
    url(r'^log/', GuestList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
