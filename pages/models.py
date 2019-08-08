from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class MovieCategory(models.Model):
    class Meta:
        verbose_name_plural = 'category first'

    cat_name_one = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name_one

class MovieCategorySecond(models.Model):
    class Meta:
        verbose_name_plural = 'category second'

    cat_name_two = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name_two

class MovieQuality(models.Model):
    class Meta:
        verbose_name_plural = 'Quality'

    quality = models.CharField(max_length=20)

    def __str__(self):
        return self.quality

class MovieRating(models.Model):

    rating = models.CharField(max_length=20)

    def __str__(self):
        return self.rating

class Order_by(models.Model):
    class Meta:
        verbose_name_plural = 'Order_by'

    movie_order_by = models.CharField(max_length=20)

    def __str__(self):
        return self.movie_order_by

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_description = models.CharField(max_length=1000)
    movie_year = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    is_published = models.BooleanField(default=True)
    movie_date = models.DateTimeField(default=timezone.now)

    #Foreign Keys
    movie_category = models.ForeignKey(MovieCategory, on_delete=models.DO_NOTHING)
    movie_category_second = models.ForeignKey(MovieCategorySecond, on_delete=models.DO_NOTHING)
    movie_quality = models.ForeignKey(MovieQuality, on_delete=models.DO_NOTHING)
    movie_rating = models.ForeignKey(MovieRating, on_delete=models.DO_NOTHING)
    movie_order = models.ForeignKey(Order_by, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.movie_name

class Review(models.Model):
    class Meta:
        verbose_name_plural = 'Reviews'

    movie_title_content = models.CharField(max_length=100)
    movie_content = models.TextField(max_length=1000)
    movie_date = models.DateTimeField(default=timezone.now)

    #Foreign Keys
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_rating = models.ForeignKey(MovieRating, on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.movie_title_content

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})



