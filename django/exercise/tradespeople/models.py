from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)


class Tradesperson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="tradespeople",
    )

    @property
    def full_name(self):
        pass
