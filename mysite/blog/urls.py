from django.urls import path
from blog import views

urlpatterns = [
    path("", views.RootView.as_view(), name="root"),
    path("home/", views.PostView.as_view(), name="home"),
]
