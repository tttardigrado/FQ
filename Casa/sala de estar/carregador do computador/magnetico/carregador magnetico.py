from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import Range1d, LabelSet, ColumnDataSource
from scipy.interpolate import interp1d
import numpy as np


output_file('N:\CODING\Python\Projetos\FQ\Casa\sala de estar\carregador do computador\magnetico\carregador magnetico.html')



d = [0.000, 0.010, 0.020]

b = [3.230, 0.1166, 0.01274]


f = figure(plot_height=300, title='Carregador do computador - Campo magnético', toolbar_location='above')

source = ColumnDataSource(dict(x=d, y=b))
labels = LabelSet(x='x', y='y', text='y', level='glyph', x_offset=10, y_offset=5, source=source, render_mode='canvas')
f.add_layout(labels)

f.x_range = Range1d(0, 0.04, bounds=(0, None))
f.y_range = Range1d(0, 4, bounds=(0, None))
f.xaxis.axis_label = 'd (m)'
f.yaxis.axis_label = 'B (uT)'
f.xgrid.grid_line_color = None
f.y_range.start = 0

f.circle(d, b, fill_color="green", size=8)

show(f)