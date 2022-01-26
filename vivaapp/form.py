from django import forms
from vivaapp.models import User, ClassManagement, SubjectManagement, ChapterManagement, QuestionType, EducationBoard
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import ValidationError

class Loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'inputEmail', 'class':'form-control', 'name':'username', 'autofocus':'autofocus', 'placeholder':' '}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'inputPassword', 'class':'form-control', 'name':'password', 'placeholder':' '}), required=False)


class Userregisterform(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email_id', 'contact_number', 'password1', 'password2', 'account_type', 'date_of_birth']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'id':'full_name', 'class':'form-control', 'name':'full_name', 'placeholder':' '}), required=False, label='Your Full Name')
    email_id = forms.CharField(widget=forms.TextInput(attrs={'id':'email_id', 'class':'form-control', 'name':'email_id', 'placeholder':' '}), required=False, label='Your Email Id')
    #password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password', 'class':'form-control', 'name':'upassword', 'placeholder':' '}), required=False, label='Create Password')
    #password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id':'cpassword', 'class':'form-control', 'name':'cpassword', 'placeholder':' '}), required=False, label='Confirm Password')
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type':'date','class':'form-control'}), required=False, label='Date of Birth') 

    def __init__(self, *args, **kwargs):
        super(Userregisterform, self).__init__(*args, **kwargs)

        self.fields['contact_number'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'contact_number', 'placeholder':' '})
        self.fields['contact_number'].label = 'Contact Number'
        self.fields['contact_number'].required = False

        self.fields['account_type'].widget.attrs.update({'id':'type', 'class':'form-control', 'name':'account_type', 'placeholder':' '})
        self.fields['account_type'].required = False

        self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder': 'Confirm Password'})  
        self.fields['password1'].required = False  
        self.fields['password2'].required = False

    def clean(self):
        cleaned_data = super().clean()
        full_name    = cleaned_data.get('full_name')
        email_id   = cleaned_data.get('email_id')
        contact_number  = cleaned_data.get('contact_number')
        password1   = cleaned_data.get('password1')
        #cpassword   = cleaned_data.get('cpassword')
        account_type     = cleaned_data.get('account_type')
        date_of_birth = cleaned_data.get('date_of_birth')

        if not full_name:
            self.add_error('full_name', 'Full name is required')
        if not email_id:
            self.add_error('email_id', 'Email id is required')
        if User.objects.filter(email_id=email_id).exists():
            self.add_error('email_id', 'Email Already Exist')
        if not contact_number:
            self.add_error('contact_number', 'Contact Number is required')
        if contact_number and User.objects.filter(contact_number=contact_number).exists():
            self.add_error('contact_number', 'Number Already Exist')
        if not password1:
            self.add_error('password1', 'Password is required')
        '''if not cpassword:
            self.add_error('cpassword', 'Confirm password is required')   
        if cpassword and cpassword != upassword:
            self.add_error('cpassword', 'Password not matchin')'''
        if not account_type:
            self.add_error('account_type', 'Account type is required.')
        if not date_of_birth:
            self.add_error('date_of_birth', 'DOB is required')
            
class ClassForms(forms.ModelForm):
    class Meta:
        model = ClassManagement
        fields = ['class_name']
    def __init__(self, *args, **kwargs):
        super(ClassForms, self).__init__(*args, **kwargs)
        self.fields['class_name'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'class_name', 'placeholder':' '})
        self.fields['class_name'].label = 'Class Name'
        self.fields['class_name'].required = False

    def clean(self):
        cleaned_data = super().clean()
        class_name  =   cleaned_data.get('class_name')
        if not class_name:
            self.add_error('class_name', 'Class is required!')
        if class_name and  ClassManagement.objects.filter(class_name=class_name).exists():
            self.add_error('class_name', 'Class already exist ')


class SubjectForms(forms.ModelForm):
    class Meta:
        model = SubjectManagement
        fields = ['subject_name']
    def __init__(self, *args, **kwargs):
        super(SubjectForms, self).__init__(*args, **kwargs)
        self.fields['subject_name'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'subject_name', 'placeholder':' '})
        self.fields['subject_name'].label = 'Subject Name'
        self.fields['subject_name'].required = False

    def clean(self):
        cleaned_data = super().clean()
        subject_name  =   cleaned_data.get('subject_name')
        if not subject_name:
            self.add_error('subject_name', 'Subject is required!')
        if subject_name and SubjectManagement.objects.filter(subject_name=subject_name).exists():
            self.add_error('subject_name', 'Subject already exist ')

