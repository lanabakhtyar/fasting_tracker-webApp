# tracker/models.py

from django.db import models
from django.contrib.auth.models import User

class FastingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.start_time} to {self.end_time}"

    def get_fasting_duration(self):
        if self.end_time:
            duration = self.end_time - self.start_time
            return duration.total_seconds() / 60 # Convert to hours
        return None
