from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class person(models.Model):
	name = models.CharField(max_length=250)
	area = models.CharField(max_length=250)
	specialization = models.CharField(max_length=250)
	details = models.TextField()
	image = models.ImageField(upload_to='lawyered/media/',blank=True)
	def __str__(self):
		return self.title	
	

class divorceForm(models.Model):
	ASSETS = (
    ('residential_property', 'Residential Property'),
    ('investment_property', 'Investmant Property'),
    ('investment_account', ' Investment Account(s) (stocks, bonds, mutual funds, etc.) '),
    ('bank_account','Bank Account(s)'),
    ('pension', 'pension, or other retirement plan'),
    ('business','Business interest(s)'),
    ('personal_property','Personal property (jewelry, cars, furniture, appliances, etc.) '),
    ('others','Others'),
    )
	CHOICES1 = (('1', 'Yes',), ('2', 'No',),('3','Not Sure',))
	CHOICES2 = (('1', 'Male',), ('2', 'Female',))
	CHOICES3 = (('1', 'Yes',), ('2', 'No',))

	name = models.ForeignKey(User)
	spouse = models.CharField('What is your Spouse\'s name?', max_length = 25)
	date_of_marriage = models.DateField( 'What was your Date of Marriage?',default=datetime.date.today)
	gender = models.CharField(max_length=1)
	mutual = models.CharField(max_length=1)
	assets = models.CharField(max_length=5)
	assets_before = models.CharField(max_length=5)
	children = models.CharField(max_length=1)
	custody = models.CharField(max_length=1)
	budget = models.CharField(max_length=250)
	details = models.CharField(max_length=250)
