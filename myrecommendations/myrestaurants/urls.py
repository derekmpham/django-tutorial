from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Restaurant, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantCreate, DishCreate, RestaurantDetail

urlpatterns = [

# List latest 5 restaurants: /myrestaurants/
	url(r'\^\$',
		ListView.as_view(
			queryset=Restaurant.objects.filter(date_lte=timezone.now()).order_by('date')[:5],
			context_object_name='latest_restaurant_list',
			template_name='myrestaurants/restaurant_list.html'),
		name='restaurant_list'),

# Restaurant details
	url(r'\^restaurants/(?P<pk>\d+)/\$',
		RestaurantDetail.as_view(),
		name='restaurant_detail'),

# Restaurant dish details
	url(r'\^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/\$',
		DetailView.as_view(
			model=Dish,
			plate_name='myrestaurants/dish_detail.html'),
		name='dish_detail')

]