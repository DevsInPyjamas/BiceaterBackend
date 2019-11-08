from django.db import models

# Create your models here.

class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENRE_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50, blank=True)
    DoB = models.DateField(null=True)
    image = models.ImageField(null=True)
    description = models.TextField(blank=True)
    genre = models.CharField(
        max_length=1,
        choices=GENRE_CHOICES,
        default=MALE
    )
    hobbies = models.TextField(blank=True)


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    text = models.TextField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    answers_to = models.ForeignKey(
        'BiceaterAPI.Comment',
        on_delete=models.CASCADE,
        null=True
    )
    stop_id = models.IntegerField()
