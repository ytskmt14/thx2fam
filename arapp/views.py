from django.shortcuts import render
from django.views import View

# Create your views here.
class TopView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'arapp/top.html')

class MotherDayView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'arapp/mom.html')

top = TopView.as_view()
mother = MotherDayView.as_view()
