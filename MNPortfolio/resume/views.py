from django.shortcuts import render
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
    Testimonial
)

# Create your views here.


def home(request):
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

    }

    return render(request, "home.html", context=data)
