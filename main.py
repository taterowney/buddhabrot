from math import log
from tkinter import *
from pylab import *
import random
from PIL import Image

from buddhabrot_raw import ganesh_set_red, ganesh_set_green, ganesh_set_blue

tk = None
canvas = None

ZOOM = 1
#POSITION = (-0.75, 0)
POSITION = (-1.226439605936408, 0.12247307505831123)

cmap = cm.get_cmap('twilight_shifted', 100)
stripe_width = 3

random.seed(11)



def plot_ganesh_set(canvas_size, chunk_size, center_point, zoom_factor=1.0):
    tk = Tk()
    canvas = Canvas(tk, width=canvas_size[0], height=canvas_size[1])
    canvas.pack()
    ganesh_set = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    for i in range(2000000):
#        random_point = (random.uniform(-0.5, 2), random.uniform(-1.3, 1.3))
        random_point = (random.uniform(-2, 2), random.uniform(-2, 2))
        new_points = update_escape_points(random_point, canvas_size, chunk_size, zoom_factor=zoom_factor)
        if new_points:
            for point in new_points:
                x = point[0]
                y = point[1]
                ganesh_set[x][y] += 20
    for i in range(len(ganesh_set)):
        for j in range(len(ganesh_set[i])):
            if ganesh_set[i][j] > 255:
                color = 255
            else:
                color = ganesh_set[i][j]
            canvas.create_rectangle(j*chunk_size[0], i*chunk_size[1], (j+1)*chunk_size[0], (i+1)*chunk_size[1]+1, outline="#%02x%02x%02x" % (color, color, color), fill="#%02x%02x%02x" % (color, color, color))
    tk.mainloop()



def save_ganesh_set(canvas_size, chunk_size, center_point, zoom_factor=1.0):
    img = Image.new("RGB", (canvas_size[0], canvas_size[1]), "black")
    pixels = img.load()
#    ganesh_set = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    ganesh_set_red = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    ganesh_set_green = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    ganesh_set_blue = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    for i in range(2000000):
#        random_point = (random.uniform(-0.5, 2), random.uniform(-1.3, 1.3))
        random_point = (random.uniform(-2, 2), random.uniform(-2, 2))
        new_points, colors = update_escape_points(random_point, canvas_size, chunk_size, zoom_factor=zoom_factor)
        if new_points:
            for point in new_points:
                x = point[0]
                y = point[1]
                increase = 50
                if "red" in colors:
                    ganesh_set_red[x][y] += increase
                if "green" in colors:
                    ganesh_set_green[x][y] += increase
                if "blue" in colors:
                    ganesh_set_blue[x][y] += increase
    for i in range(len(ganesh_set_red)):
        for j in range(len(ganesh_set_red[i])):
            color = [ganesh_set_red[i][j], ganesh_set_green[i][j], ganesh_set_blue[i][j]]
            for c in range(len(color)):
                if color[c] > 255:
                    color[c] = 255
            pixels[j, i] = tuple(color)
            #canvas.create_rectangle(j*chunk_size[0], i*chunk_size[1], (j+1)*chunk_size[0], (i+1)*chunk_size[1]+1, outline="#%02x%02x%02x" % (color, color, color), fill="#%02x%02x%02x" % (color, color, color))
    img.save("buddhabrot.jpg", quality=95)

def load_ganesh_set(canvas_size=(2000, 2000), gain=10):
    img = Image.new("RGB", (canvas_size[0], canvas_size[1]), "black")
    pixels = img.load()
    for i in range(len(ganesh_set_red)):
        for j in range(len(ganesh_set_red[i])):
            color = [ganesh_set_red[i][j]*gain, ganesh_set_green[i][j]*gain, ganesh_set_blue[i][j]*gain]
            for c in range(len(color)):
                if color[c] > 255:
                    color[c] = 255
            pixels[j, i] = tuple(color)
            #canvas.create_rectangle(j*chunk_size[0], i*chunk_size[1], (j+1)*chunk_size[0], (i+1)*chunk_size[1]+1, outline="#%02x%02x%02x" % (color, color, color), fill="#%02x%02x%02x" % (color, color, color))
    img.save("buddhabrot.jpg", quality=95)


def write_ganesh_set(canvas_size, chunk_size, center_point, zoom_factor=1.0, iterations=2000000):
    img = Image.new("RGB", (canvas_size[0], canvas_size[1]), "black")
    pixels = img.load()
