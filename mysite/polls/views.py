from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from django.shortcuts import render, redirect,render_to_response
from django.template import loader
from .models import Question
from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def index(request):
#     print "=checking="
#     context = { 'Arun' : 'Arun' }
#     return HttpResponse("Hello, world.")
#     # return render_to_response('about_us.html',context)

class AboutUsView(TemplateView):
    template_name = 'polls/index.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        print " now():", now()
        print " now().weekday():", now().weekday()
        print " now().hour:", now().hour
        if now().weekday() < 5 and 8 < now().hour < 18:
            context['open'] = True
        else:
            context['open'] = False
        return context

class ContactView(FormView):
    # form_class = ContactForm
    template_name = 'polls/contact.html'

class SecretView(LoginRequiredMixin, TemplateView):
    template_name = "secret.html"

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
