from django.shortcuts import render,redirect
from .models import Room,Message
import json 
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):  
    return render(request,'index.html')

def room(request,pk):
    username=request.GET.get('username')
    room_detail=Room.objects.get(name=pk)
    return render(request,'room.html',{'username':username,'room_details':room_detail,'room':pk})
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        room_obj = Room.objects.get(name=room)
        room_obj.users += 1
        room_obj.save()
    else:
        room_obj = Room.objects.create(name=room, users=1)
    return redirect('/' + room + '/?username=' + username)
def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']
    # date=Message.objects.get()
    new_message=Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse("message has been send successfully")
def getmessages(request,pk):
    room_details=Room.objects.get(name=pk)
    message=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(message.values())})
from django.http import JsonResponse
import traceback

def leave_room(request):
    try:
        data = json.loads(request.body)

        room = Room.objects.filter(name=data["room"]).first()

        if room:
            room.users -= 1

            if room.users <= 0:
                print("Deleting messages...")
                Message.objects.filter(room=str(room.id)).delete()

                print("Deleting room...")
                room.delete()
            else:
                room.save()

        return JsonResponse({"status": "success"})

    except Exception as e:
        print(traceback.format_exc())
        return JsonResponse({"error": str(e)}, status=500)