from django.db import models
import uuid

# Create your models here.
class Appointment(models.Model):
    
    GENERAL_CHECK_UP = 'general_check-up'
    TEETH_CLEANING = 'teeth_cleaning'
    TEETH_WHITENING = 'teeth_whitening'
    DENTAL_IMPLANTS = 'dental_implants'
    OTHER = 'other' 
    
    SERVICETYPE_CHOICES = [
        ('GENERAL_CHECK-UP', 'General Check-Up'),
        ('TEETH_CLEANING', 'Teeth Cleaning'),
        ('TEETH_WHITENING', 'Teeth Whitening'),
        ('DENTAL_IMPLANTS', 'Dental Implants'),
        ('ROOT_CANAL', 'Root Canal'),
        ('OTHER', 'Other'),
    ]
      
    aid = models.UUIDField(primary_key=True, max_length=10, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=70, blank=False, null=False)
    firstname = models.CharField(max_length=70,blank=False, null=False)
    lastname = models.CharField(max_length=70, blank=False, null=False)
    phonenumber = models.CharField(max_length=20, blank=False, null=False)
    preferred_date = models.DateField(blank=False, null=False)
    preferred_time = models.TimeField(blank=False, null=False)
    service_type = models.CharField(max_length=50, choices=SERVICETYPE_CHOICES, default=GENERAL_CHECK_UP, blank=False, null=False,)
    additonal_note = models.TextField()