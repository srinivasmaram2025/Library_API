from django.urls import path

from .views import BooklistView

urlpatterns = [
    path('', BooklistView.as_view(), name='home')
]
