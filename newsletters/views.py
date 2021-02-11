from django.shortcuts import render
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm


#newsletter signup view
def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("Sorry! this email already exist")
        else:
            instance.save()

    context = {
        'form': form,

    }
    template = "newsletters/sign_up.html"

    return render(request, template, context)

#newsletter unsubscribe views
def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()

        else:
            print('sorry! we did not find your email address')
            
        context = {
            "form": form,
        }
        template = "newsletters/unsubscribe.html"

        return render(request, template, context)
