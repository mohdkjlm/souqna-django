from django.shortcuts import render, redirect
from .models import Profils
from .forms import Signupform, ProfilrForms, UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def signup(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            owner_group = Group.objects.get(name="owner")
            user.groups.add(owner_group)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/accounts/prof")

    else:
        form = Signupform()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def prof(request):
    prof = Profils.objects.get(user=request.user)
    return render(request, "profile.html", {"prof": prof})


@login_required
def profile_edit(request):
    prof = Profils.objects.get(user=request.user)

    if request.method == "POST":
        userform = UserForm(request.POST, instance=request.user)
        profile_form = ProfilrForms(request.POST, instance=prof)

        if userform.is_valid() and profile_form.is_valid():
            userform.save()
            profile_form.save()
            return redirect("/accounts/prof")

    else:
        userform = UserForm(instance=request.user)
        profile_form = ProfilrForms(instance=prof)

    return render(
        request,
        "profile_edit.html",
        {"userform": userform, "profile_form": profile_form},
    )


@login_required
def logout_user(request):
    logout(request)
    return redirect("login")
