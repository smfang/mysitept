# from django.db import models  # import the models package. This line is already existing as soon as we use 'startapp'
# from datetime import datetime


# # Must inherit from Django Model class
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     birth_date = models.DateField()
#     has_pet = models.BooleanField(default=True)
#     number_pet = models.IntegerField()


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     category = models.CharField(max_length=50)
#     released_date = models.DateField(default=datetime.now())
#     # author = models.ForeignKey(Person, on_delete=models.CASCADE)

#     # If you delete a person, his posts will be also deleted

#     def __str__(self):
#         return f'{self.title}'
