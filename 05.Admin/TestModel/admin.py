from django.contrib import admin
from TestModel.models import Test,Contact,Tag

class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
