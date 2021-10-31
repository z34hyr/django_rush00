from django.views.generic import TemplateView
from django.shortcuts import render
from worldmap.views import gamer

class Gamer:
	"""класс про игрока"""
	def __init__(self) -> None:
		self.pos_x = 0
		self.pos_y = 0
		self.balls = 0


class TitlePageView(TemplateView):
	template_name = "base.html"

	def page(request):
		print(request)
		page = "title_screen.html"
		z = "title_screen"
		if request.method == 'POST':
			# если POST - значит нажатие на кнопку
			key = request.POST.get("key")
			if key == "a":
				page = "table.html"
				z = "worldmap"
			else:
				page = "title_screen.html"
				z = "title_screen"
		return render(request, page, 
		{
			'page_title': "Main page",
			'header': "Main page",
			'curr_page': z,
			'rows': gamer.field
		})

#URL -> View -> Model (typically) -> Template