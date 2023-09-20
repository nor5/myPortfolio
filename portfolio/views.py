import mimetypes
import os
from pathlib import Path

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Blogs, Education, Projects, Skills, WorkExperiences


# Create your views here.
def mainPage(request):
    skills = Skills.objects
    educations = Education.objects
    workExperiences = WorkExperiences.objects
    projects = Projects.objects
    blogs = Blogs.objects

    # email sending
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]

            message1 = (
                "you got an e-mail from:\n" + name + "\n" + from_email + "\n" + message
            )
            try:
                # send_mail(subject, message, "noorbelkacem5@gmail.com",[from_email] )
                send_mail(subject, message1, from_email, ["noorsaoudi55@gmail.com"])

            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect(mainPage)

    return render(
        request,
        "index.html",
        {
            "skills": skills,
            "educations": educations,
            "workExperiences": workExperiences,
            "projects": projects,
            "blogs": blogs,
            "form": form,
        },
    )


def download_file(request):
    # fl_path = "/home/nour/Documents/nourPortfolio/portfolio/static/CV_2022-12-24_NourElhouda_Belkacem.pdf"
    filename = "static/CV_Nour_Elhouda_Belkacem.pdf"

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    fl_path = os.path.join(BASE_DIR, filename)

    fl = open(fl_path, "rb")
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response["Content-Disposition"] = "attachment; filename=%s" % filename
    return response
