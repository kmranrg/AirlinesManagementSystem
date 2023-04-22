import flet as ft
import csv

class ShowFlights(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.flight_name = ft.Text()
        self.flight_serialCode = ft.Text()
        self.flight_model = ft.Text()
        self.flight_starting_airport = ft.Text()
        self.flight_ending_airport = ft.Text()
        self.flight_time_duration = ft.Text()

    def build(self):
        self.flight_row = ft.Row([self.flight_name,self.flight_serialCode,self.flight_model,self.flight_starting_airport,self.flight_ending_airport,self.flight_time_duration],alignment='center')

        self.flight_row_container = ft.Container(
            content=self.flight_row,
            height=50,
            width=800,
            border_radius=30,
            bgcolor='#e0e8fb'
        )
        return self.flight_row_container