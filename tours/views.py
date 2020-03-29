from django.shortcuts import render
from django.views import View
from tours.data import title, subtitle, description, departures, tours
from random import shuffle
# Create your views here.


class MainView(View):
    template_name = 'index.html'

    def get(self, request):
        r = [i for i in tours.keys()]
        shuffle(r)
        r = r[:6]
        tours_copy = {}
        for x in r:
            tours_copy[x] = tours[x]
        return render(request, self.template_name, {"title": title, "departures": departures, "subtitle": subtitle,
                                                    "description": description, "tours": tours_copy})


class DepartureView(View):
    template_name = 'departure.html'

    def get(self, request, departure_id):
        tour_copy = {}
        min_price = 50000000
        max_price = 0
        min_days = 100000
        max_days = 0
        count = 0
        for key, value in tours.items():
            if value['departure'] == departure_id:
                tour_copy[key] = tours[key]
                count += 1
                min_days = min(min_days, tours[key]['nights'])
                max_days = max(max_days, tours[key]['nights'])
                min_price = min(min_price, tours[key]['price'])
                max_price = max(max_price, tours[key]['price'])
        t_t = 'тур'
        if (20 >= count >= 10) or ((count % 10) in [0, 5, 6, 7, 8, 9]):
            t_t += 'ов'
        elif (count % 10) in [2, 3, 4]:
            t_t += 'а'
        return render(request, self.template_name, {"title": title, "departures": departures,
                                                    "current": departures[departure_id],
                                                    "tours": tour_copy, "count": count,
                                                    "min_price": min_price, "max_price": max_price, 't_t': t_t,
                                                    "min_days": min_days, "max_days": max_days})


class TourView(View):
    template_name = 'tour.html'

    def get(self, request, tour_id):

        return render(request, self.template_name, {"title": title, "departures": departures, "dep": departures[tours[tour_id]['departure']], "tour": tours[tour_id]})
