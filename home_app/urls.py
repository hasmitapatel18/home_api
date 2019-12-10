
from django.urls import path
from . import views
from home_app.views import *



urlpatterns = [
    path('homes/', ListHomeView.as_view(), name='homes-all'),





]
