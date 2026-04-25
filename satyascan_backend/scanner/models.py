from django.db import models
from users.models import User

class ProfileScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    risk_score = models.FloatField()
    is_fake = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)