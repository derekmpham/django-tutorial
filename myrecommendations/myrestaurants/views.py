# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from models import RestaurantReview, Restaurant, Dish
from forms import RestaurantForm, DishForm

# Create your views here.
class RestaurantDetail(DetailView):
	model = Restaurant
	template_name = 'myrestaurants/restaurant_detail.html'

	def get_context_data(self, **kwargs):
		context = super(RestaurantDetail, self).get_context_data(**kwargs)
		context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
		return context


class RestaurantCreate(CreateView):
	model = Restaurant
	template_name = 'myrestaurants/form.html'
	form_class = RestaurantForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(RestaurantCreate, self).form_valid(form)





















