from django import forms

choices = [
    (1, 'English'),
    (2, 'French'),
    (3, 'Swedish'),
    (4, 'Dutch'),
]

class UserForm(forms.Form):
    field_order = [
        "name",
        "surname",
        "email",
        "phone",
        "password",
        "set_lang",
        "lang",
        "about"
    ]

    name = forms.CharField(initial="John", label="Name")
    surname = forms.CharField(initial="Smith", label="Surname")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Contact phone")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter password")
    set_lang = forms.ChoiceField(choices=choices, label="Preferred language")
    lang = forms.MultipleChoiceField(choices=choices)
    about = forms.CharField(widget=forms.Textarea, label="About")