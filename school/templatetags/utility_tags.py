# -*- coding: UTF-8 -*-
from django import template
from datetime import date, timedelta

register = template.Library()
### FILTERS ###
@register.filter(name='cut')
def cut(value, arg):
	return value.replace(arg, '')

@register.filter(name='calc_position')
def calc_position(score):
	maxscore = 0
	score = int(score)
	
	

	# maxscore = score
	# if score == score:
	#  	return "1st"
	# elif score < 100:
	# 	return "2nd"
	# # if score > maxscore:
	# 	maxscore = score
	# 	if score == maxscore:
	# 		return "1st"
	# 	# return maxscore


# @register.filter(name='get_due_date_string')
# def get_due_date_string(value):

# 	delta = value - date.today()

# 	if delta.days == 0:
# 		return "Today!"

# 	elif delta.days < 1:
# 		return "%s %s ago!" % (abs(delta.days),("day" if abs(delta.days) == 1 else "days"))

# 	elif delta.days == 1:
# 		return "Tomorrow"

# 	elif delta.days > 1:
# 		return "In %s days" % delta.days