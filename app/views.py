from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Snikers, Choice

class IndexView(generic.ListView):
    template_name = 'app/main_index.html'
    context_object_name = 'latest_snikers_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Snikers.objects.order_by('id')



# def detail(request, snikers_id):
#     snikers = get_object_or_404(Snikers, pk=snikers_id)
#     return render(request, 'app/detail.html', {'snikers': snikers})
#
#
# def results(request, snikers_id):
#     snikers = get_object_or_404(Snikers, pk=snikers_id)
#     return render(request, 'app/result.html', {'question': snikers})

class DetailView(generic.DetailView):
    model = Snikers
    template_name = 'app/detail.html'


class ResultsView(generic.DetailView):
    model = Snikers
    template_name = 'app/result.html'

def vote(request, snikers_id):
    sniker = get_object_or_404(Snikers, pk=snikers_id)
    try:
        selected_choice = sniker.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app/detail.html', {
            'sniker': sniker,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app:results', args=(sniker.id,)))