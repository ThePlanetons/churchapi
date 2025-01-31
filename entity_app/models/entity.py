from django.db import models

# Create your models here.
class entity(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=250)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.id}, {self.code} - {self.name}"
    class Meta:
        db_table='entity'