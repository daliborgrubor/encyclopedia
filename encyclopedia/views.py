from django.shortcuts import render
from . import util
from markdown2 import Markdown
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def add(request):
    if request.method == "GET":
        return render(request, "encyclopedia/add.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        title_exists = util.get_entry(title)
        if title_exists is not None:
            return render(request, "encyclopedia/error.html", {
                "error_message" : "Encyclopedia page already exists."
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                'title' : title,
                'content' : html_content
            })

def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title" : title,
            "content" : content
        })

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "error_message" : "The requested page was not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "content" : html_content
        })

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    html_content = convert_md_to_html(random_entry)
    return render(request, "encyclopedia/entry.html", {
        "title" : random_entry,
        "content" : html_content
    })

def save(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            'title' : title,
            'content' : html_content
        })

def search(request):
    if request.method == "POST":
        search_entry = request.POST['q']
        entry_data = convert_md_to_html(search_entry)
        if entry_data is not None:
            return render(request, "encyclopedia/entry.html", {
                "title" : entry_data, 
                "content" : entry_data
            })
        else:
            entries = util.list_entries()
            suggestion = []
            for entry in entries:
                if search_entry.lower() in entry.lower():
                    suggestion.append(entry)
            return render(request, "encyclopedia/search.html", {
                "suggestion" : suggestion
        })
