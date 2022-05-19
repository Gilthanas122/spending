from django.db import models

class Spending(models.Model):
    description = models.CharField(min_length=5, max_length=100)
    amount = models.PositiveIntegerField(default=10)
    spent_at = models.DateTimeField(auto_now=True)
    currency = models.CharField(min_length=2, max_length=10)



