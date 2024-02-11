from django import forms
from myfitness.models import Fitness
from myfitness.models import Calorie

class FitnessForm(forms.ModelForm):
    class Meta:
        model = Fitness
        fields = ['lift', 'reps','weight']

class CalorieForm(forms.ModelForm):
    class Meta:
        model = Calorie
        fields = ['type', 'calorie', 'protein', 'carbs', 'fats']