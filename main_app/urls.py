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
    path('stuff/<int:stuff_id>/add-walk/', views.add_walk, name='add-walk'),
    path('things/create/', views.ThingsCreate.as_view(), name='thing-create'),
    path('things/<int:pk>/', views.ThingsDetail.as_view(), name='thing-detail'),
    path('things/', views.ThingsList.as_view(), name='thing-index'),
]
