from django import forms

from . import models


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ['title', 'slug', 'body', 'blogtag', 'thumbnail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class':'form-control'})
        self.fields['title'].label = "عنوان"
        self.fields['slug'].label = "آدرس"
        self.fields['body'].label = "متن"
        self.fields['blogtag'].label = "دسته‌بندی"
        self.fields['thumbnail'].label = "تصویر"
        self.fields['thumbnail'].widget.attrs.update({'class':'form-control-file'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']