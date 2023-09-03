from django.contrib import admin

# Register your models here.
from phones import models

@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price','image','release_date','lte_exists','slug')
admin.site.unregister(models.Phone)
admin.site.register(models.Phone, PhoneAdmin)