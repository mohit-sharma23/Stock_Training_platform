from django.contrib import admin

# Register your models here.
from .models import Room, Join, Stock, Buy,Ratings


# Register your models here.
admin.site.register(Room)
admin.site.register(Join)
admin.site.register(Stock)
admin.site.register(Buy)
admin.site.register(Ratings)

