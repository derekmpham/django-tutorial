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
		name='dish_detail'),

# Create a restaurant
	url(r'\^restaurants/create/\$',
		RestaurantCreate.as_view(),
		name='restaurant_create'),

# Edit restaurant details
	url(r'\^restaurants/(?P<pk>\d+)/edit/\$',
		UpdateView.as_view(
			model = Restaurant,
			template_name = 'myrestaurants/form.html',
			form_class = RestaurantForm),
		name='restaurant_edit'),

# Create a restaurant dish
	url(r'\^restaurants/(?P<pk>\\d+)/dishes/create/\$',
		DishCreate.as_view(),
		name='dish_create'),

# Edit restaurant dish details
	url(r'\^restaurants/(?P<pkr>\\d+)/dishes/(?P<pk>\\d+)/edit/\$',
		UpdateView.as_view(
			model = Dish,
			template_name = 'myrestaurants/form.html',
			form_class = DishForm),
		name='dish_edit'),

# Create restaurant review
	url(r'\^restaurants/(?P<pk>\\d+)/reviews/create/\$',
		'myrestaurants.views.review',
		name='review_create'),

]
