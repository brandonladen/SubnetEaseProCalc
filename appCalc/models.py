from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SubnettingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ipaddress = models.CharField(max_length=100)
    subnetmask = models.CharField(max_length=100)
    wildcardmask = models.CharField(max_length=100)
    networkbits = models.IntegerField()
    networkadddress = models.CharField(max_length=100)
    first_ip = models.CharField(max_length=100)
    last_ip = models.CharField(max_length=100)
    broadcast_address = models.CharField(max_length=100)
    timecreated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.ipaddress