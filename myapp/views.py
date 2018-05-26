from django.shortcuts import render
from django.db.models import Count, Q
from .models import Passenger
import json

def ticket_class_view(request):
	dataset = Passenger.objects.values('ticket_class').annotate(survived_count=Count('ticket_class', filter=Q(survived=True)), not_survived_count=Count('ticket_class', filter=Q(survived=False))).order_by('ticket_class')

	categories = list()
	survived_series = list()
	not_survived_series = list()

	for entry in dataset:
		categories.append('%s Class' %entry['ticket_class'])
		survived_series.append(entry['survived_count'])
		not_survived_series.append(entry['not_survived_count'])

	return render(request, 'myapp/index_2.html', {
			'categories': json.dumps(categories),
			'survived_series': json.dumps(survived_series),
			'not_survived_series': json.dumps(not_survived_series)
		})