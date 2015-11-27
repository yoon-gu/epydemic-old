from PyQt4 import QtGui
import pyqtgraph as pg
import pyqtgraph.parametertree.parameterTypes as pTypes
from pyqtgraph.parametertree import Parameter, ParameterTree, ParameterItem, registerParameterType

def show():    
    ## Always start by initializing Qt (only once per application)
    app = QtGui.QApplication([])

    ## Define a top-level widget to hold everything
    w = QtGui.QWidget()
    params = [
            {'name': 'beta', 'type': 'float', 'value': 1.4247},
            {'name': 'gamma', 'type': 'float', 'value': 0.14286, 'step': 0.1},
            {'name': 'TS', 'type': 'float', 'value': 0.1},
            {'name': 'ND', 'type': 'float', 'value': 70},
            {'name': 'S0', 'type': 'float', 'value': 1-1e-6},
            {'name': 'I0', 'type': 'float', 'value': 1e-6},
    ]
    ## Create tree of Parameter objects
    p = Parameter.create(name='params', type='group', children=params)
    t = ParameterTree()
    t.setParameters(p, showTop=False)

    ## Create a grid layout to manage the widgets size and position
    layout = QtGui.QGridLayout()
    w.setLayout(layout)
    w.resize(1000,600)

    ## Create some widgets to be placed inside
    btn = QtGui.QPushButton('&Play')
    btn2 = QtGui.QPushButton('&Stop')
    btn3 = QtGui.QPushButton('E&xit')

    cw = pg.GraphicsLayoutWidget()
    p1 = cw.addPlot(row=0, col=0, title="S")
    p1.setLabel('left', "Ratio")
    p1.setLabel('bottom', "Time", units='day')
    p2 = cw.addPlot(row=1, col=0, title="I")
    p2.setLabel('left', "Ratio")
    p2.setLabel('bottom', "Time", units='day')
    p3 = cw.addPlot(row=2, col=0, title="R")
    p3.setLabel('left', "Ratio")
    p3.setLabel('bottom', "Time", units='day')

    def compute():
        import scipy.integrate as spi
        import numpy as np
        beta=p['beta']
        gamma=p['gamma']
        TS=p['TS']
        ND=p['ND']
        S0=p['S0']
        I0=p['I0']
        INPUT = (S0, I0, 0.0)
        def diff_eqs(INP,t):  
            '''The main set of equations'''
            Y=np.zeros((3))
            V = INP    
            Y[0] = - beta * V[0] * V[1]
            Y[1] = beta * V[0] * V[1] - gamma * V[1]
            Y[2] = gamma * V[1]
            return Y   # For odeint
        t_start = 0.0; t_end = ND; t_inc = TS
        t_range = np.arange(t_start, t_end+t_inc, t_inc)
        RES = spi.odeint(diff_eqs,INPUT,t_range)
        ## Plot
        p1.clear()
        p2.clear()
        p3.clear()
        p1.plot(t_range, RES[:, 0])
        p2.plot(t_range, RES[:, 1])
        p3.plot(t_range, RES[:, 2])

    btn.clicked.connect(compute)

    ## Add widgets to the layout in their proper positions
    layout.addWidget(t, 0, 0)  # list widget goes in bottom-left
    layout.addWidget(btn, 1, 0)   # button goes in upper-left
    layout.addWidget(btn2, 2, 0)   # button goes in upper-left
    layout.addWidget(btn3, 3, 0)   # button goes in upper-left
    layout.addWidget(cw, 0, 1, 4, 1)  # plot goes on right side, spanning 3 rows

    ## Display the widget as a new window
    w.show()
    ## Start the Qt event loop
    app.exec_()

if __name__ == '__main__':
    show()