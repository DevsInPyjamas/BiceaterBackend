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
    username = models.CharField(unique=True, max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, blank=True)
    DoB = models.DateField(null=True)
    image = models.ImageField(blank=True, upload_to='profile_images', default='/media/')
    description = models.TextField(blank=True)
    genre = models.CharField(
        max_length=1,
        choices=GENRE_CHOICES,
        default=MALE
    )
    hobbies = models.TextField(blank=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'DoB': str(self.DoB),
            'image': self.image.path,
            'description': self.description,
            'genre': self.genre
        }


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    text = models.TextField(max_length=140, default='')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    answers_to = models.ForeignKey(
        'BiceaterAPI.Comment',
        on_delete=models.CASCADE,
        null=True
    )
    bike_hire_docking_station_id = models.CharField(max_length=100,
                                                    default='0')

    def to_dict(self):
        return {
            'comment_id': self.comment_id,
            'text': self.text,
            'date': str(self.date),
            'author': self.author.to_dict(),
            'answers_to': self.answers_to.to_dict(),
            'bike_hire_docking_station_id':
                self.bike_hire_docking_station_id
        }


class Rating(models.Model):
    rating_id = models.BigAutoField(primary_key=True)
    rating = models.IntegerField(null=False, default=3)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,
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
