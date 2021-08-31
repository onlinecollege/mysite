from django import forms
from django.forms.widgets import URLInput

Subject = (
    ('Islamiat I', 'Islamiat I'), ('English I', 'English I'), ('Urdu I', 'Urdu I'), ('AD I', 'AD I'), ('PD I', 'PD I'),
    ('Ess. Maths', 'Ess. Maths'), ('Lab I', 'Lab I'), ('AD II', 'AD II'), ('PD II', 'PD II'), ('Chemistry I', 'Chemistry I'),
    ('BioMaths', 'BioMaths'), ('Lab II', 'Lab II'), ('English II', 'English II'), ('Islamiat II', 'Islamiat II'), ('Urdu II', 'Urdu II'),
    ('Cell Bio', 'Cell Bio'), ('Mol. Bio', 'Mol. Bio'), ('Chemistry II', 'Chemistry II'), ('EVS', 'EVS'), ('Lab III', 'Lab III'),
    ('Developmental Bio', 'Developmental Bio'), ('Animal Physio', 'Animal Physio'), ('Plant Physio', 'Plant Physio'), ('Biophysics', 'Biophysics'), ('Lab IV', 'Lab IV'),
    ('Microbiology', 'Microbiology'), ('Immunology', 'Immunology'), ('Genetics', 'Genetics'), ('Bioinfo', 'Bioinfo'), ('Lab V', 'Lab V'), 
    ('Biochemistry', 'Biochemistry'), ('Ecology', 'Ecology'), ('Evolution', 'Evolution'), ('TIB', 'TIB'), ('Lab VI', 'Lab VI')
)

Year = (
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025')
)

Category = (
    ('Semester', 'Semester'),
    ('Sessional I', 'Sessional I'),
    ('Sessional II', 'Sessional II')
)

class NewPaperForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. semester 5 Genetics Paper '}))
    subject = forms.ChoiceField(choices=Subject)

    year = forms.ChoiceField(choices=Year)
    
    your_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Mohammad Ali'}))

    category = forms.ChoiceField(choices=Category)
    file_url = forms.URLField(widget=URLInput(attrs={'placeholder': 'Please paste the above generated link'}))

class SubjectPaperForm(forms.Form):
    subject = forms.ChoiceField(choices=Subject)


class SearchPaperForm(forms.Form):
    subject = forms.ChoiceField(choices=Subject)
    year = forms.ChoiceField(choices=Year)    
    category = forms.ChoiceField(choices=Category)


class NewNotesForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Protein Synthesis'}))
    subject = forms.ChoiceField(choices=Subject)

    source =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Where did you get these notes?'}))   
    your_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'e.g. Mohammad Ali'}))
    file_url = forms.URLField(widget=URLInput(attrs={'placeholder': 'Please paste the above generated link'}))
