
from django.forms import ModelForm

from readme.models import Component

class ReadmeDataForm(ModelForm):
    pass    
    class Meta:
        model = Component
        fields = ['name', 'symbol', 'description', 'type', 'build_type']
