from django.urls import path
from . import views

urlpatterns = [
    path('<str:code>/', views.get_policyholder),
    path('<str:code>/top/', views.get_policyholder_top_list),
]