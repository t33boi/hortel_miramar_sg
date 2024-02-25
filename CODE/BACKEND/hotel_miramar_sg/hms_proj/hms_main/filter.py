import django_filters
from .models import Room

class RoomFilter(django_filters.FilterSet):
    class Meta:
        model = Room
        fields = ['room_type','occupancy','price','no_of_bed']