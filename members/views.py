from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Member


# This was mostly an archive for early exploration

def members(request: HttpRequest):
    mymembers = Member.objects.all().values()
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
    return HttpResponse(template.render({}, request))


def testing(request):
  mydata = Member.objects.all.values()
  template = loader.get_template('testing.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


def detailed_member_inventory(request: HttpRequest):
    template = loader.get_template('member_inventory.html')
    mymembers = Member.objects.all().values()
    context = {
        "members": mymembers
    }
    return HttpResponse(template.render(context, request))


def thanks(request):
    return render(request, 'thanks.html')
