from django.shortcuts import render



rooms = [
{'id':1, 'name':'DailyM8 Project'},
{'id':2, 'name':'DailyM8 Developers'},
{'id':3, 'name':'DailyM8 Users'}

]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', {'rooms': rooms}, context)

def room(request):
    return render(request, 'room.html')

