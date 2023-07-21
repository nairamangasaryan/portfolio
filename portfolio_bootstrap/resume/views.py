from django.shortcuts import render, redirect
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
    PortfolioDetails,
    UserInfo
)
from django.views.generic import DetailView
from .forms import MassageForm
# Create your views here.


def home(request):

    if request.method == "POST":
        print("POSTED DATA")
        form = MassageForm(request.POST)
        if form.is_valid():
            print("NEED TO SAVE")
            form.save()
            return redirect("/")

        else:
            error = "THE SEND MASSAGE IS INCORRECT"

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
    portfolio_details = PortfolioDetails.objects.all()
    user_info = UserInfo.objects.get(user__username="naira")
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
        "portfolio_details": portfolio_details,
        "user_info": user_info,
        "massageForm": massageForm
    }

    return render(request, "home.html", context=data)


def portfolio_details(request):
    return render(request, "portfolio_details.html")


class PortfolioDetailView(DetailView):
    model = PortfolioDetails
    template_name = 'portfolio_details.html'
    context_object_name = 'project'
