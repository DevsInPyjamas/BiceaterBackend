from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AppUser(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    MALE = 'M'
    FEMALE = 'F'
    GENRE_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    DoB = models.DateField(null=True)
    image = models.ImageField(blank=True, upload_to='profile_images', null=True)
    description = models.TextField(blank=True)
    genre = models.CharField(
        max_length=1,
        choices=GENRE_CHOICES,
        default=MALE
    )
    hobbies = models.TextField(blank=True)
    isAdmin = models.BooleanField(default=False)

    def to_dict(self):
        return {
            'user_id': self.user.id,
            'username': self.user.username,
            'name': self.user.first_name,
            'surname': self.user.last_name,
            'DoB': str(self.DoB),
            'image': self.image.path,
            'description': self.description,
            'genre': self.genre,
            'hobbies': self.hobbies,
            'isAdmin': self.isAdmin
        }

    def __str__(self):
        return self.user.username + ": " + str(self.user_id)


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    text = models.TextField(max_length=140, default='')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE
    )
    answers_to = models.ForeignKey(
        'BiceaterAPI.Comment',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    bike_hire_docking_station_id = models.CharField(max_length=100,
                                                    default='0', blank=True, null=True)

    def to_dict(self):
        if not self.answers_to:
            return {
                'comment_id': self.comment_id,
                'text': self.text,
                'date': str(self.date),
                'author': self.author.to_dict(),
                'answers_to': None,
                'bike_hire_docking_station_id':
                    self.bike_hire_docking_station_id
            }
        else:
            return {
                'comment_id': self.comment_id,
                'text': self.text,
                'date': str(self.date),
                'author': self.author.to_dict(),
                'answers_to': self.answers_to.to_dict(),
                'bike_hire_docking_station_id':
                    self.bike_hire_docking_station_id
            }

    def __str__(self):
        return self.author.user.username + ": " + str(self.comment_id)


class Rating(models.Model):
    rating_id = models.BigAutoField(primary_key=True)
    rating = models.IntegerField(null=False, default=3)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AppUser,
                               on_delete=models.CASCADE,
                               null=False)
    bike_hire_docking_station_id = models.CharField(max_length=100,
                                                    default='0')

    def to_dict(self):
        return {
            'rating_id': self.rating_id,
            'rating': self.rating,
            'date': str(self.date),
            'author': self.author.to_dict(),
            'bike_hire_docking_station_id':
                self.bike_hire_docking_station_id
        }

    def __str__(self):
        return self.author.user.username + ": " + str(self.rating_id)
