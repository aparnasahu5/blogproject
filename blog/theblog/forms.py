from django import forms
from .models import Post, Category

#Choices=[('coding','coding'),('sports','sports'),('entertainment','entertainment'),]
Choices= Category.objects.all().values_list('name','name')
choice_list=[]

for item in Choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'input title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ('title','title_tag','body')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'input title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),

        }