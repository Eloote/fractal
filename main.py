import math
import tkinter as tk


def draw_branch(x, y, length, direction, depth, angle):
    if depth == 0:
        return

    radians = math.radians(direction)
    x2 = x + length * math.cos(radians)
    y2 = y + length * math.sin(radians)

    canvas.create_line(
        x, y, x2, y2, fill="darkgreen", width=max(1, depth // 3)
    )

    draw_branch(x2, y2, length * 0.7, direction - angle, depth - 1, angle)
    draw_branch(x2, y2, length * 0.7, direction + angle, depth - 1, angle)


def draw_tree(value=None):
    canvas.delete("all")
    draw_branch(400, 550, 150, -90, 10, angle_slider.get())


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Фрактальное дерево")
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=800, height=600, bg="white")
    canvas.pack()

    angle_slider = tk.Scale(
        window,
        from_=0,
        to=90,
        orient=tk.HORIZONTAL,
        label="Угол ветвей (градусы)",
        length=400,
        command=draw_tree,
    )
    angle_slider.set(25)
    angle_slider.pack()

    draw_tree()
    window.mainloop()