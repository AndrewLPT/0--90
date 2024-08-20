from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='nutrition_user_set',  # 為 groups 指定一個新的 related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='nutrition_user_permissions_set',  # 為 user_permissions 指定一個新的 related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    health_goal = models.CharField(max_length=255)

class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()

class UserFoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date_consumed = models.DateTimeField()
    quantity = models.FloatField()
    calories_consumed = models.FloatField()
    protein_consumed = models.FloatField()
    carbs_consumed = models.FloatField()
    fat_consumed = models.FloatField()

class MetabolicData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bmr = models.FloatField()  # 基礎代謝率
    activity_level = models.FloatField()
    tdee = models.FloatField()  # 總每日能量消耗
