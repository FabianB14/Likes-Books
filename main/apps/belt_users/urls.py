from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^create_user$', views.create_user),
    url(r'^LogReg$',views.LogReg),                               
    url(r'^profile$',views.profile),
    url(r'^login$',views.login),
    url(r'^showLogin$',views.showLogin),
    url(r'^logOut$',views.logOut),

]                            