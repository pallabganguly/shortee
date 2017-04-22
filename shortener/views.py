from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import UrlShort
from .forms import SubmitUrlForm

# Create your views here.

#these views handle URLs
# when this views are called it does something like render a template, or some static page or something else
# def redirect_view(request, shortcode=None, *args, **kwargs): # function based   recieve the shortcode passed as keyword argument!
#     # print(shortcode)
#     obj = get_object_or_404(UrlShort, shortcode=shortcode) # query db model for record using passed shortcode. if not found raise 404 error
#     # try:
#     #     obj = UrlShort.objects.get(shortcode=shortcode)
#     # except:
#     #     obj = UrlShort.objects.all().first()
#     return HttpResponseRedirect(obj.url)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "title": "Shortee",
            "form": form
        }
        return render(request, 'shortener/home.html', context)   # context-dictionary which is passed to home.html

    def post(self, request, *args, **kwargs):   # define how to handle post method
        # print(request.POST.get("url"))
        form = SubmitUrlForm(request.POST)  # get its POST data
        if form.is_valid():
            submitted_url = form.cleaned_data.get("url")
            obj, created = UrlShort.objects.get_or_create(url=submitted_url)    # insert into database and return result of insert
            submittedcontext = {
                "object": obj,
                "created": created,
            }
            if created:
                return render(request, 'shortener/success.html', submittedcontext)
            else:
                return render(request, 'shortener/exists.html', submittedcontext)

        context = {
            "title": "Shortee",
            "form": form
        }
        return render(request, 'shortener/home.html', context)

class RedirectCBView(View): # class based
    def get(self, request, shortcode=None, *args, **kwargs):    # specifies how to handle GET method
        # print(shortcode)
        obj = get_object_or_404(UrlShort, shortcode=shortcode)  # query db model for record using passed shortcode. if not found raise 404 error
        return HttpResponseRedirect(obj.url)
