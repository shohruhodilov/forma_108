from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Qurilish(models.Model):
    q_type = models.CharField(max_length=100)
    servise_name = models.CharField(max_length=100)
    servise_code = models.CharField(max_length=5)
    soato = models.CharField(max_length=6)
    report_month = models.CharField(max_length=6)
    report_year = models.CharField(max_length=6)
    last_year = models.CharField(max_length=6)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.q_type

    def get_absolute(self):
        return reverse('hi', kwargs={'pk':self.pk})



