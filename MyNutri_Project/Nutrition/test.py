from django.test import TestCase
from .models import User, Food, UserFoodLog

class NutritionAppTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.food = Food.objects.create(name='Apple', calories=52, protein=0.3, carbs=14, fat=0.2)

    def test_food_log_creation(self):
        log = UserFoodLog.objects.create(user=self.user, food=self.food, quantity=1, calories_consumed=52)
        self.assertEqual(log.calories_consumed, 52)
