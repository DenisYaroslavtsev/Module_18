from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_info(request):
    return render(request, 'func_templates.html')

class ClassTemplate(TemplateView):
    template_name = 'class_templates.html'