#    ganesh_set = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    ganesh_set_red = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    ganesh_set_green = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    ganesh_set_blue = [[0 for cols in range(int(canvas_size[0]/chunk_size[0]))] for rows in range(int(canvas_size[1]/chunk_size[1]))]
    for i in range(iterations):
#        random_point = (random.uniform(-0.5, 2), random.uniform(-1.3, 1.3))
        random_point = (random.uniform(-2, 2), random.uniform(-2, 2))
        a = random_point[0]
        b = random_point[1]
        cr = a * a + b * b
        ci = sqrt(cr - a / 2 + 0.0625)
        if ((16 * cr * ci) < (5 * ci - 4 * a + 1)):
            continue
        new_points, colors = update_escape_points(random_point, canvas_size, chunk_size, zoom_factor=zoom_factor)
        if new_points:
            for point in new_points:
                x = point[0]
                y = point[1]
                increase = 1
                if "red" in colors:
                    ganesh_set_red[x][y] += increase
                    ganesh_set_red[x][len(ganesh_set_red[0])-y-1] += increase
                if "green" in colors:
                    ganesh_set_green[x][y] += increase
                    ganesh_set_green[x][len(ganesh_set_green[0])-y-1] += increase
                if "blue" in colors:
                    ganesh_set_blue[x][y] += increase
                    ganesh_set_blue[x][len(ganesh_set_blue[0])-y-1] += increase
    with open("./buddhabrot_raw.py", "w") as f:
        f.write("ganesh_set_red = " + str(ganesh_set_red) + "\n")
        f.write("ganesh_set_green = " + str(ganesh_set_green) + "\n")
        f.write("ganesh_set_blue = " + str(ganesh_set_blue) + "\n")


def update_escape_points(c, canvas_size, chunk_size, zoom_factor=1.0, max_iterations=500):
#    x0 = (c[0]-0.5*(canvas_size[0]/chunk_size[0]))/(zoom_factor*canvas_size[0]/(chunk_size[0]))
#    y0 = (c[1]-0.5*(canvas_size[0]/chunk_size[0]))/(zoom_factor*canvas_size[0]/(chunk_size[0]))
    x0 = c[0]
    y0 = c[1]
    x = 0
    y = 0
    iteration = 0
    updated_points = []
    #while (x**2+y**2 < 65536) and iteration < max_iterations:
    while (x ** 2 + y ** 2 < 4096) and iteration < max_iterations:
        xtemp = x*x - y*y + x0
        y = 2*x*y + y0
        x = xtemp
        iteration += 1
        screen_x = x * (zoom_factor * canvas_size[0] / (chunk_size[0])) + 0.5 * (canvas_size[0] / chunk_size[0])
        screen_y = y * (zoom_factor * canvas_size[1] / (chunk_size[1])) + 0.5 * (canvas_size[1] / chunk_size[1])
        if (abs(screen_x) < canvas_size[0] / chunk_size[0] - 1) and (abs(screen_y) < canvas_size[1] / chunk_size[1] - 1) and (screen_x>=0) and (screen_y>=0):
            updated_points.append((round(screen_x), round(screen_y)))
    if iteration < max_iterations:
        if iteration < max_iterations/2:
            if iteration < max_iterations/10:
                return updated_points, ("red",)
            return updated_points, ("green",)
        return updated_points, ("blue",)
    else:
        return False, False



def create_canvas(canvas_size):
    global tk, canvas
    tk = Tk()
    canvas = Canvas(tk, width=canvas_size[0], height=canvas_size[1])
    canvas.pack()


def save_mandelbrot_set(canvas_size, center_point, zoom_factor=1.0):
    chunk_size = (1, 1)
    global ZOOM
    ZOOM = zoom_factor
    for round in range(100):
        img = Image.new("RGB", (canvas_size[0], canvas_size[1]), "black")
        pixels = img.load()
        mandelbrot_set = [[0] * int(canvas_size[0]/chunk_size[0])]*int(canvas_size[1]/chunk_size[1])
        for i in range(len(mandelbrot_set)):
            for j in range(len(mandelbrot_set[i])):
                hue = mandelbrot(((j-0.5*(canvas_size[0]/chunk_size[0]))/(ZOOM*canvas_size[0]/(chunk_size[0]))+center_point[0], (i-0.5*(canvas_size[1]/chunk_size[1]))/(-ZOOM*canvas_size[1]/(chunk_size[1]))+center_point[1]))
                if hue == None:
                    hue = (0, 0, 0)
                else:
                    hue = to_rgb(hue)
                pixels[j,i] = hue
