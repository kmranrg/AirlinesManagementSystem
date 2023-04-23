import flet as ft
from register_flight import FlightRegistration
from show_flight import ShowFlight
from developer import DeveloperDetails
import csv
import random

def main(page: ft.Page):
	page.title = "Airlines Management System"
	page.theme_mode = "light"
	page.horizontal_alignment = "center"
	page.vertical_alignment = "center"
	page.scroll = "always"

	# navigation appbar
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

	def change_navigation_destination(e):
		if e.control.selected_index == 0:
			page.clean()
			page.add(flightRegistration)
		elif e.control.selected_index == 1:
			page.clean()
			page.add(showFlights)
		elif e.control.selected_index == 2:
			page.clean()
			page.add(developerDetails)

	# navigation bar
	page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EDIT_NOTE, label="Register Flight"),
            ft.NavigationDestination(icon=ft.icons.AIRPLANEMODE_ACTIVE, label="Flights"),
            ft.NavigationDestination(
                icon=ft.icons.PERSON_ROUNDED,
                label="Developer",
            ),
        ],
	height=70,
	on_change=lambda e: change_navigation_destination(e),
    )

	def show_flights():
		row_count = 0
		filename = "airlines_data.csv"
		fields = []
		rows = []
		with open(filename, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for row in csvreader:
				rows.append(row)
		total_flights = (csvreader.line_num)-1 # subtracting the fields name row
		show_flights_column = ft.Column()
		for row in rows:
			row_count += 1
			globals()[f"showFlight_{row_count}"] = ShowFlight()
			random_no = random.randint(1,9)
			globals()[f"showFlight_{row_count}"].flight_image.src = f"images/airlogos_{random_no}.png"
			globals()[f"showFlight_{row_count}"].flight_name.value = row[0]
			globals()[f"showFlight_{row_count}"].flight_serialCode.value = row[1]
			globals()[f"showFlight_{row_count}"].flight_model.value = row[2]
			globals()[f"showFlight_{row_count}"].flight_starting_airport.value = row[3]
			globals()[f"showFlight_{row_count}"].flight_ending_airport.value = row[4]
			globals()[f"showFlight_{row_count}"].flight_time_duration.value = row[5]
			show_flights_column.controls.append(globals()[f"showFlight_{row_count}"])
		return show_flights_column

	# creating the instance of FlightRegistration class
	flightRegistration = FlightRegistration()

	# creating the instance of DeveloperDetails class
	developerDetails = DeveloperDetails()

	# creating the instance of ShowFlight
	showFlights = show_flights()

	page.add(flightRegistration)

ft.app(target=main,assets_dir="assets")