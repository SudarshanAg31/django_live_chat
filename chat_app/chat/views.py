from django.shortcuts import render,redirect
from .models import Room,Message
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):  
    return render(request,'index.html')

def room(request,pk):
    username=request.GET.get('username')
    room_detail=Room.objects.get(name=pk)
    return render(request,'room.html',{'username':username,'room_details':room_detail,'room':pk})
def checkview(request):  
    room=request.POST['room_name']
    username=request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
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