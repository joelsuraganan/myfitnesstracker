from django.urls import path
from myfitness import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("faq/", views.faq, name="faq"),
    path("nutrition/", views.nutrition, name="nutrition"),
    path("workouts/", views.workouts, name="workouts"),
    path("supplements/", views.supplements, name="supplements"),
    path("", views.home, name="home"),
    path("myfitness/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("workouttracker/", views.workouttracker, name="workouttracker"),
    path("workoutupdate/", views.workoutupdate, name="workoutupdate"),
    path("calories/", views.calories, name="calories"),
    path("calorieupdate/", views.calorieupdate, name="calorieupdate"), 
    path("weight/", views.weight, name="weight"),
    path("weightupdate/", views.weightupdate, name="weightupdate"),
    path("logout/", views.logout, name="logout"),
]