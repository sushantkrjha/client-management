from django.shortcuts import render, get_object_or_404, redirect
from .models import JobSheet
from .forms import JobSheetForm

def dashboard(request):
    search_query = request.GET.get('search', '')
    if search_query:
        job_sheets = JobSheet.objects.filter(client_name__icontains=search_query)
    else:
        job_sheets = JobSheet.objects.all()
    return render(request, 'dashboard.html', {'job_sheets': job_sheets})

def create_job_sheet(request):
    if request.method == 'POST':
        form = JobSheetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobSheetForm()
    return render(request, 'create_job_sheet.html', {'form': form})

def edit_job_sheet(request, id):
    job_sheet = get_object_or_404(JobSheet, id=id)
    if request.method == 'POST':
        form = JobSheetForm(request.POST, request.FILES, instance=job_sheet)
        if form.is_valid():
            form.save()
            return redirect('view_job_sheet', id=id)
    else:
        form = JobSheetForm(instance=job_sheet)
    return render(request, 'edit_job_sheet.html', {'form': form, 'job_sheet': job_sheet})

def view_job_sheet(request, id):
    job_sheet = get_object_or_404(JobSheet, id=id)
    return render(request, 'view_job_sheet.html', {'job_sheet': job_sheet})

def delete_job_sheet(request, id):
    job_sheet = get_object_or_404(JobSheet, id=id)
    job_sheet.delete()
    return redirect('dashboard')
