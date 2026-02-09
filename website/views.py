from django.shortcuts import render, get_object_or_404
from .models import SiteSettings, Program, TeamMember, AboutContent, Contact, MentorshipPhilosophy
from blog.models import BlogPost


def home(request):
    settings = SiteSettings.objects.first()
    programs = Program.objects.all()[:3]
    return render(request, 'home.html', {
        'settings': settings,
        'programs': programs
    })

def about(request):
    site = SiteSettings.objects.first()
    about_content = AboutContent.objects.first()

    return render(request, 'about.html', {
        'site': site,
        'about_content': about_content
    })

def programs(request):
    programs = Program.objects.filter(is_active=True)
    return render(request, "programs.html", {
        "programs": programs
    })


def team(request):
    leadership = TeamMember.objects.filter(role='leadership')
    advisors = TeamMember.objects.filter(role='advisor')
    mentors = TeamMember.objects.filter(role='mentor')
    philosophy = MentorshipPhilosophy.objects.first()

    return render(request, 'team.html', {
        'leadership': leadership,
        'advisors': advisors,
        'mentors': mentors,
        'philosophy': philosophy,
    })

def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'blog_detail.html', {'post': post})


def contact(request):
    site = SiteSettings.objects.first()
    contact = Contact.objects.first()

    return render(request, 'contact.html', {
        'site': site,
        'about': contact
    })
