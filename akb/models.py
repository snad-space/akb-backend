from django.db import models

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
	oid = models.BigIntegerField(unique = True, blank = False)
	description = models.TextField(blank = True)
	tags = models.ManyToManyField("Tag", related_name="tagged_objects")
	simbadid = models.CharField(max_length = 256, blank = True)

	class Meta:
		indexes = [
			models.Index(fields=['oid']),
		]
