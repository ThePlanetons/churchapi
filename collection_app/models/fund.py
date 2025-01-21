from django.db import models
from django.utils.timezone import now
PAYMENT_METHOD_CHOICES = [
    ('cash', 'Cash'),
    ('bank_transfer', 'Bank Transfer'),
    ('online', 'Online Payment'),
    ('other', 'Other'),
]

# Create your models here.
class fund(models.Model):
    member = models.ForeignKey("member_app.member", on_delete=models.SET_NULL, null=True, related_name='funds')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default='cash')
    date_of_contribution = models.DateTimeField(auto_now_add=True)
    purpose = models.CharField(max_length=100, blank=True, null=True)
    # transaction_id = models.CharField(max_length=100, blank=True, null=True) 

    # created_by = models.CharField(max_length=220)
    # created_at = models.DateTimeField(default=now, editable=False)
    # updated_by = models.CharField(max_length=220, null=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Fund of {self.amount} by {self.member.first_name} {self.member.last_name}"
    class Meta:
        db_table='fund'

# from django.db import models
# from django.utils.timezone import now

# # Create your models here.
# class member(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True)
#     date_of_birth = models.DateField()
#     phone = models.CharField(max_length=20)
#     gender = models.CharField(max_length=20)

#     # street_address = models.CharField(max_length=255)
#     # city = models.CharField(max_length=100)
#     # state = models.CharField(max_length=100)
#     # postal_code = models.CharField(max_length=20)
#     # country = models.CharField(max_length=100, default="")

#     # created_by = models.CharField(max_length=220)
#     # created_at = models.DateTimeField(default=now, editable=False)
#     # updated_by = models.CharField(max_length=220, null=True)
#     # updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.id}, {self.first_name} {self.last_name}"
#     class Meta:
#         db_table='member'