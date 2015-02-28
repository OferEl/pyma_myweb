from django.views.generic import TemplateView
#from django.shortcuts import render

class main_page(TemplateView):
    template_name = "main.html"
    #return render (request,"main.html")