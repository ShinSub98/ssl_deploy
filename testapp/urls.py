from django.urls import path
from .views import *

app_name = 'test'

urlpatterns = [
    path('create/', TestCreate.as_view()),
    path('get/<int:test_id>/', GetTest.as_view()),
]