from django.urls import path
from . import views

urlpatterns = [
    path("verify", views.verify, name="verify"),
    path("protected", views.protected_resources, name="protected"),
]
