from encyclopedia.models import Note, Paper
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from random import choice
from django.urls import reverse
import re

from .forms import NewPaperForm, SubjectPaperForm, SearchPaperForm, NewNotesForm

from . import util
import encyclopedia


def index(request):
    titles = Note.objects.values_list('title', flat=True)
    return render(request, "encyclopedia/index.html", {
        "titles": titles
    })          


def addnotes(request):
    if request.method == "POST":
        form = request.POST
        title = form["title"]
        subject =  form["subject"]
        source = form["source"]
        file_url = form["file_url"]
        your_name = form["your_name"]

        note = Note(title=title, subject=subject, source=source, your_name=your_name, file_url=file_url)
        note.save()

        return render(request, "encyclopedia/notes.html", {
            "note": note,
            "message": "Notes saved successfully!"
        })

    else:
        return render(request, "encyclopedia/addnotes.html", {
            "form": NewNotesForm
        })


def search(request):
    if request.method == "POST":
        form = request.POST
        title =  form["q"]
        
        # Getting all titles from database and search which title matches to the query
        notes = []
        entries = Note.objects.all()
        for entry in entries:
            if re.search(title, entry.title, re.IGNORECASE):
                notes.append(entry)
                # Get this entry and append into list of objects                
        return render(request, "encyclopedia/notes.html", {
            "notes": notes,
            "message": "Search Results:"
        })
    else:
        return redirect('index')


      
#####
def paperhome(request):
    return render(request, "encyclopedia/paperhome.html")


def searchpaper(request):
    if request.method == "POST":
        form = request.POST
        subject =  form["subject"]
        category = form["category"]
        year = int(form["year"])  

        # Check if that entry exists
        if Paper.objects.filter(subject=subject, category=category, year=year).exists():
             
            # It  exists
            paper = Paper.objects.get(subject=subject, category=category, year=year)
            return render(request, "encyclopedia/paper.html", {
                "paper": paper,
                "message": "Paper Found!"
            })
        else:
            # Entry does not exist
            return render(request, "encyclopedia/error.html", {
                "message": "Requested paper do not exist."
            })

    else:
        return render(request, "encyclopedia/searchpaper.html", {
            "form": SearchPaperForm
        })


def subjectpapers(request):
    if request.method == "POST":
        form = request.POST
        subject =  form["subject"] 

        papers = Paper.objects.filter(subject=subject).order_by('-year')
        return render(request, "encyclopedia/subjectpaper.html", {
            "papers": papers
        })
    else:
        return render(request, "encyclopedia/searchsubjectpaper.html", {
            "form": SubjectPaperForm
        })
    

def  addpaper(request):
    if request.method == "POST":
        form = request.POST
        title = form["title"]
        subject =  form["subject"]
        category = form["category"]
        year = int(form["year"])
        file_url = form["file_url"]
        your_name = form["your_name"]

        # Check if that entry exists
        if Paper.objects.filter(subject=subject, category=category, year=year).exists():
             
            # It  exists
            return render(request, "encyclopedia/error.html", {
                "message": "Thank You for your efforts but this paper already exist."
            })

        else:        
            paper = Paper(subject=subject, category=category, year=year, title=title, file_url=file_url, uploader=your_name)
            paper.save()
            return render(request, "encyclopedia/paper.html", {
                "message": "Paper added successfully!",
                "paper": paper

            })

    else:
        return render(request, "encyclopedia/addpaper.html", {
            "form" : NewPaperForm
        })




def contact(request):
    return render(request, "encyclopedia/contact.html")
