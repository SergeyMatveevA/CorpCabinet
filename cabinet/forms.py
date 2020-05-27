from django import forms

from cabinet.lib import get_surveys


class SurveyStatForm(forms.Form):
    date_start = forms.DateField()
    date_end = forms.DateField()

    def __init__(self, *args, **kwargs):
        super(SurveyStatForm, self).__init__(*args, **kwargs)
        self.fields['SurveyName'] = forms.ChoiceField(widget=forms.Select(), choices=get_surveys())
