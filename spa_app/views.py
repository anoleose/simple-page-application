from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .models import FoodStore
from django.db.models import Q





def index(request):
	foodstore = FoodStore.objects.all()
	items_by_page = Paginator(foodstore, 3)
	page_obj_list = items_by_page.page(1).object_list
	pagerange = items_by_page.page_range
	

	if request.method == "POST":
		page_n = request.POST.get('page_n', None)
		print(page_n)
		page_n = page_n.strip('?page=')
		results = list(items_by_page.page(page_n).object_list.values('id', 'title', 'quantity', 'distance', 'meter'))
		return JsonResponse({"results":results})
		

	context = {
		'items_by_page':items_by_page,
		'page_obj_list':page_obj_list,
		'pagerange': pagerange,
		
	}



	template = loader.get_template('spa_app/index.html')
	return HttpResponse(template.render(context, request))


def filtering (request):
	try:
		query = request.POST.get("search")
	except:
		query:None
	if request.method == 'POST':
		query = request.POST.get("search")
		if query:
			foodstore = FoodStore.objects.filter(
				Q(title__icontains=query)| 
				Q(quantity__icontains=query)| 
				Q(distance__icontains=query)| 
				Q(meter__icontains=query)).distinct()	
			results = list(foodstore.values('id', 'title', 'quantity', 'distance', 'meter'))
			return JsonResponse({"results":results}, status = 200)
			
		return HttpResponse(query)


	



	