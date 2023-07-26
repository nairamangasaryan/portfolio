from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Skill,
    Education,
    Experience,
    Language,
    HardSkill,
    SoftSkill,
    SocialLink,
    Personal_info,
    Facts,
    Service,
    Testimonial,
    PortfolioProject,
)
from django.views.generic import DetailView
from .forms import MassageForm

# Create your views here.


def home(request):

    if request.method == "POST":
        form = MassageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/#contact")

    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    languages = Language.objects.all()
    soft_skills = SoftSkill.objects.all()
    hard_skills = HardSkill.objects.all()
    social_links = SocialLink.objects.all()
    personal_info = Personal_info.objects.first()
    facts = Facts.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    portfolio_project = PortfolioProject.objects.all()
    massageForm = MassageForm()

    data = {
        "skills": skills,
        "educations": educations,
        "experiences": experiences,
        "languages": languages,
        "soft_skills": soft_skills,
        "hard_skills": hard_skills,
        "social_links": social_links,
        "personal_info": personal_info,
        "facts": facts,
        "services": services,
        "testimonials": testimonials,
        "portfolio_project": portfolio_project,
        "massageForm": massageForm
    }

    return render(request, "home.html", context=data)


def portfolio_project(request, pk):
    project = get_object_or_404(PortfolioProject, id=pk)
    return render(request, "portfolio_details.html", context={"project": project})
