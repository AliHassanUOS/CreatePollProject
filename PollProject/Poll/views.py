from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



def home(request):
    polls = Poll.objects.all()

    context = {

        'polls': polls
    }
    return render(request, 'Poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    else:
        form = CreatePollForm()
    context = {

        'form': form
    }
    return render(request, 'Poll/create.html', context)
#@method_decorator(login_required, name="dispatch")
def results(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'Poll/results.html', context)

def vote(request,poll_id):
    polls = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option=(request.POST['poll'])
        if selected_option == 'option1':
            polls.option_one_count += 1
        elif selected_option == 'option2':
            polls.option_two_count += 1
        elif selected_option == 'option3':
            polls.option_three_count += 1
        else:
            return  HttpResponse(400,'Invalid Form')
        polls.save()
        return redirect('results', polls.id)

    context =  {

        'polls': polls
    }
    return render(request, 'Poll/vote.html', context)



def delete_data(request, id):
    if request.method == 'POST':
        dl = Poll.objects.get(pk=id)
        dl.delete()
        return redirect('/')