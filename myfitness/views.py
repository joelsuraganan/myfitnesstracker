from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import date
from myfitness.forms import FitnessForm
from myfitness.models import Fitness
from myfitness.forms import CalorieForm
from myfitness.models import Calorie
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(
        request,
        'myfitness/index.html'
    )

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}    
    return render(request, "myfitness/signup.html", context)

def home(request):
    return render(request, "myfitness/home.html")

def workouts(request):
    return render(request, "myfitness/workouts.html")

def supplements(request):
    return render(request, "myfitness/supplements.html")

def nutrition(request):
    return render(request, "myfitness/nutrition.html")

def faq(request):
    return render(request, "myfitness/faq.html")

def login(request):
    return render(request, "myfitness/login.html")

def logout(request):
    return render(request, "myfitness/logout.html")

def workouttracker(request):
    context = {}
    form = FitnessForm()
    user = request.user.username
    today = date.today()
    fitnesss = Fitness.objects.filter(user_name=user,date=today)

    context ['form'] = form
    context ['fitnesss'] = fitnesss
  
    return render(request, "myfitness/workouttracker.html", context)

def workoutupdate(request):
    
    if request.method == 'POST':
        if 'save' in request.POST:
            key = request.POST.get('save')
            if not key:
                user = request.user.username
                d = date.today()
                lift = request.POST.get('lift')
                reps = request.POST.get('reps')
                weight = request.POST.get('weight')
                Fitness.objects.create(user_name=user, date=d , lift=lift, reps=reps, weight=weight  )
            else:
                fitness = Fitness.objects.get(id=key)
                form = FitnessForm(request.POST, instance=fitness)
                form.save()
        elif 'delete' in request.POST:
            key = request.POST.get('delete')
            fitness = Fitness.objects.get(id=key)
            fitness.delete()
        elif 'edit' in request.POST:
            key = request.POST.get('edit')
            fitness = Fitness.objects.get(id=key)
            form = FitnessForm(instance=fitness)
                                    
    context = {}
    user = request.user.username
    today = date.today()
    fitnesss = Fitness.objects.filter(user_name=user,date=today)
    context ['fitnesss'] = fitnesss
    
    if 'edit' in request.POST:
        context ['form'] = form
        return render(request, "myfitness/workouttracker.html", context)
    else: 
        return redirect(dashboard) 

def calories(request):
    context = {}
    form = CalorieForm()
    user = request.user.username
    calorie_goal = Calorie.objects.filter(user_name=user, type='Goal')
    calorie_current = Calorie.objects.filter(user_name=user, type='Current')

    context ['form'] = form
    context ['calorie_goal'] = calorie_goal
    context ['calorie_current'] = calorie_current
    context ['cal_goal_rows'] = len(calorie_goal)
    context ['cal_current_rows'] = len(calorie_current)
  
    return render(request, "myfitness/calories.html", context)

def calorieupdate(request):
    
    if request.method == 'POST':
        if 'save_goal' in request.POST or 'save_current' in request.POST:
            if 'save_goal' in request.POST:
                key = request.POST.get('save_goal')
            else:
                key = request.POST.get('save_current')   
            if not key:
                user = request.user.username
                if 'save_goal' in request.POST:
                    type = "Goal"
                else: 
                    type = "Current"
                cal = request.POST.get('calorie')
                protein = request.POST.get('protein')
                carbs = request.POST.get('carbs')
                fats = request.POST.get('fats')
                Calorie.objects.create(user_name=user, type=type , calorie=cal, protein=protein, carbs=carbs, fats=fats  )
            else:
                calorie = Calorie.objects.get(id=key)
                calorie.calorie = request.POST['calorie']
                calorie.protein = request.POST['protein']
                calorie.carbs = request.POST['carbs']
                calorie.fats = request.POST['fats']
                calorie.save()
        elif 'delete' in request.POST:
            key = request.POST.get('delete')
            calorie = Calorie.objects.get(id=key)
            calorie.delete()
        elif 'edit' in request.POST:
            key = request.POST.get('edit')
            calorie = Calorie.objects.get(id=key)
            form = CalorieForm(instance=calorie)
                                    
    if 'edit' in request.POST:
        context = {}
        user = request.user.username
        calorie_goal = Calorie.objects.filter(user_name=user, type='Goal')
        calorie_current = Calorie.objects.filter(user_name=user, type='Current')

        context ['form'] = form
        context ['calorie_goal'] = calorie_goal
        context ['calorie_current'] = calorie_current
        context ['cal_goal_rows'] = len(calorie_goal)
        context ['cal_current_rows'] = len(calorie_current)
        return render(request, "myfitness/calories.html", context)
    else:  
        return redirect(dashboard)
    
def weight(request):
    return render(request, "myfitness/weight.html")

def dashboard(request):
    context = {}
    user = request.user.username
    today = date.today()
    fitnesss = Fitness.objects.filter(user_name=user,date=today)
    context ['fitnesss'] = fitnesss

    calorie = Calorie.objects.filter(user_name=user)
    context ['calories'] = calorie

    return render(request, "myfitness/dashboard.html", context)




