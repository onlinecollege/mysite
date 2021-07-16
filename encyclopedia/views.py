from encyclopedia.models import Note
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from random import choice
from django.urls import reverse
import re

from . import util
import encyclopedia


def index(request):
    titles = Note.objects.values_list('title', flat=True)
    return render(request, "encyclopedia/index.html", {
        "titles": titles
    })


def library(request, title):
    try:
        note = Note.objects.get(title=title)
    except Note.DoesNotExist:
        note = None

    if note == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page do not exist"
        })

    else:
        content = note.content
        return render(request, "encyclopedia/entry.html", {
            "content": util.convert(content),
            "note": note
        })


def search(request):
    if request.method == "POST":
        form = request.POST
        title =  form["q"]

        try:
            result = Note.objects.get(title=title)
        except Note.DoesNotExist:
            result = None
        if result is not None:
            return redirect('library/'+title)
        else:
            results = []
            entries = Note.objects.values_list('title', flat=True)
            for entry in entries:
                if re.search(title, entry, re.IGNORECASE):
                    results.append(entry)                
            return render(request, "encyclopedia/search.html", {
                "results": results
            })
    else:
        return redirect('index')


def add(request):
    if request.method == "POST":
        form = request.POST
        title = form["title"]
        content = form["content"]
        name = form["name"]

        # Checking if page already exist or not
        try:
            result = Note.objects.get(title=title)
        except Note.DoesNotExist:
            result = None

        if result == None:
            note = Note(title=title, content=content, name=name)
            note.save()
            return redirect('library/'+title)
        else:
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exist",
                "title": title
            })
    else:
        return render(request, "encyclopedia/add.html")
            

def edit(request, title):
    if request.method == "POST":
        # Deleting previous entry
        note = Note.objects.get(title=title)
        note.delete()

        #Saving new entry
        form = request.POST
        content = form["content"]   
        title = form["title"]    
        name = form["name"]
        note = Note(title=title, content=content, name=name)  
        note.save()             
        return HttpResponseRedirect(reverse("library", args=(title,)))
    else:
        note = Note.objects.get(title=title)
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "note": note
        })


def guide(request):
    return render(request, "encyclopedia/guide.html")
      

def allpapers(request):
    return render(request, "encyclopedia/allpaper.html")


def subjectpapers(request, subject):
    return render(request, "encyclopedia/subjectpaper.html")


def papers(request, paper_id):
    return render(request, "encyclopedia/paper.html")