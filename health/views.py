# from django.views import View
# from django.shortcuts import render

# class HealthTipsView(View):
#     def get(self, request):
#         return render(request, 'health/tips.html')  # Adjust the template path as needed

# class HealthArticlesView(View):
#     def get(self, request):
#         return render(request, 'health/articles.html')  # Adjust the template path as needed

# def add_health_metric(request):
#     # Your logic for adding a health metric
#     return render(request, 'health/add_health_metric.html')

# def schedule_appointment(request):
#     # Your logic for scheduling an appointment
#     return render(request, 'health/schedule_appointment.html')

# def recommendations(request):
#     # Your logic for health recommendations
#     return render(request, 'health/recommendations.html')

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from .models import HealthMetric
from .ml_models import predict_health_trend, detect_anomalies, get_personalized_recommendations

class HealthTipsView(View):
    def get(self, request):
        return render(request, 'health/tips.html')

class HealthArticlesView(View):
    def get(self, request):
        return render(request, 'health/articles.html')

def add_health_metric(request):
    if request.method == "POST":
        # Logic to handle adding health metric
        return JsonResponse({"message": "Health metric added successfully."})
    return render(request, 'health/add_health_metric.html')

def schedule_appointment(request):
    if request.method == "POST":
        # Logic for scheduling an appointment
        return JsonResponse({"message": "Appointment scheduled successfully."})
    return render(request, 'health/schedule_appointment.html')

def recommendations(request):
    if request.method == "GET":
        # Fetch user health data
        user_health_data = HealthMetric.objects.all().values()
        
        # Predict health trends
        trend_predictions = predict_health_trend(user_health_data)
        
        # Detect anomalies in health metrics
        anomalies = detect_anomalies(user_health_data)
        
        # Get personalized recommendations
        personalized_recs = get_personalized_recommendations(user_health_data)
        
        response_data = {
            "trend_predictions": trend_predictions,
            "anomalies": anomalies,
            "personalized_recommendations": personalized_recs
        }
        return JsonResponse(response_data)
    return render(request, 'health/recommendations.html')