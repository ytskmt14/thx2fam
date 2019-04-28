from django.shortcuts import render
from django.views import View

# Create your views here.
class TopView(View):
  def get(self, request, *args, **kwargs):
    context = {
      'message': "Hello World!",
    }
    return render(request, 'arapp/top.html', context)

top = TopView.as_view()