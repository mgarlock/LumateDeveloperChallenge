from django.views.generic import ListView
from guestBook.models import GuestLog
from django.shortcuts import render_to_response
from forms import GuestLogForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

class GuestList(ListView):
  model = GuestLog
  context_object_name = 'guest_log_list'
  def get_queryset(self):
    return GuestLog.objects.order_by('-access_date')

def get_client_ip(request):
  x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
  if x_forwarded_for:
     ip = x_forwarded_for.split(',')[-1].strip()
  else:
     ip = request.META.get('REMOTE_ADDR')
  return ip

def create(request):
  if request.POST:
    form = GuestLogForm(request.POST)
    if form.is_valid():
      print form
      newLog = form.save(commit=False)
      newLog.ip_address = get_client_ip(request)
      newLog.save()
      return HttpResponseRedirect('/log/')
  else:
    form = GuestLogForm()
                                
  args = {}
  args.update(csrf(request))
  args['form'] = form                                      
  return render_to_response('guestBook/create_log.html', args)
                                                
