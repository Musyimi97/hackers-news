from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from links.models import Link

# Create your views here.
class NewSubmissionView(object):
    model= Link
    fields=('title','url')
    template_name='new_submission.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewSubmissionView,self).dipatch(*args,**kwargs)

    def form_valid(self, form):
        new_link=form.save(commit=False),
        new_link.submitted_by=self.request.user
        new_link.save()

        self.object = new_link
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse('home')