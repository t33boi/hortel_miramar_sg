import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.


class Person(AbstractUser):
    phoneNumber = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    # USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'hms_main_person'

    groups = models.ManyToManyField(Group, related_name='person_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='person_user_permissions')


class Room(models.Model):

    ROOM_TYPES = [
        ('single', 'Single Room'),
        ('double', 'Double Room'),
        ('suite', 'Suite Room'),
        ('delux', 'Delux Room'),
    ]

    room_type = models.CharField(
        max_length=10, choices=ROOM_TYPES, help_text='Select the type of room.')
    description = models.TextField(
        help_text='Provide a description of the room.')
    # amenities = models.TextField(help_text='List the amenities available in the room.')
    occupancy = models.PositiveIntegerField(
        help_text='Specify the maximum number of guests allowed in the room.')
    # room_size = models.CharField(max_length=50, help_text='Enter the size of the room.')
    # view = models.CharField(max_length=100, help_text='Specify any specific views from the room.')
    availability = models.BooleanField(
        default=True, help_text='Indicate if the room is currently available for booking.')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, help_text='Enter the price per night for the room.')
    no_of_bed = models.PositiveBigIntegerField(
        null=True, help_text='Specify number of Beds')
    no_of_bath = models.PositiveBigIntegerField(
        null=True, help_text='Specify number of Baths')
    # photos = models.ImageField(upload_to='room_photos/', help_text='Upload photos of the room.')
    # additional_services = models.TextField(help_text='Specify any additional services offered with the room.')
    # accessibility_features = models.TextField(help_text='Describe any accessibility features of the room.')
    # cancellation_policy = models.TextField(help_text='Describe the hotel\'s cancellation policy for bookings made for this room.')
    # special_offers = models.TextField(help_text='List any special offers or packages associated with booking this room.')

    def __str__(self):
        return f"{self.get_room_type_display()} - ${self.price} per night"


class BookRoom(models.Model):
    generated_id = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"by {self.user.username} - {self.room.room_type}"
