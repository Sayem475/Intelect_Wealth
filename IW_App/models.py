from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
# from ckeditor.fields import RichTextField

# Create your models here.



class TeamMember(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, null=True)
	image = models.ImageField(null=True, blank=True)
	designation = models.CharField(max_length=120, null=True, blank=True)
	team_desc = models.TextField(blank=True)

	def __str__(self):
		return self.name

	def image_tag(self):
		if self.image.url is not None:
			return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
		else:
			return ""
	def get_absolute_url(self):
		return reverse('SearchResult', args=[self.id, self.slug])

class IWLicense(models.Model):
	license_name = models.CharField(max_length=200)
	license_desc = models.TextField()

	def __str__(self):
		return self.license_name

class IWAdvisor(models.Model):
	advisor_title = models.CharField(max_length=200)
	advisor_desc = models.TextField()

	def __str__(self):
		return self.advisor_title

class OurOffers(models.Model):
	offer_title = models.CharField(max_length=200)
	offer_desc = models.TextField()

	def __str__(self):
		return self.offer_title

class BusinessAdvise(models.Model):
	ba_title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, null=True)
	shortDesc = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.ba_title

	class Meta:
		ordering=('ba_title',)
		index_together=(('id', 'slug'),)

	def get_absolute_url(self):
		return reverse('advise_detail', args=[self.id, self.slug])

class ClientEducation(models.Model):
	ce_title = models.CharField(max_length=200)
	# file = models.FileField(upload_to ='files/', blank=True, null=True)

	def __str__(self):
		return self.ce_title

class ClintFile(models.Model):
	clint = models.ForeignKey(ClientEducation, on_delete=models.CASCADE, blank=True, null=True)
	file = models.FileField( blank=True, null=True)

class Contact(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	email = models.EmailField(max_length=250)
	phone = models.CharField(max_length=20)
	message = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.first_name

class Security(models.Model):
	security_title = models.CharField(max_length=250)
	security_desc = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.security_title

class TermsOfUse(models.Model):
	term_title = models.CharField(max_length=200)
	term_desc = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.term_title

class Limitation(models.Model):
	description = models.TextField()


 



