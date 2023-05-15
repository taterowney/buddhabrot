from math import log
from pylab import *
from tkinter import *
import random
from PIL import Image

#from buddhabrot_raw import ganesh_set_red, ganesh_set_green, ganesh_set_blue

random.seed(12324565)

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


if __name__ == '__main__':
#    plot_mandelbrot_set((500, 500), (5, 5), (-0.954955230936408, 0.25391057505831116), zoom_factor=1000)
#    plot_mandelbrot_set((500, 500), (5, 5), (-0.75, 0), zoom_factor=0.5)
#    save_mandelbrot_set((500, 500), POSITION, zoom_factor=128)
#    write_ganesh_set((2000, 2000), (1, 1), (0, 0), zoom_factor=0.3, iterations=200000)
    load_ganesh_set(canvas_size=(2000, 2000), gain=100)
