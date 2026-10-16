from django import forms
from empmngt.models import Employee, Calender, News, Job
from django.contrib.auth.models import User
import re

class CalenderForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = '__all__'
        
        widgets = {
            'Date': forms.DateInput(attrs={
                'class': 'form-control w-100',
                'type':'date',
                'placeholder': 'Date of Joining',
            }),

            'Occasion': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Occasion',
                'rows': 4
            }),
        }


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "Name": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter full name",
            }),

            "Emp_ID": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter Employee ID",
                "inputmode": "numeric",
            }),

            "Email": forms.EmailInput(attrs={
                "class": "form-control w-100",
                "placeholder": "name@company.com",
            }),

            "Phone": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter 10-digit mobile number",
                "type": "tel",
                "inputmode": "numeric",
                "maxlength": "10",
                "minlength": "10",
                "pattern": "[0-9]{10}",
                "autocomplete": "tel",
            }),

            "Designation": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter designation",
            }),

            "Date_of_Joining": forms.DateInput(attrs={
                "class": "form-control w-100",
                "type": "date",
            }),

            "Date_of_Birth": forms.DateInput(attrs={
                "class": "form-control w-100",
                "type": "date",
            }),

            "Department": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter department",
            }),

            "Annual_CTC": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Example: 8",
                "min": "0",
                "step": "0.1",
            }),

            "Experience": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Example: 2",
                "min": "0",
                "step": "0.5",
            }),

            "Address": forms.Textarea(attrs={
                "class": "form-control w-100",
                "rows": 3,
                "placeholder": "Enter address",
            }),

            "Skills": forms.Textarea(attrs={
                "class": "form-control w-100",
                "rows": 3,
                "placeholder": "Python, Django, SQL, React...",
            }),

            "LinkedIn": forms.URLInput(attrs={
                "class": "form-control w-100",
                "placeholder": "https://www.linkedin.com/in/...",
            }),

            "City": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter city",
            }),

            "State": forms.TextInput(attrs={
                "class": "form-control w-100",
                "placeholder": "Enter state",
            }),

            "Resume": forms.FileInput(attrs={
                "class": "form-control w-100",
                "accept": ".pdf,application/pdf",
            }),

            "Profile_Photo": forms.FileInput(attrs={
                "class": "form-control w-100",
                "accept": "image/*",
            }),
        }

        labels = {
            "Emp_ID": "Employee ID",
            "Annual_CTC": "Annual CTC",
            "Experience": "Experience",
            "Profile_Photo": "Profile Photo",
            "Resume": "Employee Resume",
        }

        error_messages = {
            "Name": {
                "required": "Please enter the employee name.",
            },
            "Phone": {
                "required": "Please enter the phone number.",
                },
            "Email": {
                "required": "Please enter the email address.",
                },
            "Date_of_Joining": {
                "required": "Please select the joining date.",
            },
            "Designation": {
                "required": "Please enter the designation.",
            },
            "Department": {
                "required": "Please enter the department.",
            },
            "Annual_CTC": {
                "required": "Please enter the annual CTC.",
                "invalid": "Please enter a valid annual CTC.",
            },
            "Experience": {
                "required": "Please enter the experience.",
                "invalid": "Please enter a valid experience.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["Emp_ID"].required = False
        self.fields["Emp_ID"].widget = forms.HiddenInput()

        self.fields["Resume"].required = False
            
        required_fields = [
            "Name",
            'Phone',
            'Email',
            "Date_of_Joining",
            "Designation",
            "Department",
            "Annual_CTC",
            "Experience",
        ]
    
        for field_name in required_fields:
            self.fields[field_name].required = True
            

        for field_name, field in self.fields.items():
            existing_class = field.widget.attrs.get("class", "")

            field.widget.attrs["class"] = (
                f"{existing_class} is-invalid"
                if self.is_bound and self.errors.get(field_name)
                else existing_class
            ).strip()


    def clean_Phone(self):
        phone = self.cleaned_data.get("Phone", "")
        
        if not phone:
            return phone

        if not re.fullmatch(r"[0-9]{10}", phone):
            raise forms.ValidationError(
                "Enter a valid phone number containing exactly 10 digits."
            )

        return phone

    def clean_Resume(self):
        resume = self.cleaned_data.get("Resume")

        if not resume:
            return resume

        # Check the extension.
        if not resume.name.lower().endswith(".pdf"):
            raise forms.ValidationError(
                "Only PDF files are allowed for the employee resume."
            )

        # Check the actual file signature, not just its extension.
        try:
            header = resume.read(5)
            resume.seek(0)
        except (AttributeError, OSError):
            raise forms.ValidationError(
                "The uploaded resume could not be read. Please try again."
            )

        if header != b"%PDF-":
            raise forms.ValidationError(
                "The uploaded file is not a valid PDF document."
            )

        return resume
  
        
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['Details']
        
        widgets = {
            'Details': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Details',
                'rows': 4
            }),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        
        widgets = {
            'Role': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Role'
            }),

            'Experience': forms.NumberInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Experience',
                "placeholder": "Example: 2",
                "min": "0",
                "step": "0.5",
            }),

            'Skills': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Skills'
            }),
            
            'CTC': forms.NumberInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter CTC',
                "placeholder": "Example: 8",
                "min": "0",
                "step": "0.1",
            }),

            'Notice_Period': forms.NumberInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Notice Period',
                "placeholder": "Example: 2",
                "min": "0",
                "step": "1",
            }),
        }
 