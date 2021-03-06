from pysketcher import *
from numpy import exp, linspace

L = 10.
H = 6.
margin = 2
wall_thickness = 0.5

drawing_tool.set_coordinate_system(xmin=-margin, xmax=L+margin,
                                   ymin=-margin, ymax=H+margin,
                                   axis=False)

drawing_tool.set_linecolor('blue')
drawing_tool.set_fontsize(20)

bottom = Rectangle((0,-wall_thickness),  L, wall_thickness).\
         set_filled_curves(pattern='/')
top    = Rectangle((0, H),      L, wall_thickness).\
         set_filled_curves(pattern='/')
inlet  = Line((0,0), (0,H)).set_linestyle('dashed')
outlet = Line((L,0), (L,H)).set_linestyle('dashed')

def velprofile(y):
    return [1, 0]

inlet_profile = VelocityProfile((0,0), H, velprofile, 5)

fig = Composition({
    'bottom': bottom,
    'top': top,
    'inlet': inlet_profile,
    'outlet': outlet,
    })

fig.draw()  # send all figures to plotting backend

symbols = {
    'u_x inlet':
    Text('$u_x=1$', (-0.2, H/2), alignment='right'),
    'u_y inlet':
    Text('$u_y=0$', (-0.2, H/2-0.6), alignment='right'),
    'bottom':
    Text('$u_x=u_y=0$', (L/2, -1), alignment='center'),
    'top':
    Text('$u_x=u_y=0$', (L/2, H+0.75), alignment='center'),
    'outlet1':
    Text(r'$\frac{\partial u_y}{\partial n}=0$', (L+0.1,H/2-1), alignment='left'),
    'outlet2':
    Text(r'$\frac{\partial u_x}{\partial n}=0$', (L+0.1,H/2), alignment='left'),
    'outlet3':
    Text('$p=p_0$', (L+0.1, H/2+0.75), alignment='left')}

symbols = Composition(symbols)
symbols.draw()

drawing_tool.display()
drawing_tool.savefig('os.path.splitext(__file__)[0]')


raw_input()
