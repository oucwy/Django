from django.contrib import admin

from .models import Student

# Register your models here.
# markwy
# 2021.6/4

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'phone', 'status', 'create_time')
    list_filter = ('gender', 'status', 'create_time')
    search_fields = ('name', 'phone')
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'gender',
                'phone',
                'status',
            )
        }),
    )

admin.site.register(Student, StudentAdmin)