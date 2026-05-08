from django import forms

choices = [
    (1, 'English'),
    (2, 'French'),
    (3, 'Swedish'),
    (4, 'Dutch'),
]

class UserForm(forms.Form):
    f_name = forms.CharField(
        initial='John',
        label="Name",
        widget=forms.TextInput(attrs={
            'class': 'validate',
            'placeholder': 'Enter your name'
        })
    )
    name = forms.CharField(initial="John", label="Full Name")
    age_field = forms.IntegerField(
        initial=18,
        min_value=18,
        max_value=100,
        label="Age"
    )
    surname = forms.CharField(initial="Smith", label="Surname")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Contact phone")
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Enter password"
    )
    set_lang = forms.ChoiceField(
        choices=choices,
        label="Preferred language"
    )
    lang = forms.MultipleChoiceField(choices=choices)
    about = forms.CharField(
        widget=forms.Textarea,
        label="About"
    )
    avatar = forms.ImageField(label="Avatar", required=False)

    error_css_class = "error-text"
    required_css_class = "required-text"

    def clean_f_name(self):
        data = self.cleaned_data['f_name']
        if "joe" in str(data).lower():
            self.add_error("f_name", "Please enter your name")
        return data

    def clean(self):
        return super().clean()


choices_months = [
    (1, 'One month'),
    (3, 'Three months'),
    (6, 'Six months'),
    (12, 'Twelve months'),
]

choices_volume = [
    (5, '5 liters'),
    (10, '10 liters'),
    (15, '15 liters'),
]


class WaterForm(forms.Form):
    name = forms.CharField(initial="John", label="Name")
    surname = forms.CharField(initial="Smith", label="Surname")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone")
    address = forms.CharField(label="Address")
    months = forms.ChoiceField(
        choices=choices_months,
        label="Delivery months"
    )
    volume = forms.ChoiceField(
        choices=choices_volume,
        label="Bottle volume"
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label="Notes"
    )

    def clean_email(self):
        data = self.cleaned_data['email']
        if "test" in str(data).lower():
            self.add_error("email", "Invalid email")
        return data

    def clean(self):
        return super().clean()