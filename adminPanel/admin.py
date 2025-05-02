from django.contrib import admin
from .models import Internship, Development, Newsletter

@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phoneno', 'institute', 'course', 'areaofinterest', 'hours', 'request_date')
    search_fields = ('name', 'email', 'phoneno', 'institute', 'course', 'areaofinterest')
    list_filter = ('course', 'areaofinterest', 'request_date')
    ordering = ('-request_date',)
    date_hierarchy = 'request_date'

@admin.register(Development)
class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'phoneno', 'compinst', 'department', 'request_date')
    search_fields = ('fname', 'lname', 'email', 'phoneno', 'compinst', 'department')
    list_filter = ('department', 'request_date')
    ordering = ('-request_date',)
    date_hierarchy = 'request_date'

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email_sub',)
    search_fields = ('email_sub',)
    list_filter = ('email_sub',)
    ordering = ('-id',)