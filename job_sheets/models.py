from django.db import models

class JobSheet(models.Model):
    client_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=15)
    received_date = models.DateField()
    inventory_received = models.TextField()
    upload = models.FileField(upload_to='uploads/', null=True, blank=True)
    reported_issues = models.TextField()
    client_notes = models.TextField()
    assigned_technician = models.CharField(max_length=255)
    estimated_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed')
    ])

    def __str__(self):
        return f"{self.client_name} - {self.received_date}"
