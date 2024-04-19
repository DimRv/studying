from . import views
from django.urls import path

app_name = "builtin_functions"
urlpatterns = [
    path('', views.index, name='functions'),
    path('/<str:func_name>', views.detail, name='detail')
]