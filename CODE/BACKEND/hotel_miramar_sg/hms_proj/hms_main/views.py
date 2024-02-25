from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

from .models import Room,BookRoom,Person

# Create your views here.
# @login_required(login_url='/auth/login')
def index(request):
    print(request.user)
    return render(request,'home.html')

def room(request):
     if request.method == 'GET':
        room_type = request.GET.get('room_type', '')
        price = request.GET.get('price', '')
        occupancy = request.GET.get('occupancy', '')
        no_of_bed = request.GET.get('no_of_bed', '')

        default_price_range = (0, 1000)
        default_no_of_bed = 0

        if '-' in price:
            p1, p2 = map(int, price.split('-'))
        else:
            p1, p2 = default_price_range

        no_of_bed = int(no_of_bed) if no_of_bed.isdigit() else default_no_of_bed

        room_type_query = Q(room_type__icontains=room_type)
        price_query = Q(price__range=(p1, p2))
        occupancy_query = Q(occupancy=occupancy)
        no_of_bed_query = Q(no_of_bed=no_of_bed)

        filters = []

        if room_type:
            filters.append(room_type_query)
        if price:
            filters.append(price_query)
        if occupancy:
            filters.append(occupancy_query)
        if no_of_bed:
            filters.append(no_of_bed_query)

        if filters:
            rooms = Room.objects.filter(*filters)
            print(rooms)
        
        else:
            rooms = Room.objects.all()
            print(rooms)

        return render(request, 'rooms.html', {'rooms': rooms})

def book_room(request,pk):
    room_booked = Room.objects.get(id=pk)
    booked_room = BookRoom.objects.create(user=request.user,room=room_booked)
    booked_room.save()
    return redirect('check_out')


# class CheckOut(View):
#     # @login_required(login_url='/auth/login')
#     def get_object(self,request,pk):
        # user = request.user 
        # user = Person.objects.get(username=user)
        # return  user.bookroom_set.get(id=pk)
    
#     def get(self,request):
#         if request.user is not None:
#             user = request.user 
#             user = Person.objects.get(username=user)
#             user_room = user.bookroom_set.all()
#             print(user_room)
#             context = {
#                 'rooms' : user_room,
#         }
#             return render(request,'check_out.html',context)
#         else:
#             return HttpResponse('Login First')
    
#     def delete(self,request,pk):
#         user_room = self.get_object(request,pk)
#         user_room.delete()
#         return redirect('check_out')

def check_out(request):
    user = request.user 
    user = Person.objects.get(username=user)
    user_room = user.bookroom_set.all()
    print(user_room)
    context = {
        'rooms' : user_room,
}
    return render(request,'check_out.html',context)

def check_out_delete(request,pk):
    user = request.user 
    user = Person.objects.get(username=user)
    user_room = user.bookroom_set.get(id=pk)
    user_room.delete()
    return redirect('check_out')

    