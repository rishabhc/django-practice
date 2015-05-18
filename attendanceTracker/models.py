from django.db import models
from django.forms import ModelForm
from django.db.models import ForeignKey


# Create your models here.
class Subject(models.Model):
	subject_name = models.CharField(max_length=50)
	classes_held = models.IntegerField(default=0)
	classes_attended = models.IntegerField(default=0)
	percentage_attendance = models.FloatField(default=0)

	def calculate_attendance(self):
		if self.classes_held == 0:
			self.percentage_attendance = 0
			return
		self.percentage_attendance = self.classes_attended/self.classes_held * 100

	def is_attendance_not_low(self):
		return self.percentage_attendance >= 75.0

	def __str__(self):
		return self.subject_name + " " +`self.classes_held` +" "+ `self.classes_attended`

	is_attendance_not_low.boolean = True

class TimeTable(models.Model):
	day = models.CharField(max_length=8)
	subject_id_8_to_9 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_8_to_9')
	subject_id_9_to_10 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_9_to_10')
	subject_id_10_to_11 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_10_to_11')
	subject_id_11_to_12 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_11_to_12')
	subject_id_12_to_1 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_12_to_11')
	subject_id_2_to_3 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_2_to_3')
	subject_id_3_to_4 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_3_to_4')
	subject_id_4_to_5 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_4_to_5')
	subject_id_5_to_6 = models.ForeignKey(Subject,null='True',blank=True,related_name='subject_id_5_to_6')

	def __str__(self):
		return self.day

	