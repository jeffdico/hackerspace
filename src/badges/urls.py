from django.urls import path

from badges import views

from django.conf.urls import url

app_name = 'badges'

urlpatterns = [
    path('', views.badge_list, name='list'),
    path('create/', views.badge_create, name='badge_create'),
    path('<int:badge_id>', views.detail, name='badge_detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.BadgeUpdate.as_view(), name='badge_update'),
    url(r'^(?P<badge_id>[0-9]+)/copy/$', views.badge_copy, name='badge_copy'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.BadgeDelete.as_view(), name='badge_delete'),
    # url(r'^(?P<badge_id>[0-9]+)/grant/(?P<user_id>[0-9]+)/$', views.grant, name='grant'),
    url(r'^(?P<badge_id>[0-9]+)/grant/(?P<user_id>[0-9]+)/$', views.assertion_create, name='grant'),
    url(r'^(?P<badge_id>[0-9]+)/grant/bulk/$', views.bulk_assertion_create, name='bulk_grant_badge'),
    path('grant/bulk/', views.bulk_assertion_create, name='bulk_grant'),
    url(r'^assertion/(?P<assertion_id>[0-9]+)/revoke/$', views.assertion_delete, name='revoke'),
]
