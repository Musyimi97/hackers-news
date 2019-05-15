from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from links.models import Link

# Create your views here.
