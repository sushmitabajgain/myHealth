from django.urls import path
from .views import HealthTipsView, HealthArticlesView, add_health_metric, schedule_appointment, recommendations  

urlpatterns = [
    path('', HealthTipsView.as_view(), name='health_tips'),
    path('articles/', HealthArticlesView.as_view(), name='health_articles'),
    path('add-metric/', add_health_metric, name='add_health_metric'),
    path('schedule-appointment/', schedule_appointment, name='schedule_appointment'),
    path('recommendations/', recommendations, name='recommendations'),
]
