from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stuff/', views.stuff_index, name='stuff-index'),
    path('stuff/<int:stuff_id>/', views.stuff_detail, name='stuff-detail'),
    path('stuff/create/', views.StuffCreate.as_view(), name='stuff-create'),
    path('stuff/<int:pk>/update/', views.StuffUpdate.as_view(), name='stuff-update'),
    path('stuff/<int:pk>/delete/', views.StuffDelete.as_view(), name='stuff-delete'),
]