class ChapterForms(forms.ModelForm):
    class Meta:
        model = ChapterManagement
        fields = ['chapter_name']
    def __init__(self, *args, **kwargs):
        super(ChapterForms, self).__init__(*args, **kwargs)
        self.fields['chapter_name'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'chapter_name', 'placeholder':' '})
        self.fields['chapter_name'].label = 'Chapter Name'
        self.fields['chapter_name'].required = False

    def clean(self):
        cleaned_data = super().clean()
        chapter_name  =   cleaned_data.get('chapter_name')
        if not chapter_name:
            self.add_error('chapter_name', 'Chapter is required!')
        if chapter_name and ChapterManagement.objects.filter(chapter_name=chapter_name).exists():
            self.add_error('chapter_name', 'Chapter already exist ')

class QuestionTypeForms(forms.ModelForm):
    class Meta:
        model = QuestionType
        fields = ['question_name']
    def __init__(self, *args, **kwargs):
        super(QuestionTypeForms, self).__init__(*args, **kwargs)
        self.fields['question_name'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'question_name', 'placeholder':' '})
        self.fields['question_name'].label = 'Question Type Name'
        self.fields['question_name'].required = False

    def clean(self):
        cleaned_data = super().clean()
        question_name  =   cleaned_data.get('question_name')
        if not question_name:
            self.add_error('question_name', 'Question type is required!')
        if question_name and QuestionType.objects.filter(question_name=question_name).exists():
            self.add_error('question_name', 'Question type already exist ')

class EducationBoardForms(forms.ModelForm):
    class Meta:
        model = EducationBoard
        fields = ['board_name']
    def __init__(self, *args, **kwargs):
        super(EducationBoardForms, self).__init__(*args, **kwargs)
        self.fields['board_name'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'board_name', 'placeholder':' '})
        self.fields['board_name'].label = 'Education Board Name'
        self.fields['board_name'].required = False

    def clean(self):
        cleaned_data = super().clean()
        board_name  =   cleaned_data.get('board_name')
        if not board_name:
            self.add_error('board_name', 'Education Board is required!')
        if board_name and EducationBoard.objects.filter(board_name=board_name).exists():
            self.add_error('board_name', 'Education Board already exist ')

class UserEditform(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email_id', 'contact_number', 'account_type', 'date_of_birth']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'id':'full_name', 'class':'form-control', 'name':'full_name', 'placeholder':' ', 'readonly':True}), required=False, label='Your Full Name')
    email_id = forms.CharField(widget=forms.TextInput(attrs={'id':'email_id', 'class':'form-control', 'name':'email_id', 'placeholder':' ', 'readonly':True}), required=False, label='Your Email Id')
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type':'date','class':'form-control', 'readonly':True}), required=False, label='Date of Birth') 

    def __init__(self, *args, **kwargs):
        super(UserEditform, self).__init__(*args, **kwargs)

        self.fields['contact_number'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'contact_number', 'placeholder':' ', 'readonly':True})
        self.fields['contact_number'].label = 'Contact Number'
        self.fields['contact_number'].required = False

        self.fields['account_type'].widget.attrs.update({'id':'type', 'class':'form-control', 'name':'account_type', 'placeholder':' '})
        self.fields['account_type'].required = False

    def clean(self):
        cleaned_data = super().clean()
        account_type     = cleaned_data.get('account_type')
        
        if not account_type:
            self.add_error('account_type', 'Account type is required.')

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email_id', 'contact_number', 'date_of_birth']

    full_name = forms.CharField(widget=forms.TextInput(attrs={'id':'full_name', 'class':'form-control', 'name':'full_name', 'placeholder':' '}), required=False, label='Your Full Name')
    email_id = forms.CharField(widget=forms.TextInput(attrs={'id':'email_id', 'class':'form-control', 'name':'email_id', 'placeholder':' ', 'readonly':True}), required=False, label='Your Email Id')
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type':'date','class':'form-control'}), required=False, label='Date of Birth') 

    def __init__(self, *args, **kwargs):
        super(AccountEditForm, self).__init__(*args, **kwargs)

        self.fields['contact_number'].widget.attrs.update({'id':'number', 'class':'form-control', 'name':'contact_number', 'placeholder':' ', 'readonly':True})
        self.fields['contact_number'].label = 'Contact Number'
        self.fields['contact_number'].required = False 