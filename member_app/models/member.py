from django.db import models

# Create your models here.
class member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.id}, {self.first_name} {self.last_name}"
    class Meta:
        db_table='member'