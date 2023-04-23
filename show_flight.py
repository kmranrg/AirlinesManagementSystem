import flet as ft

class ShowFlight(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.flight_name = ft.Text(style='headlineSmall',width=150)
        self.flight_serialCode = ft.Text(style='titleMedium')
        self.flight_model = ft.Text(style='titleLarge',color=ft.colors.ORANGE_800,width=80)
        self.flight_starting_airport = ft.Text(style='titleLarge')
        self.flight_ending_airport = ft.Text(style='titleLarge')
        self.flight_time_duration = ft.Text(style='headlineLarge',color=ft.colors.BLACK)
        self.flight_image = ft.Image(width=70)
        self.delete_flight = ft.IconButton(icon=ft.icons.DELETE_FOREVER,icon_color=ft.colors.RED,icon_size=35)

    def build(self):
        self.flight_row = ft.Row(
            controls = [
                ft.Container(width=50),
                self.flight_image,
                ft.Column([
                    self.flight_name,
                    self.flight_serialCode
                ],alignment='center',spacing=5),
                self.flight_model,
                ft.Container(width=6),
                self.flight_starting_airport,
                ft.Icon(ft.icons.ARROW_FORWARD),
                self.flight_ending_airport,
                ft.Container(width=8),
                ft.Row([ft.Icon(ft.icons.ACCESS_TIME,color=ft.colors.BLUE_900),self.flight_time_duration],alignment='end')
            ]
        )

        self.flight_row_container = ft.Row([
            ft.Container(
                content=self.flight_row,
                height=120,
                width=1000,
                border_radius=30,
                gradient= ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#eef2fa", "#e0e8fb"],
                ),
            ),
            ft.Container(
                content=self.delete_flight,
                height=120,
                width=80,
                border_radius=30,
                gradient= ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=["#fae8e8", "#fac1c1"],
                ),
            )
        ],alignment='center')
        
        return self.flight_row_container