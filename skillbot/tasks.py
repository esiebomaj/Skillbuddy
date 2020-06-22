import logging
from skillbot.models  import our_user
from django.core.mail import send_mail
from skillbuddy.celery import app
from datetime import datetime, timedelta
from skillbot.views import post_facebook_message

 
 
@app.task
def reminder():
	present_date_time=datetime.now()
	present_date_time_hours=present_date_time-timedelta(
		minutes=present_date_time.minute, 
		seconds=present_date_time.second, 
		microseconds=present_date_time.microsecond)
	
	all_users=our_user.objects.all()
	for user in all_users:
		notify_times=user.get_notify_times()
		print(present_date_time_hours)
		print(notify_times)
		if present_date_time_hours in notify_times:
			print('Yass!! go ahead and send notificatons')
			send_notification(user)
		else:
			print('no date_time matches')
    
    

def send_notification(user):
	name=user.first_name
	skill=user.skill
	fbid=user.fbid
	message_to_be_sent='Hello {} have you completed your {} target for today?'.format(name, skill)
	print(message_to_be_sent)
	post_facebook_message(fbid, message_to_be_sent)


