from django.forms import ModelForm, ModelChoiceField

from .models import Mark


class ChoiceMark(ModelForm):
    mark_name = ModelChoiceField(queryset=Mark.objects.all(), empty_label='(Noting)')

    class Meta:
        model = Mark
        fields = ['name']





