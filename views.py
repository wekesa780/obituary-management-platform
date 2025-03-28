from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Obituary
from .forms import ObituaryForm

def obituary_list(request):
    try:
        obituaries = Obituary.objects.all().order_by('-created_at')
        return render(request, 'obituaries/list.html', {'obituaries': obituaries})
    except Exception as e:
        messages.error(request, f"Error loading obituaries: {str(e)}")
        return render(request, 'obituaries/list.html', {'obituaries': []})

def add_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Obituary added successfully!')
                return redirect('obituary_list')
            except Exception as e:
                messages.error(request, f'Save failed: {str(e)}')
    else:
        form = ObituaryForm()
    return render(request, 'obituaries/add.html', {'form': form})