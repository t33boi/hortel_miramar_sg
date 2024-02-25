from django.contrib import admin
from .models import Person, Room, BookRoom
# Register your models here.

admin.site.register(Person)
admin.site.register(Room)
admin.site.register(BookRoom)