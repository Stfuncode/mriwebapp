from django.urls import path
from .views import upload_images, predict
urlpatterns = [
    path('', upload_images, name='upload_images'),
    path('predict/', predict, name='predict'),
]
