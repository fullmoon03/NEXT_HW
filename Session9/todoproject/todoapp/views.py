from django.shortcuts import render, redirect
from .models import List
from datetime import datetime
from django.utils import timezone

# Create your views here.
def home(request):
    list = List.objects.all().order_by('end_date')
    return render(request, 'home.html', {'list': list})

def new(request):
    if request.method == 'POST':
        end_date = request.POST['end_date']
        List.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            # end_date = end_date.strptime(date_string, "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
            # 에러 : str object has no attribute strptime
            end_date = datetime.fromisoformat(end_date),
            #str에서 date로 
            
        )
        return redirect('home')
    current_date_shown = datetime.isoformat(timezone.localtime(timezone.now()))
    return render(request, 'new.html', {'current_date_shown': current_date_shown})

def detail(request, todo_id):
    todo = List.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})

def update(request, todo_id):
    todo = List.objects.get(id=todo_id)
    if request.method == 'POST':
        end_date = request.POST['end_date']
        List.objects.filter(id=todo_id).update(
            title = request.POST['title'],
            content = request.POST['content'],
            end_date = datetime.fromisoformat(end_date),
        )
        return redirect('detail', todo_id)
    end_date_shown = datetime.isoformat(timezone.localtime(todo.end_date))
    #end_date를 로컬 타임으로 바꾼 후 str 폼으로 바꿈
    return render(request, 'update.html', {'todo': todo, 'end_date_shown': end_date_shown})

def delete(request, todo_id):
    todo = List.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')
