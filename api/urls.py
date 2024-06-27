from django.urls import path

from api import views

urlpatterns = [
    path('', views.IndexAPIView.as_view(), name='announcements_index'),
    path('<int:id>/', views.AnnouncementAPIView.as_view(), name='announcements_detail'),
]
