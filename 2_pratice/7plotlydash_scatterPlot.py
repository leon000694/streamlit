""" Plotly Dash Tutorial Part-7 """
import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components as html
import numpy as np

app = dash.Dash()
np.random.seed(50)
x_rand = np.random.randint(1,61,60)
y_rand = np.random.randint(1,61,60)

app.layout = html.Div([
	dcc.Graph(
		id='scatter_chart',
		figure = {
			'data' : [
				go.Scatter(
					x = x_rand,
					y = y_rand,
					mode = 'markers'
				)
			],
			'layout' : go.Layout(
				title = 'Scatterplot of  Random 60 points',
				xaxis = {'title':'Random X Values'},
				yaxis = {'title':'Random Y Values'}
			)
		}
	)
])

if __name__ == '__main__': 
	app.run_server(port =4050)


# https://www.youtube.com/watch?v=LtmdwkprcEk
