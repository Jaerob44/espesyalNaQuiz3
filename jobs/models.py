from django.db import models
from accounts.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class JobOpening(models.Model):
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    min_offer = models.DecimalField(max_digits=10, decimal_places=2)
    max_offer = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    def clean(self):
        if self.min_offer > self.max_offer:
            raise ValidationError('min_offer cannot be greater than max_offer.')

    def __str__(self):
        return self.job_title

class JobApplicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(default=timezone.now)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return f'{self.user.username} applied for {self.job.job_title}'