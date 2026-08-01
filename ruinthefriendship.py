import tkinter as tk
import random

WIDTH = 1200
HEIGHT = 700

BG = "#000000"
GREEN = "#00ff66"
DARK = "#003311"

lyrics = [
    "My advice is always ruin the friendship",
    "Better that than regret it for all time",
    "Should've kissed you anyway",
    "",
    "And my advice is always answer the question",
    "Better than that to ask it all your life",
    "Should've kissed you anyway..."
]


class HackerTerminal:

    def __init__(self):
        self.root = tk.Tk()

        ...
        self.cursor_state = True

        self.create_background()
        self.create_terminal()
        self.animate()

        self.root.mainloop()

    def create_background(self):

        for _ in range(120):
            ...

            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)

            size = random.randint(1, 2)

            star = self.canvas.create_oval(
                x,
                y,
                x + size,
                y + size,
                fill="white",
                outline=""
            )

            self.stars.append(star)

        chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for x in range(0, WIDTH, 20):

            column = []

            start = random.randint(-HEIGHT, 0)

            for i in range(30):

                letter = random.choice(chars)

                obj = self.canvas.create_text(
                    x,
                    start + i * 22,
                    text=letter,
                    fill="#003300",
                    font=("Consolas", 10)
                )

                column.append(obj)

                self.matrix.append(column)

    def create_terminal(self):

        self.canvas.create_rectangle(
            20,
            20,
            WIDTH - 20,
            HEIGHT - 20,
            outline=GREEN,
            width=2
        )

        self.canvas.create_text(
            45,
            45,
            text="Windows Terminal",
            fill=GREEN,
            anchor="w",
            font=("Consolas", 18, "bold")
        )

        self.canvas.create_text(
            45,
            80,
            text="C:\\Users\\Ian>",
            fill=GREEN,
            anchor="w",
            font=("Consolas", 16)
        )
        def animate(self):
            for star in self.stars:
                self.canvas.move(star, 0, 1)

        x1, y1, x2, y2 = self.canvas.coords(star)

        if y1 > HEIGHT:
            nx = random.randint(0, WIDTH)

            self.canvas.coords(
                star,
                nx,
                0,
                nx + 2,
                2
            )

        chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for column in self.matrix:

            for obj in column:

                self.canvas.move(obj, 0, 4)

                x, y = self.canvas.coords(obj)

                if y > HEIGHT:

                    self.canvas.coords(obj, x, -20)

                if random.random() < 0.02:

                    self.canvas.itemconfig(
                        obj,
                        text=random.choice(chars)
                    )

        self.root.after(30, self.animate)
self.cursor_state = True

        self.create_background()
        self.create_terminal()

        self.animate()

        self.root.mainloop()
        
        self.root = tk.Tk()

        self.root.title("Windows Terminal")

        self.root.geometry(f"{WIDTH}x{HEIGHT}")

        self.root.configure(bg=BG)

        self.canvas = tk.Canvas(
            self.root,
            width=WIDTH,
            height=HEIGHT,
            bg=BG,
            highlightthickness=0
        )

        self.canvas.pack(fill="both", expand=True)

        self.stars = []

        self.matrix = []

        self.lines = []

        self.cursor = None

        self.cursor_state = True

        if __name__ == "__main__":
    run_popups()
    HackerTerminal()
