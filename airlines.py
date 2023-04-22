import flet as ft
from register_flight import FlightRegistration
from show_flights import ShowFlights
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
			show_flights()
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
		showFlights = ShowFlights()
		filename = "airlines_data.csv"
		fields = []
		rows = []
		with open(filename, 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			fields = next(csvreader)
			for row in csvreader:
				rows.append(row)
		total_flights = (csvreader.line_num)-1 # subtracting the fields name row
		
		for row in rows:
			random_no = random.randint(1,9)
			showFlights.flight_image.src = f"images/airlogos_{random_no}.png"
			showFlights.flight_name.value = row[0]
			showFlights.flight_serialCode.value = row[1]
			showFlights.flight_model.value = row[2]
			showFlights.flight_starting_airport.value = row[3]
			showFlights.flight_ending_airport.value = row[4]
			showFlights.flight_time_duration.value = row[5]
			page.add(showFlights)

	# creating the instance of FlightRegistration class
	flightRegistration = FlightRegistration()

	# creating the instance of DeveloperDetails class
	developerDetails = DeveloperDetails()

	page.add(
		flightRegistration,
	)

ft.app(target=main,assets_dir="assets")