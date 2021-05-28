from django.urls import path
from .views import HomeView, PageView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('page/<int:pk>', PageView.as_view(), name='page-detail'),
]
