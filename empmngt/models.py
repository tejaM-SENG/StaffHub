from django.db import models

# Create your models here.

class Calender(models.Model):
    Date = models.DateField()
    Occasion = models.TextField(max_length=1000)
    
class News(models.Model):
    Details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)


class Employee(models.Model):
    # Existing fields
    Name = models.CharField(max_length=100)
    
    Emp_ID = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )
    
    Date_of_Joining = models.DateField()
    Designation = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Annual_CTC = models.FloatField()
    Experience = models.FloatField()

    # Profile and contact information
    Profile_Photo = models.ImageField(
        upload_to="employee_photos/",
        blank=True,
        null=True
    )
    Email = models.EmailField(blank=True)
    Phone = models.CharField(max_length=20, blank=True)
    Date_of_Birth = models.DateField(blank=True, null=True)
    Address = models.TextField(blank=True)
    City = models.CharField(max_length=100, blank=True)
    State = models.CharField(max_length=100, blank=True)

    # Professional information
    Employment_Type = models.CharField(
        max_length=30,
        choices=[
            ("Full-time", "Full-time"),
            ("Part-time", "Part-time"),
            ("Contract", "Contract"),
            ("Intern", "Intern"),
        ],
        blank=True
    )
    Skills = models.TextField(blank=True)
    LinkedIn = models.URLField(blank=True)
    Reporting_Manager = models.CharField(max_length=100, blank=True)

    # Resume document
    Resume = models.FileField(
        upload_to="employee_resumes/",
        blank=True,
        null=True
    )


    def save(self, *args, **kwargs):
        if not self.Emp_ID:
            last_employee = (
                Employee.objects
                .filter(Emp_ID__startswith="EMP")
                .order_by("-id")
                .first()
            )

            next_number = 1

            if last_employee:
                try:
                    last_number = int(last_employee.Emp_ID[3:])
                    next_number = last_number + 1
                except (ValueError, TypeError):
                    next_number = Employee.objects.count() + 1

            self.Emp_ID = f"EMP{next_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Name} ({self.Emp_ID})"




class Job(models.Model):
    Role = models.CharField(max_length=100)
    Experience = models.FloatField(max_length=100)
    Skills = models.CharField(max_length=100)
    CTC = models.FloatField(max_length=100)
    Notice_Period = models.FloatField(max_length=100)