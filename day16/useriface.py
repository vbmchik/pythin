import flet as ft
from flet import Page, IconButton, Text, TextField


def main(page:Page):

    

    def submit1(e):
        try:
            year = int(yearText.value)
            monthText.focus()
        except:
            page.dialog = dlg
            dlg.open=True
            yearText.focus()
            page.update()

        

    def submit2(e):
        businessText.focus()
    def submit3(e):
        incomeText.focus()
    def close_dlg(e):
        dlg.open=False
        page.update()    

    dlg = ft.AlertDialog(modal=True,
                         title=ft.Text("Data error"),
                         content=ft.Text("Please check if data is integer"),
                         actions=[ft.TextButton("Ok", on_click=close_dlg)])
    
    yearLabel = Text("Year: ", color=ft.colors.RED, size=40)
    yearText  = TextField(value="", color=ft.colors.BLUE, text_size=40, on_submit=submit1)
    yearRow = ft.Row([yearLabel,yearText],alignment='center')

    monthLabel = Text("Month: ", color=ft.colors.RED, size=40)
    monthText = TextField(value="", color=ft.colors.BLUE, text_size=40, on_submit=submit2)
    monthRow = ft.Row([monthLabel, monthText], alignment='center')

    businessLabel = Text("Business: ", color=ft.colors.RED, size=40)
    businessText = TextField(value="", color=ft.colors.BLUE, text_size=40,on_submit=submit3)
    businessRow = ft.Row([businessLabel, businessText], alignment='center')

    incomeLabel = Text("Income: ", color=ft.colors.RED, size=40)
    incomeText = TextField(value="", color=ft.colors.BLUE, text_size=40)
    incomeRow = ft.Row([incomeLabel, incomeText], alignment='center')
    
    page.add(ft.Column([yearRow,monthRow, businessRow, incomeRow]))


ft.app(target=main)