from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.SlugField(max_length=256, blank = False, unique = True)
	priority = models.IntegerField(unique = False, blank = False)
	description = models.TextField(blank = True)

	class Meta:
		indexes = [
			models.Index(fields=['name']),
			models.Index(fields=['priority']),
		]
		ordering = ['priority']

class Object(models.Model):
	oid = models.BigIntegerField(primary_key = True, blank = False)
	description = models.TextField(blank = True)
	tags = models.ManyToManyField("Tag", related_name="tagged_objects")
	simbadid = models.CharField(max_length = 256, blank = True)
	changed_at = models.DateTimeField(auto_now = True)
	changed_by = models.ForeignKey(User, on_delete=models.PROTECT, blank = False)
