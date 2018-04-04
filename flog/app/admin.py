from django.contrib import admin
from .models import BigCategory,Category,Specify
# Register your models here.
admin.site.register(Category)
admin.site.register(BigCategory)
admin.site.register(Specify)