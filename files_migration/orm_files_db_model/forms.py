from django import forms
from .models import FileData

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileData
        fields = ['uploaded_file']  # Only the file field will be displayed

class MultiFileUploadForm(forms.Form):
    uploaded_files = forms.FileField(widget=forms.FileInput(), label='Select files', required=True)
