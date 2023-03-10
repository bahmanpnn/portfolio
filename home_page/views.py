from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import ContactForm
from .models import Contact, Clients, Degrees, Experiences, Langueges, Portfolio, Skills, Services
from .models import User


# Create your views here.

class IndexPage(View):
    def get(self, request):
        form = ContactForm()
        clients = Clients.objects.all()
        degrees = Degrees.objects.all()
        experiences = Experiences.objects.all()
        langueges = Langueges.objects.all()
        portfolios = Portfolio.objects.all()
        skills = Skills.objects.order_by('-knowledge_percent_skill')
        services = Services.objects.all()
        user = User.objects.all().first()
        context = {
            'form': form,
            'user': user,
            'clients': clients,
            'degrees': degrees,
            'experiences': experiences,
            'langueges': langueges,
            'portfolios': portfolios,
            'skills': skills,
            'services': services,
        }
        return render(request, 'home_module/index.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone')
            text = form.cleaned_data.get('text')
            new_form = Contact(name=fullname,
                               email=email,
                               phone=phone_number,
                               text=text)
            new_form.save()
            return redirect(reverse('home_page_dark'))
        context = {
            'form': form
        }
        return render(request, 'home_module/index.html', context)


class IndexPageLight(View):
    def get(self, request):
        form = ContactForm()
        clients = Clients.objects.all()
        degrees = Degrees.objects.all()
        experiences = Experiences.objects.all()
        langueges = Langueges.objects.all()
        portfolios = Portfolio.objects.all()
        skills = Skills.objects.order_by('-knowledge_percent_skill')
        services = Services.objects.all()
        user = User.objects.all().first()
        context = {
            'form': form,
            'user': user,
            'clients': clients,
            'degrees': degrees,
            'experiences': experiences,
            'langueges': langueges,
            'portfolios': portfolios,
            'skills': skills,
            'services': services,
        }
        return render(request, 'home_module/index-light.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone')
            text = form.cleaned_data.get('text')
            new_form = Contact(name=fullname,
                               email=email,
                               phone=phone_number,
                               text=text)
            new_form.save()
            return redirect(reverse('home_page_light'))
        context = {
            'form': form
        }
        return render(request, 'home_module/index-light.html', context)
