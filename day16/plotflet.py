import plotly.express as px
from flet.plotly_chart import PlotlyChart
import plotly.graph_objects as go
import flet as ft
import numpy as np
import pandas
import solver
from flet import Page, Text, TextField, Column, Row, IconButton

def main(page: Page):
   
    def valSet( x )->str:
        s = ""
        if x[0] == '-':
            s = f'({x})'
        else:
            s = x
        return s

    def draw(e):
        a = int(startx.value)
        b = int(endx.value)
        data = list(np.arange(a,b,0.1))
        funcs = func.value
        values = list(map(lambda t: solver.solve(funcs.replace('@x',valSet(str(t)))),data))
        df = pandas.DataFrame(dict(
            x=data,
            y=values
        ))
        fig = px.line(df, x="x", y="y", title="User function")
        fig.update_traces(line=dict(color="Red", width=0.5))
        column = Column([
            rowf,
            rowrange,
            PlotlyChart(fig, expand=False)
        ],scroll=ft.ScrollMode.ALWAYS)

        page.clean()
        page.add(column)
        page.update()

    text = Text('Enter your function with variable as @x')
    func = TextField(value='')
    buttonstart = IconButton(
        icon=ft.icons.CALCULATE_ROUNDED, icon_size=60, on_click=draw)
    textstartlabel = Text('Enter start on X scale')
    startx = TextField(value='')
    textendlabel = Text('Enter end on X scale')
    endx = TextField(value='')
    rowf = Row([text,func,buttonstart])
    rowrange=Row([textstartlabel,startx,textendlabel,endx])
    column = Column([
        rowf,
        rowrange,
    ])
    page.add(column)


ft.app(target=main, view=ft.WEB_BROWSER, port=80)
