from .models import UserFoodLog, MetabolicData

def generate_nutrition_suggestion(user):
    tdee = user.metabolicdata.tdee
    recent_food_logs = UserFoodLog.objects.filter(user=user).order_by('-date_consumed')[:7]

    total_calories = sum([log.calories_consumed for log in recent_food_logs])
    total_protein = sum([log.protein_consumed for log in recent_food_logs])
    total_carbs = sum([log.carbs_consumed for log in recent_food_logs])
    total_fat = sum([log.fat_consumed for log in recent_food_logs])

    # 根據用戶的目標和數據生成建議
    suggestion = "您過去一周攝入的總卡路里為 {total_calories} 大卡。"
    if total_calories > tdee:
        suggestion += " 您的攝入量超過了建議的能量消耗，建議減少每日攝入。"
    else:
        suggestion += " 您的攝入量低於能量消耗，考慮增加營養攝入以達到您的健康目標。"
    
    return suggestion
