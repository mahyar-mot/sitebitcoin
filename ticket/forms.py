from django import forms
from django.forms import modelformset_factory

from . import models


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'category', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].label = "عنوان"
        self.fields['category'].label = "دسته بندی"
        self.fields['text'].label = "متن مشکل"


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Messages
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'rows':5})
        self.fields['body'].label = "پیام"


EditTicketFormSet = modelformset_factory(models.Ticket, fields=('close',), extra=0)
