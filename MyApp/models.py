from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	user = models.CharField('user name', max_length=20, unique=True)
	pwd = models.CharField('password', max_length=20)
	first_name = models.CharField('first name', max_length=20, unique=True)
	last_name = models.CharField('last name', max_length=20, unique=True)
	age = models.IntegerField()
	email_id = models.EmailField('email ID', unique=True)
	dob = models.DateField('date of birth')
	date_created = models.DateTimeField(auto_now=True)
	# last_used = models.DateTimeField(auto_now=True)
	phone = models.CharField('phone no.',max_length=10, unique=True)
	address = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural='Person Info'

	def __unicode__(self):
		return unicode(self.first_name + self.last_name)


class DealersInfo(models.Model):
	person_info = models.ForeignKey(Person) 
	company_name = models.CharField(max_length=50)
	dl1 = models.CharField('dealer 1',max_length=15, unique=True)
	dl2 = models.CharField('dealer 2', max_length=15, unique=True)
	tin = models.CharField('tin number',max_length=15, unique=True)

	class Meta:
		verbose_name_plural='Dealers Info'

	def __unicode__(self):
		return unicode(self.person_info.first_name + self.person_info.last_name)


class ComplteStockDetails(models.Model):
    batch_num = models.IntegerField('batch No.', unique=True)
    item_name = models.CharField('item name', max_length=50, unique=True)
    company = models.CharField(max_length=30)
    price_per_unit = models.FloatField('price per unit')
    manf_date = models.CharField('manufacturing date', max_length=10)
    exp_date = models.CharField('expiry date', max_length=10)
    quantity = models.IntegerField()
    dealer = models.ForeignKey(DealersInfo)
    comments = models.CharField(max_length=100)

    class Meta:
		verbose_name_plural='Stock Info'

    def __unicode__(self):
	# changed return statement.
        return unicode(self.company)
