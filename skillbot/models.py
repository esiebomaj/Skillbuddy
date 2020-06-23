from django.db import models
from datetime import datetime, timedelta
from dateutil.rrule import rrule, MONTHLY,DAILY, WEEKLY


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
	created = models.DateTimeField( auto_now_add=True)


	def get_notify_times(self):
		frequency=self.frequency
		day_period=self.time_of_reminder
		# converted to unaware datetime
		start_date = self.created.replace(tzinfo=None)
		
		start_midnight=start_date-timedelta(hours=start_date.hour,
	                                    minutes=start_date.minute, 
	                                    seconds=start_date.second, 
	                                    microseconds=start_date.microsecond)
		if frequency=='daily':
			if day_period=='morning':
				morning_start_time=start_midnight+timedelta(hours=6)
				reminder_list=list(rrule(freq=DAILY, count=30, dtstart=morning_start_time))
			elif day_period=='afternoon':
				afternoon_start_time=start_midnight+timedelta(hours=12)
				reminder_list=list(rrule(freq=DAILY, count=30, dtstart=afternoon_start_time))
			elif day_period=='evening':
				evening_start_time=start_midnight+timedelta(hours=18)
				reminder_list=list(rrule(freq=DAILY, count=30, dtstart=evening_start_time))
			else:
				reminder_list=[]

		elif frequency=='weekly':
			if day_period=='morning':
				morning_start_time=start_midnight+timedelta(hours=6)
				reminder_list=list(rrule(freq=WEEKLY, count=4, dtstart=morning_start_time))
			elif day_period=='afternoon':
				afternoon_start_time=start_midnight+timedelta(hours=12)
				reminder_list=list(rrule(freq=WEEKLY, count=4, dtstart=afternoon_start_time))
			elif day_period=='evening':
				evening_start_time=start_midnight+timedelta(hours=18)
				reminder_list=list(rrule(freq=WEEKLY, count=4, dtstart=evening_start_time))
			else:
				reminder_list=[]

		else:
			reminder_list=[]

		return reminder_list













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