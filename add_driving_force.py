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

    def derivs(state, t, param):
        '''Return dydx the derivative of the equation of motion.'''
        dydx = np.zeros_like(state)
        w_driv, A = param
        dydx = [state[1], 
                ((-float(g.get())/(float(l.get())*w_driv**2) - A/float(l.get())*np.cos(t))*sin(state[0]))]
        return dydx

    def init():
        '''initialize line and time_text'''
        line.set_data([])
        time_text.set_text('')
        return line, time_text

    def animate(i):
        '''connect the two points with a line to create a pendulum and print the time'''
        # thisx = [0, x1[i]]
        # thisy = [0, y1[i]]
        thisx = [0, x1[i]]
        thisy = [y0[i], y1[i] + y0[i]]
        #draw a line connecting the pivoting point and the ball
        line.set_data(thisx, thisy)
        time_text.set_text(time_template%(i*float(Dt.get())))
        # px1.set_text("x = %.2fm"%x1[i])
        # py1.set_text("y = %.2fm"%y1[i])
        # period.set_text("Period = %.2fs"%T)

    #period calculations(SHM)
    omeg = (float(g.get())/float(l.get()))**0.5
    if omeg == 0:
        T = 2
        pass
    else:
        T = (2*pi)/omeg
    
    #initial states of pendulum
    state = np.radians([float(Theta.get()), float(W.get())])
    param = [np.radians(float(W_driv.get())), float(A.get())]
    t = np.arange(0.0,T*5,float(Dt.get()))  

    derivs(state, t, param)
    # integrate the differential equation
    y = integrate.odeint(derivs, state,t, args=(param,))

    #the position of x and y
    x1 = float(l.get())*sin(y[:,0])
    y1 = -float(l.get())*cos(y[:,0])
    y0 = float(A.get())/float(l.get())*cos(t)

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
    e2.insert(1, '2')
    e3.insert(2,'1')
    e4.insert(3, '170')
    e5.insert(4, '0.1')
    e6.insert(5, '0')
    e7.insert(6, '150')
    e8.insert(7, '4')
    e1.grid(row = 0, column = 1)
    e2.grid(row = 1, column = 1)
    e3.grid(row = 2, column = 1)
    e4.grid(row = 3, column = 1)
    e5.grid(row = 4, column = 1)
    e6.grid(row = 5, column = 1)
    e7.grid(row = 6, column = 1)
    e8.grid(row = 7, column = 1)

    

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

l6 = Label(window, text = 'w')
l6.grid(row = 5, column = 0)

l7 = Label(window, text = 'w_driv')
l7.grid(row = 6, column = 0)

l8 = Label(window, text = 'Amplitude_driv')
l8.grid(row = 7, column = 0)

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

W_driv = StringVar()
e7 = Entry(window, textvariable = W_driv)
e7.grid(row = 6, column = 1)

A = StringVar()
e8 = Entry(window, textvariable = A)
e8.grid(row = 7, column = 1)

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


