from django.views import View
from django.shortcuts import render

class HealthTipsView(View):
    def get(self, request):
        return render(request, 'health/tips.html')  # Adjust the template path as needed

class HealthArticlesView(View):
    def get(self, request):
        return render(request, 'health/articles.html')  # Adjust the template path as needed

def add_health_metric(request):
    # Your logic for adding a health metric
    return render(request, 'health/add_health_metric.html')

def schedule_appointment(request):
    # Your logic for scheduling an appointment
    return render(request, 'health/schedule_appointment.html')

def recommendations(request):
    # Your logic for health recommendations
    return render(request, 'health/recommendations.html')
