from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Share
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
	return render(request, 'base.html')

# def share_createview(request):
# 	template_name = 'shares/shares.html'
# 	context = {}
# 	return render(request, 'shares/form.html', context)


# def share_createview(request):
# 	if request.method == 'POST':
# 		form = ShareCreateForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponseRedirect('/thanks/')

# 	else:
# 		form = ShareCreateForm()

# 	return render(request, 'shares/form.html', {'form':form})



class ShareListView(ListView):
	queryset = Share.objects.all()
	template_name = 'shares/shares.html'
	context = {
		'name_share' : 'Уралкалий',
		'descript' : 'URLK',
	}



class SearchShareListView(ListView):

	def get_queryset(self):
		slug = self.kwargs.get('slug')
		queryset = Share.objects.filter(category=slug)
		return queryset


class ShareDetailView(DetailView):
	queryset = Share.objects.all()
	template_name = 'base.html'
	

	def get_context_data(self, *arg, **kwargs):
		print(self.kwargs)
		context = super(ShareDetailView, self).get_context_data(*arg, **kwargs)
		print(context)
		return context



# class BankShareListView(ListView):
# 	queryset = Share.objects.filter(name_share="Cбербанк")
# 	template_name = 'shares/shares_list.html'

# class TransportShareListView(ListView):
# 	queryset = Share.objects.filter(category="Транспорт")
# 	template_name = 'shares/shares_list.html'