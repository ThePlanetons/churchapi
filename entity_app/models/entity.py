from django.db import models

# Create your models here.
class entity(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    primary_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=510)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=250, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.id}, {self.code} - {self.name}"
    class Meta:
        db_table='entity'