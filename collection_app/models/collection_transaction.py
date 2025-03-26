from django.db import models
import shortuuid

COLLECTION_TYPE_CHOICES = [
    ('tithes', 'Tithes'),
    ('mission', 'Mission'),
    ('partnership', 'Partnership'),
    ('offering', 'Offering'),
    ('normal', 'Normal'),
]

TRANSACTION_TYPE_CHOICES = [
    ('cash', 'Cash'),
    ('bank_transfer', 'Bank Transfer'),
    ('online', 'Online Payment'),
    ('other', 'Other'),
]

# Create your models here.
class collection_transaction(models.Model):
    member = models.ForeignKey('member_app.member', on_delete=models.SET_NULL, null=True, related_name='funds')
    collection = models.ForeignKey('collection_app.collection', on_delete=models.SET_NULL, null=True, related_name='ct_collection_id')
    collection_type = models.CharField(max_length=50, choices=COLLECTION_TYPE_CHOICES)
    collection_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=50, unique=True, editable=False)
    transaction_date = models.DateField()
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=250, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=250, null=True)

    def save(self, *args, **kwargs):
        if not self.transaction_id:  # Only generate if it's not set
            self.transaction_id = shortuuid.uuid()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Fund of {self.collection_amount} by {self.member.first_name} {self.member.last_name}"
    class Meta:
        db_table='collection_transaction'