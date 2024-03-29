from django import forms
from myfitness.models import Fitness
from myfitness.models import Calorie
from myfitness.models import Weight
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class FitnessForm(forms.ModelForm):
    class Meta:
        model = Fitness
        fields = ['lift', 'reps','weight']

class CalorieForm(forms.ModelForm):
    class Meta:
        model = Calorie
        fields = ['type', 'calorie', 'protein', 'carbs', 'fats']

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['start', 'goal', 'last', 'current']