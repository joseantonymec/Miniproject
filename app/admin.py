from django.contrib import admin

from .models import UserTable

class UserTableDetails(admin.ModelAdmin):
	list_display=["__unicode__",'password']
	class Meta:
		model=UserTable

admin.site.register(UserTable,UserTableDetails)

