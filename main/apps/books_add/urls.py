from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^/add_books$', views.add_books),
    url(r'^/show_add_books$', views.show_add_books),
]