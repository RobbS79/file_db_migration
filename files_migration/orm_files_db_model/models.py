from django.db import models
import os


class FileData(models.Model):
    file_name = models.CharField(max_length=255)  # Still keeping the file name
    file_content = models.TextField()  # To store the string content of the file
    uploaded_file = models.FileField(upload_to='uploads/', blank=True, null=True)  # Allow file uploads

    def save(self, *args, **kwargs):
        if self.uploaded_file:
            # Open the uploaded file and read its content
            file_path = self.uploaded_file.path
            with open(file_path, 'r') as f:
                self.file_content = f.read()  # Read the file content
            self.file_name = os.path.basename(self.uploaded_file.name)  # Store the file name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name

