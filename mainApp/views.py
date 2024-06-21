from django.shortcuts import render

def home(Request):
    return render(Request,"index.html")

def aboutPage(Request):
    return render(Request,"about.html")

def image(Request):
    return render(Request,"image.html")
