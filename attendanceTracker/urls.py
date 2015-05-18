from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.enterAttendance,name='enterAttendance'),
	url(r'^calculateAttendance',views.calculateAttendance,name='calculateAttendance'),
]
