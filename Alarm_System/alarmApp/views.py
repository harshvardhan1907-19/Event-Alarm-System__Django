from django.shortcuts import render, redirect
from alarmApp.models import Alarm
from alarmApp.forms import AlarmEvent
from datetime import date, datetime
from django.http import JsonResponse

def add_event(request):
    if request.method == "POST":
        form = AlarmEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlarmEvent()
    
    return render(request, 'add_event.html', {"form":form})

def event_list(request):
    events = Alarm.objects.all().order_by('start_date')

    selected_date = request.GET.get('date')
    month = request.GET.get('month')
    weekday = request.GET.get('weekday')

    if selected_date:
        try:
            date_obj = datetime.strptime(selected_date, "%Y-%m-%d").date()
            events = events.filter(
                start_date__lte = date_obj,
                end_date__gte = date_obj
            )
        except ValueError:
            pass
    
    if month:
        events = events.filter(start_date__month = int(month))
    
    if weekday:
        events = events.filter(start_date__week_day = int(weekday))

    return render(request, 'index.html', {'events': events})

def events_json(request):
    events = Alarm.objects.all()
    data = []

    for event in events:
        data.append({
            'title' : event.title,
            'start_date' : event.start_date.strftime("%Y-%m-%d"),
            'end_date': event.end_date.strftime("%Y-%m-%d"),
            'time': event.time.strftime("%H:%M") if event.time else None
        })

    return JsonResponse(data, safe=False)


# separate from alarm syem -> play music on change dropdoem
def play_song(request):
    return render(request, "Onchange.html")