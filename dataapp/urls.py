from django.urls import path
from . import views
urlpatterns = [
path('', views.homepageview, name='homepage'),
#path('choose-file', views.choosefile_view, name='choose-file'),
path('upload-file', views.getfile_view, name='upload-file'),
]