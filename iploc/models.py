from django.db import models

class IP(models.Model):
    """ Requisitar IPs """
    ip = models.CharField(max_length=15)

    def __str__(self):
        return self.ip