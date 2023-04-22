import flet as ft
from register_flight import FlightRegistration

def main(page: ft.Page):
	page.title = "Airlines Management System"
	page.theme_mode = "light"
	page.horizontal_alignment = "center"
	page.vertical_alignment = "center"
	page.scroll = "always"

	page.appbar = ft.AppBar(
		leading=ft.Row([ft.Container(width=4),ft.Image(src="logo/airplane.png",width=50)]),
		leading_width=60,
		title=ft.Text("Airlines Management System",color="#FFFFFF"),
		center_title=False,
		bgcolor=ft.colors.BLUE_900,
		actions=[
			ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,icon_color=ft.colors.WHITE),
			ft.IconButton(ft.icons.FILTER_3,icon_color=ft.colors.WHITE),
			ft.Container(width=10)
		],
	)

	# creating the instance of FlightRegistration class
	flightRegistration = FlightRegistration()

	page.add(
		flightRegistration
	)

ft.app(target=main,assets_dir="assets")