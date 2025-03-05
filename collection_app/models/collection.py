from django.db import models

# Create your models here.
class collection(models.Model):
    first_approver = models.ForeignKey('member_app.member', on_delete=models.SET_NULL, null=True, related_name='first_approver_1')
    second_approver = models.ForeignKey('member_app.member', on_delete=models.SET_NULL, null=True, related_name='second_approver_2')
    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=250, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f"Fund of by {self.first_approver.first_name} {self.first_approver.last_name}"
    class Meta:
        db_table='collection'