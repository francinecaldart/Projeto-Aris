from django.forms import ModelForm
from .models import NC


class NCForm (ModelForm):
    class Meta:
        model = NC
        fields = '__all__'