#        img.show()
        img.save("mandelbrot_set"+str(round)+".jpg")
        ZOOM *= 1.1


def plot_mandelbrot_set(canvas_size, chunk_size, center_point, zoom_factor=1.0):
    global ZOOM
    ZOOM = zoom_factor
    if tk == None:
        create_canvas(canvas_size)
    mandelbrot_set = [[0] * int(canvas_size[0]/chunk_size[0])]*int(canvas_size[1]/chunk_size[1])
    for i in range(len(mandelbrot_set)):
        for j in range(len(mandelbrot_set[i])):
            hue = mandelbrot(((j-0.5*(canvas_size[0]/chunk_size[0]))/(zoom_factor*canvas_size[0]/(chunk_size[0]))+center_point[0], (i-0.5*(canvas_size[1]/chunk_size[1]))/(-zoom_factor*canvas_size[1]/(chunk_size[1]))+center_point[1]))
            if hue == None:
                hue = 'black'
            else:
                hue = to_hex(hue)
            canvas.create_rectangle(j*chunk_size[0], i*chunk_size[1], (j+1)*chunk_size[0], (i+1)*chunk_size[1]+1, outline=hue, fill=hue)
    tk.bind('<Button-1>', zoom_in)
    tk.bind('<Button-2>', zoom_out)
    tk.bind('<Return>', enhance)
    tk.bind('<KeyPress-+>', zoom_in_same_pos)
    tk.mainloop()


def enhance(event):
    global POSITION
    canvas.delete('all')
    plot_mandelbrot_set((500, 500), (1, 1), POSITION, zoom_factor=ZOOM)


def zoom_in_same_pos(event):
    global POSITION
    canvas.delete('all')
    plot_mandelbrot_set((500, 500), (5, 5), POSITION, zoom_factor=ZOOM*2)


def zoom_in(event):
    global POSITION
    POSITION = (POSITION[0] + (event.x/500 - 0.5)/ZOOM, POSITION[1] -(event.y/500 - 0.5)/ZOOM)
    print(POSITION, ZOOM)
    canvas.delete('all')
    plot_mandelbrot_set((500, 500), (5, 5), POSITION, zoom_factor=ZOOM*2)


def zoom_out(event):
    global POSITION
    canvas.delete('all')
    print(POSITION, ZOOM)
    plot_mandelbrot_set((500, 500), (5, 5), POSITION, zoom_factor=ZOOM/2)


def to_rgb(value):
    value /= stripe_width
    color = list(cmap(math.floor(value) % cmap.N))
    color.pop()
    for i in range(len(color)):
        color[i] = round(color[i]*255)
    return tuple(color)


def to_hex(value):
    value /= stripe_width
    color = matplotlib.colors.to_hex(cmap(math.floor(value) % cmap.N))
    return color


def mandelbrot(c, max_iterations=1000):
    x0 = c[0]
    y0 = c[1]
    x = 0
    y = 0
    x2 = 0
    y2 = 0
#    x = 0.1
#    y = 0.2
    iteration = 0
    while (x2+y2 < 65536) and iteration < max_iterations:
        y = 2 * x * y + y0
        x = x2 - y2 + x0
        x2 = x * x
        y2 = y * y
        iteration += 1
    if iteration < max_iterations:
# sqrt of inner term removed using log simplification rules.
        log_zn = log(x*x + y*y) / 2
        nu = log(log_zn / log(2)) / log(2)
        #This is to scale the value into a color that makes sense
        #I don't know exactly whats going on here, I got it from wikipedia
        #what does a drowning number theorist say? "log log log log..."
        iteration = iteration + 1 - nu
        return (iteration)




if __name__ == '__main__':
#    plot_mandelbrot_set((500, 500), (5, 5), (-0.954955230936408, 0.25391057505831116), zoom_factor=1000)
#    plot_mandelbrot_set((500, 500), (5, 5), (-0.75, 0), zoom_factor=0.5)
#    save_mandelbrot_set((500, 500), POSITION, zoom_factor=128)
#    write_ganesh_set((2000, 2000), (1, 1), (0, 0), zoom_factor=0.3, iterations=200000)
    load_ganesh_set(canvas_size=(2000, 2000), gain=100)
