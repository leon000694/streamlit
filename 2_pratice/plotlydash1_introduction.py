""" Plotly Dash Tutorial Part-3"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

app = dash.Dash()

app.layout = html.Div([
	html.H1('Hello Dash!!!'),
	html.Div('Dash - A Data product development framework from plolty'),

	dcc.Graph(
		id ='samplechart',
		figure={
			'data':[
				{'x':[4,6,8],'y':[12,16,18],'type':'bar','name':'First chart'},
				{'x':[4,6,8],'y':[20,24,26],'type':'bar','name':'Second chart'}
			],
			'layout':{
				'title':'Simple Bar Chart'
			}
		}
	)
])

if __name__ == '__main__': 
	app.run_server(port =4050)


# https://www.youtube.com/watch?v=QJPN2J_KGXI&t=7s