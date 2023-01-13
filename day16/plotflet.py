import plotly.express as px
from flet.plotly_chart import PlotlyChart
import plotly.graph_objects as go
import flet as ft
import pandas
import solver
from flet import Page, Text

def main(page: Page):

    
    xdata = list(range(-200,201))
    xlabels = list(map(lambda t: str(t), xdata))
    ydata = list(map(lambda t: solver.solve(f"sin({t})+5*cos(({t})*2)") , xdata))
    #ydata = list(map(lambda t: solver.solve(
    #    f"cos(({t})*2)"), xdata))
    #style=px.data.gapminder().query("continent=='Oceania'")
    #fig = px.line(style, x='year', y='lifeExp', color='country')
    df = pandas.DataFrame(dict(
        x = xdata,
        y = ydata
    ))
    fig = px.line(df, x="x", y="y", title="Squares")
    
    page.add(Text('Test'),PlotlyChart(fig,expand=False))


ft.app(target=main)
