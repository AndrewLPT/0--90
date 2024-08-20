from django import forms
from .models import UserFoodLog, Food

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = UserFoodLog
        fields = ['food', 'date_consumed', 'quantity']

# 在views.py中處理表單
from django.shortcuts import render, redirect
from .forms import FoodLogForm

def log_food(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        if form.is_valid():
            food_log = form.save(commit=False)
            food_log.user = request.user
            food_log.calories_consumed = food_log.food.calories * food_log.quantity
            food_log.protein_consumed = food_log.food.protein * food_log.quantity
            food_log.carbs_consumed = food_log.food.carbs * food_log.quantity
            food_log.fat_consumed = food_log.food.fat * food_log.quantity
            food_log.save()
            return redirect('dashboard')
    else:
        form = FoodLogForm()
    return render(request, 'log_food.html', {'form': form})
