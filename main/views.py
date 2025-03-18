from django.shortcuts import render, redirect
from django.contrib import messages

from main.models import Therapist, ContactMessage, Questionnaire

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def questionnaire(request):
    return render(request, 'questionnaire.html')

def therapist(request):
    return render(request, 'therapist.html')



def join_therapist(request):
    print("J'ebtre quand même ici")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        specialization = request.POST.get("specialization")
        message = request.POST.get("message")

        # Vérifier si l'email est déjà utilisé
        if Therapist.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered. Please use a different email.")
            return redirect("join_therapist")

        # Enregistrer un nouveau thérapeute
        Therapist.objects.create(
            name=name, 
            email=email, 
            phone=phone, 
            specialization=specialization, 
            message=message
        )

        messages.success(request, "Your request has been submitted successfully!")
        return redirect("join_therapist")

    return render(request, "therapist.html")


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your request has been submitted successfully!")
            return redirect("contact_submit")  # Redirection après envoi

    return render(request, "contact.html")



def questionnaire_view(request):
    if request.method == "POST":
        data = request.POST
        questionnaire = Questionnaire.objects.create(
            q1=data.get('q1'),
            q2=data.get('q2'),
            q3=data.get('q3'),
            q4=data.get('q4'),
            q5=data.get('q5'),
            q6=data.get('q6'),
            q7=data.get('q7'),
            q8=data.get('q8'),
            q9=data.get('q9'),
        )
        messages.success(request, "Your request has been submitted successfully!")
        return redirect("questionnaire_submit")  # Redirection après envoi

    return render(request, 'questionnaire.html')