'''
Weigeng Peng, 1730694
Friday,  May 10
R. Vincent, instructor
Final Project

'''

from tkinter import *

def clear_all():
    '''clear the entry values'''
    for widget in window.winfo_children():      # get all children of root
        if widget.winfo_class() == 'Entry':   # if the class is Entry
            widget.delete(0,END)              # reset its value
           
def plot():
    '''plot the given values'''
    #import all the necessary lib
    import matplotlib.animation as animation
    from numpy import cos, sin
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.integrate as integrate
    from math import pi

    def derivs(state, t):
        '''Return dydx the derivative of the equation of motion.'''
        dydx = np.zeros_like(state)
        dydx[0] = state[1]  # initial angular velocity
        dydx[1] = -(float(g.get())/float(l.get())*sin(state[0]))
        return dydx

    def init():
        '''initialize line and time_text'''
        line.set_data([])
        time_text.set_text('')
        return line, time_text

    def animate(i):
        '''connect the two points with a line to create a pendulum and print the time'''
        thisx = [0, x1[i]]
        thisy = [0, y1[i]]
        #draw a line connecting the pivoting point and the ball
        line.set_data(thisx, thisy)
        time_text.set_text(time_template%(i*float(Dt.get())))
        px1.set_text("x = %.2fm"%x1[i])
        py1.set_text("y = %.2fm"%y1[i])
        period.set_text("Period = %.2fs"%T)

    #period calculations(SHM)
    omeg = (float(g.get())/float(l.get()))**0.5
    if omeg == 0:
        T = 2
        pass
    else:
        T = (2*pi)/omeg
    
    #initial states of pendulum
    state = np.radians([float(Theta.get()), float(W.get())])
    t = np.arange(0.0,T*3,float(Dt.get()))  

    derivs(state, t)
    # integrate the differential equation
    y = integrate.odeint(derivs, state,t)

    #the position of x and y
    x1 = float(l.get())*sin(y[:,0])
    y1 = -float(l.get())*cos(y[:,0])

    #configurate the figure, plot elements that we want to animate
    fig = plt.figure()
    gp = fig.add_subplot(111, xlim =(-2*float(l.get()),2*float(l.get())), 
                        ylim = (-2*float(l.get()),2*float(l.get())))
    gp.set_aspect('equal')
    gp.grid()
    line, = gp.plot([],[], 'o-')

    #Location of time on the figure 
    time_template = 'time =%.1fs'
    time_text = gp.text(0.05, 0.9,'', transform = gp.transAxes)
    px1 = gp.text(0.7,0.9,'',transform = gp.transAxes)
    py1 =  gp.text(0.7,0.8,'',transform = gp.transAxes)
    period = gp.text(0.7,0.7,'',transform = gp.transAxes)

    ani = animation.FuncAnimation(fig, animate, np.arange(1,len(y)), interval=20)
    plt.show()

def defult_setting():
    '''If you don't want to bother to type in again and again by hand...'''
    e1.insert(0, '10')
    e2.insert(1, '9.8')
    e3.insert(2,'10')
    e4.insert(3, '60')
    e5.insert(4, '0.05')
    e6.insert(5, '10')
    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)
    e3.grid(row = 2, column = 1)
    e4.grid(row = 3, column = 1)
    e5.grid(row = 4, column = 1)
    e6.grid(row = 5, column = 1)

    

#create a window object
window = Tk()

#Labels
l1 = Label(window, text = 'Length')
l1.grid(row = 0, column = 0)

l2 = Label(window, text = 'Gravitational Constant')
l2.grid(row = 1, column = 0)

l3 = Label(window, text = 'Mass')
l3.grid(row = 2, column = 0)

l4 = Label(window, text = 'Initial Angle')
l4.grid(row = 3, column = 0)

l5 = Label(window, text = 'Change in Time')
l5.grid(row = 4, column = 0)

l6 = Label(window, text = 'Velocity')
l6.grid(row = 5, column = 0)

#Entries
l = StringVar()
e1 = Entry(window, textvariable = l)
e1.grid(row = 0, column = 1)

g = StringVar()
e2 = Entry(window, textvariable = g)
e2.grid(row = 1, column = 1)

m = StringVar()
e3 = Entry(window, textvariable = m)
e3.grid(row = 2, column = 1)

Theta = StringVar()
e4 = Entry(window, textvariable = Theta)
e4.grid(row = 3, column = 1)

Dt = StringVar()
e5 = Entry(window, textvariable = Dt)
e5.grid(row = 4, column = 1)

W = StringVar()
e6 = Entry(window, textvariable = W)
e6.grid(row = 5, column = 1)

#Buttons
b1 = Button(window, text='Plot!', width = 16, activeforeground = 'white', 
            relief = RAISED, command = plot)
b1.grid(row = 1, column = 2)

b2 = Button(window, text ='Refresh', width = 16, activeforeground = 'white',
            relief = RAISED, command = clear_all)
b2.grid(row = 2, column = 2)

b3 = Button(window, text = 'Try Default', width = 16, activeforeground = 'white',
            command = defult_setting)
b3.grid(row=3, column = 2)

window.mainloop()


