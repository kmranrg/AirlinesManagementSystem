import flet as ft
import csv

class FlightRegistration(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.airplane_name = ft.TextField(hint_text="airplane name",width=300,border_radius=25,border_color=ft.colors.BLUE_900)
        self.airplane_serialCode = ft.TextField(hint_text="serial code",width=300,border_radius=25,border_color=ft.colors.BLUE_900)
        self.airplane_model = ft.TextField(hint_text="model",width=300,border_radius=25,border_color=ft.colors.BLUE_900)
        self.start_airport = ft.TextField(hint_text="starting airport",width=300,border_radius=25,border_color=ft.colors.BLUE_900)
        self.end_airport = ft.TextField(hint_text="ending airport",width=300,border_radius=25,border_color=ft.colors.BLUE_900)
        self.time_duration = ft.TextField(hint_text="time duration (in hrs)",width=300,border_radius=25,border_color=ft.colors.BLUE_900)
        self.submit_flight = ft.ElevatedButton("Submit Flight", on_click=self.store_in_inventory)

    def store_in_inventory(self,e):
        row = [self.airplane_name.value,self.airplane_serialCode.value,self.airplane_model.value,self.start_airport.value,self.end_airport.value,self.time_duration.value]
        filename = "airlines_data.csv"
        with open(filename,'a') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the data rows
            csvwriter.writerow(row)
        csvfile.close()

    def build(self):
        self.flight_form = ft.Column([ft.Container(height=10),self.airplane_name,self.airplane_serialCode,self.airplane_model,self.start_airport,self.end_airport,self.time_duration,ft.Container(height=10),self.submit_flight],horizontal_alignment="center")
        self.flight_registration = ft.Container(
            content=self.flight_form,
            gradient= ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#eef2fa", "#e0e8fb"],
            ),
            width=400,
            height=550,
            border_radius=40,
        )

        return ft.Column([
            ft.Container(height=10),
            ft.Row([ft.Text("Welcome, register your Flight", style="titleLarge", color=ft.colors.BLUE_900)],alignment="center"),
            ft.Container(height=10),
            self.flight_registration
        ],horizontal_alignment="center")