from django.urls import path
from . import views # Import views from the current dir


# Create the list urlpatterns
urlpatterns = [
    path("", views.index, name="index")
]
