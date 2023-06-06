from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100, default=None,null=False)
    last_name = models.CharField(max_length=100, default=None, null=True)
    email = models.EmailField(_("email address"), unique=True)
    employee_code = models.IntegerField( null=False, primary_key=True)


    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_staff = True
        super().save(*args, **kwargs)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
  
#Model for discrepancy
class Discrepancy_Model(models.Model):

    DISCREPANCY_TYPE = [
        ('WFH','WFH'),
        ('Attendance','Attendance'),
        ('Overtime','Overtime'),
        ('Leave','Leave')
    ]

    MODE_OF_MARKING = [
    ('Biometric','Biometric'),
    ('Connecto','Connecto'),
    ('OneThing','OneThing')
    ]

    REPORTING_PERSON = [
        ('Sourabh Soni','Sourabh Soni'),
        ('Sunil More','Sunil More'),
        ('Santosh','Santosh')
    ]

    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    discrepancy_type = models.CharField(max_length=20, choices=DISCREPANCY_TYPE)
    mode_of_marking = models.CharField(max_length=15,choices=MODE_OF_MARKING)
    reason = models.TextField()
    Date = models.DateField()
    reporting_person = models.CharField(max_length=20, choices=REPORTING_PERSON)
    Reporting_person_remark = models.CharField(max_length=150)
    is_approved = models.BooleanField(default=False)


    def set_dates(self, dates):
        self.dates = ','.join(dates)

    def get_dates(self):
        return self.dates.split(',')

    def __str__(self):
        return f'{self.employee}-{self.discrepancy_type}-{self.is_approved}'


