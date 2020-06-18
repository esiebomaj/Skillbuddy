from django.db import models

# Create your models here.
class our_user(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	fbid=models.CharField(max_length=255)
	profile_pics=models.CharField(max_length=255)
	skill=models.CharField(max_length=255)
	Duration=models.CharField(max_length=255)
	frequency=models.CharField(max_length=255)
	time_of_reminder=models.CharField(max_length=255)













# Rough drafting of the model representation

# model fields 
# 1.	name
# 2.	surname
# 3.	fbid
# 4.	skill
# 5.	profile pics
# 6.	Duration
# 7.	frequency
# 6.	time of reminder