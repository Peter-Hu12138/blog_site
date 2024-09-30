from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from .models import Member
from .forms import user_form


# This was mostly an archive for early exploration

def members(request: HttpRequest):
    mymembers = Member.objects.all().values()
    template = loader.get_template("memberlist.html")
    context = {
        'mymembers': mymembers,
    }
    return render(request, "memberlist.html", context)
    # old: return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))


def detailed_member_inventory(request: HttpRequest):
    template = loader.get_template('member_inventory.html')
    mymembers = Member.objects.all().values()
    context = {
        "members": mymembers
    }
    return HttpResponse(template.render(context, request))


def user_registration(request: HttpRequest):
    if request.method == "POST":
        form = user_form(request.POST)
        if form.is_valid():
            # TODO: try this with return HttpResponseRedirect("/thanks/")
            new_member = Member(firstname=form.cleaned_data['firstname'], lastname=form.cleaned_data['lastname'],
                                age=form.cleaned_data['age'], phone=form.cleaned_data['phone'])
            new_member.save()
            return HttpResponseRedirect("/user_registration/thanks/")
            # return render(HttpRequest(), "thanks.html", {})

    else:
        form = user_form()

    return render(request, "registration/user_registration.html", {"form": form})

def thanks(request):
    return render(request, 'thanks.html')


