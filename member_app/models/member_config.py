from django.db import models

# Create your models here.
class member_config(models.Model):
    dynamic_input = models.JSONField()

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.created_on} - {self.created_by}"
    class Meta:
        db_table='member_config'