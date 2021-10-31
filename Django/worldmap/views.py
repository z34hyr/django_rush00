from django.http import request
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
import random

class GameField:
	def __init__(self, size=14, n_balls=30, n_films=30) -> None:
		self.size = size # количество ячеек по горизонтали (поле квадратное)
		self.total_balls = n_balls # количество покеболов на поле
		self.total_films = n_films # количество фильмов на поле
		self.field = []
		for _ in range(self.size):
			row = []
			for _ in range(self.size):
				row.append("silver")
			self.field.append(row)
	def place_items(self):
		"""здесь рандомно раскидываем элементы по карте и запоминаем где что лежит"""
		pass


class Gamer(GameField):
	"""класс про игрока"""
	def __init__(self, pos_x: int = 5, pos_y: int = 5, balls: int = 0, films_opened: int = 0) -> None:
		super().__init__() # иницииализируем тут же класс GameField чтобы работать с один классом
		self.pos_x = pos_x  #  текущая позиция по вертикали
		self.pos_y = pos_y  #  текуая позиция по горизонтали
		self.balls = balls  #  сейчас покеболов
		self.films_opened = films_opened  #  открыто фильмов
		self.hero_color = "blue"
		self.change_position(pos_x, pos_y)
		print("CLASS Gamer initiated")

	def move_hero(self, way: str):
		"""фунция для перемещения героя на карте
		'up' -> запрос на движение вверх
		'down', 'left', 'right'
		"""
		dirs = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
		if way in dirs:
			if  0 <= dirs[way][0] + self.pos_x <= self.size - 1 and \
			0 <= dirs[way][1] + self.pos_y <= self.size -1:
				self.field[self.pos_x][self.pos_y] = "green"
				self.pos_x += dirs[way][0]
				self.pos_y += dirs[way][1]
				self.field[self.pos_x][self.pos_y] = self.hero_color
		# далее надо обработать случаи когда мы наткнулись на покебол или на монстра
		# просто меняем надпись настранице - найден покебол и\или монстр

	def change_position(self, new_x, new_y):
		self.field[new_x][new_y] = self.hero_color

gamer = Gamer()

class WorldMapView(TemplateView):

	template_name = "base.html"
	def page(request):
		print(request)
		global gamer
		
		print("BALLS:", gamer.total_balls)
		page = "table.html"
		z = "worldmap"
		if request.method == 'POST':
			# если POST - значит нажатие на кнопку
			key = request.POST.get("key")
			if key in {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}:
				gamer.move_hero(key)
			if key == "a":
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