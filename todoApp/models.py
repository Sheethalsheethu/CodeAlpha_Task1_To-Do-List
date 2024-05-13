from django.db import models

class todo(models.Model):  # Renamed to follow PEP 8 conventions
    task = models.CharField(max_length=500, default='Your default value here')
