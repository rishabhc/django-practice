from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.db.models import ForeignKey
import collections
import datetime

from .models import Subject, TimeTable
# Create your views here.
def calculateAttendance(request):
	for x in range(1,9):
		if x == 1:
			y = '1'
		elif x == 2:
			y = '2'
		elif x == 3:
			y = '3'
		elif x == 4:
			y = '4'
		elif x == 5:
			y = '5'
		elif x == 6:
			y = '6'
		elif x == 7:
			y = '7'
		elif x == 8:
			y = '8'
		sub = request.GET.get(y,False)
		obj = Subject.objects.get(pk=x)
		if sub == "Did not attend":
			obj.classes_held += 1
		elif sub == "Attended":
			obj.classes_held += 1
			obj.classes_attended += 1
		obj.calculate_attendance()
		obj.save()
	return render(request, 'attendanceTracker/debug.html',{'sub1':"Thank you!",'sub2':obj,'sub3':sub})

def enterAttendance(request):
	#now = datetime.datenow.now()
	day_today = datetime.date.today().strftime("%A")
	p = get_object_or_404(TimeTable,day=day_today)
	timetable = {}
	for x in p._meta.get_all_field_names():
		timetable[x] = getattr(p, x)
	timetable = collections.OrderedDict(sorted(timetable.items()))
	lol = 'k'
	i = 0
	j = 0
	new_table = {}
	for key,value in timetable.items():
		i = i + 1
		if i % 2 == 0:
			new_table[j].append(key)
			new_table[j].append(value)
			j = j + 1	
			continue
		new_table[j] = [key,value] 
	return render(request,'attendanceTracker/enter.html',{
		'timetable': new_table
		})