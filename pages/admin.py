from django.contrib import admin
from .models import Movie, MovieCategory, MovieCategorySecond, MovieQuality, Order_by, MovieRating, Review

class display_to_admin(admin.ModelAdmin):
    list_display = ('movie_name','movie_year','movie_date','movie_category')

# Register your models here.
admin.site.register(Movie, display_to_admin)
admin.site.register(MovieCategory)
admin.site.register(MovieCategorySecond)
admin.site.register(MovieQuality)
admin.site.register(MovieRating)
admin.site.register(Order_by)
admin.site.register(Review)