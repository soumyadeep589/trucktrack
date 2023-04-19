from django.db import models


class Location(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    long = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "location"
        verbose_name_plural = "locations"
        ordering = ["id"]

    def __str__(self):
        return f"{self.id}, lat: {self.lat}, long: {self.long}"