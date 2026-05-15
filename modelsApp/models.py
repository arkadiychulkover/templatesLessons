from django.db import models
import uuid
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagePath = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name} - ${self.price} - {self.description} - Created at: {self.created_at} - Updated at: {self.updated_at} - Image Path: {self.imagePath}"
     

    class Meta:
        db_table = 'dj_product'



class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    class Mena:
        db_table = 'dj_product'

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    members = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_progress(self):
        avg = self.tasks.aggregate(Avg('progress'))['progress__avg']
        return avg or 0

    class Meta:
        db_table = 'dj_projects'

    def __str__(self):
        return self.name
    

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dj_tasks'

    def __str__(self):
        return self.name
    












class Reader(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=255)

    is_available = models.BooleanField(default=True)

    reader = models.ForeignKey(
        Reader,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books'
    )

    def save(self, *args, **kwargs):
        self.is_available = self.reader is None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title