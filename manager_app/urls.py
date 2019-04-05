from django.conf.urls import url
from manager_app import views
app_name='manager_app'

urlpatterns=[
    url(r'^$', views.index, name="index"),
url(r'^manager/$',views.manager,name="manager"),
url(r'^createdepartment/$',views.createdepartment,name="createdepartment"),
]