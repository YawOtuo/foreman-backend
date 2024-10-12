from django.db import models

class Constituency(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=255)
    constituency = models.ForeignKey(Constituency, related_name='areas', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.constituency.name})"