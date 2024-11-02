from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HealthMetric(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(null=True, blank=True)
    blood_pressure = models.CharField(max_length=10, null=True, blank=True)
    activity_level = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date}"
