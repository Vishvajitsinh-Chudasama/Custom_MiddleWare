from django.db import models

# Create your models here.
class Requestlog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.method} {self.path} [{self.status_code}]"
