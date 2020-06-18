from django.urls import path, include
from .views import BotView


urlpatterns = [
    path('bot', BotView.as_view(), name='bot'),
 
]
