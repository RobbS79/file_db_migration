from django.shortcuts import render, redirect
from .forms import FileUploadForm

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file-upload-success')
    else:
        form = FileUploadForm()
    return render(request, 'orm_file_db_model/upload.html', {'form': form})