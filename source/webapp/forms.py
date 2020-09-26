from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.exceptions import ValidationError
from django.forms import MultipleChoiceField

# from .models import Statuses, Issues, TO_DO_List, Project


class DateInput(forms.DateInput):
    input_type = 'date'


# class ToDoForm(forms.ModelForm):
#     class Meta:
#         model = TO_DO_List
#         fields = ['summary', 'description', 'status', 'issue']
#         widgets = {'issue': forms.CheckboxSelectMultiple}
#
#     def clean(self):
#         cleaned_data = super().clean()
#         errors = []
#         summary = cleaned_data.get('summary')
#         description = cleaned_data.get('description')
#         if summary == description:
#             errors.append(ValidationError("Text of the article should not duplicate it's title!"))
#         if errors:
#             raise ValidationError(errors)
#         return cleaned_data
#
#
# class SeacrhForm(forms.Form):
#     search = forms.CharField(max_length=50, required=False, label='Найти')
#
#
# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['begin_date', 'end_date', 'title', 'description', 'team']
#         # widgets = {'team': forms.MultipleChoiceField}
#         widgets = {'team': forms.CheckboxSelectMultiple}
#
#
# class ManageTeamForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['team']
#         # widgets = {'team': forms.MultipleChoiceField}
#         widgets = {'team': forms.CheckboxSelectMultiple}