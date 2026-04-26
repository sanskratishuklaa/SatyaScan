from django.db import models
from django.conf import settings


class ProfileScan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    risk_score = models.FloatField()
    is_fake = models.BooleanField()
    confidence=models.FloatField(default=0)
    reasons=models.TextField(blank=True)
    recommendation=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    


