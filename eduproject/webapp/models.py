from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver

# Create your models here.


class employees(models.Model):
	# user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	first_name = models.CharField(max_length=10)
	last_name = models.CharField(max_length=10)
	emp_id = models.IntegerField()
	slug = models.SlugField(unique=True, blank=True)

	def __str__(self):
		return self.first_name

@receiver(models.signals.pre_save, sender=employees)
def set_slug(sender, instance, **c):
    if not instance.slug:
        instance.slug = slugify(instance.first_name)
