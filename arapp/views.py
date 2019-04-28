from django.shortcuts import render
from django.views import View

# Create your views here.
class HelloView(View):
  def get(self, request, *args, **kwargs):
    context = {
      'message': "Hello World!",
    }
    return render(request, 'arapp/hello.html', context)

hello = HelloView.as_view()