from django import forms
from .models import Status


class StatusForms(forms.ModelForm):
    class Meta:
        model=Status
        fields=[
            'user',
            'content',
            'image'
        ]
    # def clean_content(self,*args,**kwargs):
    #     data=self.cleaned_data.get('content')
    #     if len(data)>50:
    #         raise forms.ValidationError('content is too long')
    #     return data
    def clean(self,*args,**kwargs):
        data=self.cleaned_data
        content=data.get('content')
        if content=="":
            content=None
        image=data.get('image')
        if content is None and image is None:
            raise forms.ValidationError('COntent or image is required')
        return data