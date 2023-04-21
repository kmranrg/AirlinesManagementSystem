import flet as ft

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

	airplane_name = ft.TextField(hint_text="airplane name",width=300,border_radius=25)
	airplane_serialCode = ft.TextField(hint_text="airplane serial code",width=300,border_radius=25)
	airplane_model = ft.TextField(hint_text="airplane model",width=300,border_radius=25)
	start_country = ft.TextField(hint_text="start country",width=300,border_radius=25)
	end_country = ft.TextField(hint_text="end country",width=300,border_radius=25)
	time_duration = ft.TextField(hint_text="time duration",width=300,border_radius=25)
	submit_flight = ft.ElevatedButton("Submit Flight")

	flight_form = ft.Column([ft.Container(height=10),airplane_name,airplane_serialCode,airplane_model,start_country,end_country,time_duration,ft.Container(height=10),submit_flight],horizontal_alignment="center")

	flight_registration = ft.Container(
		content=flight_form,
		gradient= ft.LinearGradient(
			begin=ft.alignment.top_center,
			end=ft.alignment.bottom_center,
			colors=["#eef2fa", "#e0e8fb"],
		),
		width=400,
		height=550,
		border_radius=40,
	)

	page.add(
		ft.Container(height=10),
		ft.Row([ft.Text("Welcome, Register your Flight", style="titleLarge")],alignment="center"),
		ft.Container(height=10),
		flight_registration
	)

ft.app(target=main,assets_dir="assets")