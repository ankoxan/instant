from django.db import models

# Create your models here.

class Share(models.Model):
	name_share 				= models.CharField(max_length=30, null=False, blank=True)
	descript	 			= models.CharField(max_length=30, null=False, blank=True)
	country		 			= models.CharField(max_length=30, null=False, blank=True)
	industry	 			= models.CharField(max_length=30, null=False, blank=True)
	date_of_organization 	= models.CharField(max_length=30, null=False, blank=True)
	basic_information	 	= models.TextField(max_length=1000, null=False, blank=True)
	market_share		 	= models.TextField(max_length=1000, null=False, blank=True)
	leadership			 	= models.TextField(max_length=1000, null=False, blank=True)
	benefits			 	= models.TextField(max_length=1000, null=False, blank=True)
	capitalization 			= models.CharField(max_length=30, null=False, blank=True)
	dividends_profit		= models.CharField(max_length=30, null=False, blank=True)
	dividends_real			= models.CharField(max_length=30, null=False, blank=True)
	dividends_prognosis		= models.CharField(max_length=30, null=False, blank=True)
	dividends_date			= models.CharField(max_length=30, null=False, blank=True)
	real_price				= models.CharField(max_length=30, null=False, blank=True)
	target_price_short		= models.CharField(max_length=30, null=False, blank=True)
	target_price_medium		= models.CharField(max_length=30, null=False, blank=True)
	target_price_long		= models.CharField(max_length=30, null=False, blank=True)
	potential				= models.CharField(max_length=30, null=False, blank=True)
	price_change_day		= models.CharField(max_length=30, null=False, blank=True)
	price_change_quarter	= models.CharField(max_length=30, null=False, blank=True)
	price_change_january	= models.CharField(max_length=30, null=False, blank=True)
	price_change_2017		= models.CharField(max_length=30, null=False, blank=True)
	price_change_3years		= models.CharField(max_length=30, null=False, blank=True)
	price_change_10years	= models.CharField(max_length=30, null=False, blank=True)
	trading_volume_day		= models.CharField(max_length=30, null=False, blank=True)
	trading_volume_quarter	= models.CharField(max_length=30, null=False, blank=True)
	trading_volume_january	= models.CharField(max_length=30, null=False, blank=True)
	img_logo				= models.FileField(upload_to='static/media', null=False, blank=True)
	img_fon					= models.CharField(max_length=30, null=False, blank=True)
	category				= models.CharField(max_length=30, null=False, blank=True)
	def __str__(self):
		return(self.name_share)

