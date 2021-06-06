from django.contrib import admin
from .models import Order, OrderFile

class OrderFileInline(admin.StackedInline):
	model = OrderFile
	extra = 0

class OrderAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'deadline', 'created_on']
	inlines = [OrderFileInline, ]

admin.site.register(Order, OrderAdmin)

admin.site.site_header = 'Assessment'
admin.site.site_title = 'Assessment'