from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from random import choice
from django.urls import reverse
import re


from . import util
import encyclopedia


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    result = util.get_entry(title)
    if result == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page do not exist"
        })

    else:
        return render(request, "encyclopedia/entry.html", {
            "message": util.convert(result),
            "title": title
        })


def search(request):
    if request.method == "POST":
        form = request.POST
        title =  form["q"]
        result = util.get_entry(title)
        if result:
            return redirect('wiki/'+title)
        else:
            results = []
            entries = util.list_entries()
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

        # Checking if page already exist or not
        result = util.get_entry(title)

        if result == None:
            util.save_entry(title, content)
            return redirect('wiki/'+title)
        else:
            return render(request, "encyclopedia/error.html", {
                "message": "Page already exist",
                "title": title
            })
    else:
        return render(request, "encyclopedia/add.html")
            

def edit(request, title):
    if request.method == "POST":
        form = request.POST
        content = form["content"]       
        util.save_entry(title, content)                
        return HttpResponseRedirect(reverse("wiki", args=(title,)))
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "message": content,
            "title": title
        })


def random(request):
    # Get a random title from list of entries
    title = choice(util.list_entries())
    return redirect('wiki/'+title)
      