from django import forms
from .models import HealthMetric, Appointment

class HealthMetricForm(forms.ModelForm):
    class Meta:
        model = HealthMetric
        fields = ['weight', 'blood_pressure', 'activity_level']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'reason']
