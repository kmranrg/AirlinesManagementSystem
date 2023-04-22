import flet as ft

class DeveloperDetails(ft.UserControl):
    def build(self):
        developer_photo = ft.CircleAvatar(
            content=ft.Image(src='logo/dev.png'),
            height=130,
            width=150,
            bgcolor=ft.colors.WHITE
        )
        developer_name = ft.Text("Made by SmartGurucool",style='titleLarge',color=ft.colors.BLACK87)
        copyright_details = ft.Text("Copyright © 2023",style='titleMedium',color=ft.colors.BLUE_GREY_900)
        rights = ft.Text("All Rights Reserved",style='titleMedium',color=ft.colors.BLUE_GREY_900)
        return ft.Column([ft.Container(height=180),developer_photo,ft.Container(height=20),developer_name,copyright_details,rights],horizontal_alignment="center")
