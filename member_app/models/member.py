from django.db import models

# Create your models here.
class member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    entity = models.ForeignKey('entity_app.entity', on_delete=models.SET_NULL, null=True, related_name='funds')

    dynamic_fields = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=250, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"{self.id}, {self.first_name} {self.last_name}"
    class Meta:
        db_table='member'