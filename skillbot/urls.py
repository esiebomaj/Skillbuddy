from django.urls import path, include
from .views import BotView, debugview


urlpatterns = [
    path('bot', BotView.as_view(), name='bot'),
	# path('debug', debugview, name='debug'),

 
]
