""" Plotly Dash Tutorial Part-8 """
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import pandas as pd
import numpy as np

app = dash.Dash()
orders = pd.read_excel('11010cost.xlsx', sheet_name=2, header=1)
print(orders)
input('stop..')

#app.layout = html.Div([
#	dcc.Graph(
#		id='scatter_chart',
#		figure = {
#			'data' : [
#				go.Scatter(
#					x = orders.11010cost,
#					y = orders.Profit,
#					mode = 'markers'
#				)
#			],
#			'layout' : go.Layout(
#				title = 'Scatterplot of  Random 60 points',
#				xaxis = {'title':'11010cost'},
#				yaxis = {'title':'Profit'},
#				hovermode = 'closest'
#			)
#		}
#	)
#])

if __name__ == '__main__': 
	app.run_server(port =4050)


# https://www.youtube.com/watch?v=WZERgVGUoIk&list=WL&index=4
