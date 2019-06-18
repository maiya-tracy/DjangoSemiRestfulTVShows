from django.shortcuts import render, HttpResponse, redirect
from .models import Show
import datetime


def index(request):
    return redirect("/shows")


def shows(request):
    context = {
        'all_shows': Show.objects.all(),
    }
    return render(request, 'tvshows/all_shows.html', context)


def display_show(request, showid):
    context = {
        'show': Show.objects.get(id=showid),
    }
    return render(request, 'tvshows/display_show.html', context)


def new_show(request):
    return render(request, 'tvshows/new_show.html')


def edit_show(request, showid):
    edited_release_date = Show.objects.get(id=showid).release_date.strftime("%Y-%m-%d")
    context = {
        'show': Show.objects.get(id=showid),
        "release_date": edited_release_date,
    }
    return render(request, 'tvshows/edit_show.html', context)


def addShowToDB(request):
    DBtitle = request.POST["form_title"]
    DBnetwork = request.POST["form_network"]
    DBrelease_date = request.POST["form_release_date"]
    DBdescription = request.POST["form_description"]
    new_show = Show.objects.create(
        title=DBtitle, network=DBnetwork, release_date=DBrelease_date, description=DBdescription)
    return redirect("/shows/" + str(new_show.id))


def editShowtoDB(request, showid):
    DBtitle = request.POST["form_title"]
    DBnetwork = request.POST["form_network"]
    DBrelease_date = request.POST["form_release_date"]
    DBdescription = request.POST["form_description"]
    show_to_edit = Show.objects.get(id=showid)
    show_to_edit.title = DBtitle
    show_to_edit.network = DBnetwork
    show_to_edit.release_date = DBrelease_date
    show_to_edit.description = DBdescription
    show_to_edit.save()
    return redirect("/shows/" + str(showid))


def delete_show(request, showid):
    show_to_delete = Show.objects.get(id=showid)
    show_to_delete.delete()
    return redirect("/shows")
