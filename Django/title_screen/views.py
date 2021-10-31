from django.views.generic import TemplateView
from django.shortcuts import render

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
		return render(request, 'title_screen.html', 
		{
			'page_title': "Main page",
			'header': "Main page",
			'my_ref': "https://profile.intra.42.fr/",
			'left_key_act': "",
			'left_key_ref': "",
			'right_key_act': "",
			'right_key_ref': "",
			'up_key_act': "",
			'up_key_ref': "",
			'down_key_act': "",
			'down_key_ref': "",
			'select_key_act': "",
			'select_key_ref': "",
			'start_key_act': "",
			'start_key_ref': "",
			'a_key_act': "href=",
			'a_key_ref': "/worldmap",
			'b_key_act': "href=",
			'b_key_ref': "/load",
			'curr_page': "title_screen",
		})

#URL -> View -> Model (typically) -> Template