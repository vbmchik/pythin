import flet as ft
import solver

def main(page: ft.page):
    page.title = "Flet example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER



    def solveW(e):
       try: 
        txt_output.value = solver.solve(txt_method.value)
       except Exception as e:
        txt_output.value = repr(e)
       page.update()

    txt_method = ft.TextField(
        value="", text_align=ft.TextAlign.RIGHT, width=400,on_submit=solveW)


    txt_output = ft.Text(
        value="", text_align=ft.TextAlign.RIGHT, width=400)

    

    page.add(
        ft.Column(
            [
                ft.IconButton(ft.icons.CALCULATE, on_click=solveW, icon_size=70),
                txt_method,
                txt_output
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
