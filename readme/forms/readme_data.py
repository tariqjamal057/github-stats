
from django.forms import ModelForm
from readme.models import ReadmeData

class CreateReadmeFileForm(ModelForm):
        
    class Meta:
        model = ReadmeData
        fields = ['file_name']
