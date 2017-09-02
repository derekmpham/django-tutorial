from django.forms import ModelForm
from models import Restaurant, Dish

class RestaurantForm(ModelForm):
	class Meta:
		model = Restaurant
		exclude ('user', 'date',)