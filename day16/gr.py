# pip install flet

import flet as fl
from flet import Page, Text, Row, IconButton, Column


def main(page: Page):
    page.title = "Our test window!"
    page.vertical_alignment="center"
    
    label = Text(value="0", color = fl.colors.RED, size=40 ) #Control 
    slabel = Text(value="0", color = fl.colors.YELLOW, size=40)
    
    def slider_change(e):
        slabel.value = slider.value
        page.update()

    def add_click(e):
        digits = int(label.value)+1
        label.value = str(digits)
        page.update()

    def remove_click(e):
        digits = int(label.value)-1
        label.value = str(digits)
        page.update()    

    
    button_add = IconButton(fl.icons.ADD_CIRCLE,on_click=add_click, icon_size=40,icon_color=fl.colors.GREEN)
    button_remove = IconButton(fl.icons.REMOVE_CIRCLE,on_click=remove_click, icon_size=40, icon_color=fl.colors.BLUE)
    slider = fl.Slider(min=0, max=100, divisions=10,
                       value=0, on_change=slider_change)
                       
    page.add(
        Column([
           slabel, 
           slider, 
           label,
           button_add,
           button_remove
        ],
        alignment="center")
    )

fl.app(target=main)