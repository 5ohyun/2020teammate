from django.contrib import admin
from .models import Customer,Domain,Score,Role,Message

# Register your models here.
admin.site.register(Customer)
admin.site.register(Domain)
admin.site.register(Score)
admin.site.register(Role)
admin.site.register(Message)
