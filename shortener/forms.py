from django import forms
from .validators import validate_url
class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        # label='Submit URL',
        validators=[validate_url],
        widget=forms.TextInput(attrs={'placeholder': 'Submit a long URL'})
    )
    # def clean(self):
    #     cleaned_data = super().clean()  # means that this data can be verified
    #     # url = cleaned_data.get("url")
    #     # print(url)
    #
    # def clean_url(self):    # works for the field called url only. new one is needed for new field
    #     url = self.cleaned_data['url']
    #     # print(url)
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL!")
    #     return url
