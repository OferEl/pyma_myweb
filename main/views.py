from django.views.generic import TemplateView
#from django.shortcuts import render

class main_page(TemplateView):
    template_name = "main.html"
    
#    def get_context_data(self, kwargs):
#        context = super(main_page, self).get_context_data(self,kwargs)
#        return context

    #return render (request,"main.html")