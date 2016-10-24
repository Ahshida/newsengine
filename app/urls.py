from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dashboard.views.render_dashboard', name='dashboard'),
    url(r'^dash', 'dashboard.views.render_dash'),
    url(r'^analysis/', 'dashboard.views.render_analysis'),
    url(r'^treemap/', 'dashboard.views.render_treemap'),
    url(r'^jsonFile/', 'dashboard.views.render_json'),
)

