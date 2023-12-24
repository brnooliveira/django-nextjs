from datetime import *

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Intership = 'Intership'


class Education(models.TextChoices):
    Bachelor = 'Bachelor'
    Master = 'Master'
    Phd = 'Phd'


class Industry(models.TextChoices):
    Business = 'Business'
    IT = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education'
    Telecomunication = 'Telecomunication'
    Others = 'Others'


class Experience(models.TextChoices):
    NO_EXPERIENCE = 'No experience'
    ONE_YEAR = '1 Year'
    TWO_YEAR = '2 years'
    THREE_YEAR_PLUS = '3 years above'


def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)


class Job(models.Model):
    title = models.CharField(
        max_length=200,
        null=True
    )
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(
        max_length=100,
        null=True
    )
    job_type = models.CharField(
        max_length=20,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education = models.CharField(
        max_length=20,
        choices=Education.choices,
        default=Education.Bachelor
    )
    industry = models.CharField(
        max_length=30,
        choices=Industry.choices,
        default=Industry.Business
    )
    experience = models.CharField(
        max_length=20,
        choices=Experience.choices,
        default=Experience.NO_EXPERIENCE
    )
    salary = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(1000000)
        ]
    )
    positions = models.IntegerField(default=1)
    company = models.CharField(
        max_length=100,
        null=True
    )
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(
        User,
        related_name='jobs',
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
