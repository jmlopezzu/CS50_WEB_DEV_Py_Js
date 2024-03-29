from django.shortcuts import render

tasks = ["Swim","Bike","Run","Yoga","Meditate","Read","Write","Code","Sleep","Eat","Drink"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })