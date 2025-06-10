import numpy as np #installed
import os
import re
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps #installed

class DrawingApp:
    def __init__(self, master):
        self.master = master #links window to the class instance
        self.master.title("Handwritten_Text(28x28)")

        self.canvas_size = 280 # size is 280x280 pixels for convenience
        self.canvas = tk.Canvas(master,
                                bg = "white",
                                width = self.canvas_size,
                                height = self.canvas_size) #creates canvas
        self.image = Image.new("L",
                               (self.canvas_size, self.canvas_size),
                               255) #creates an image in memory, we don't directly interact with it yet
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint) #draw when left mouse button is held down
        self.canvas.bind("<Button-1>", self.paint) #draw a point if the button is just pressed

        btn_frame = tk.Frame(master) #for the following buttons to be within the window frame
        btn_frame.pack(side = tk.LEFT)

        clear_btn = tk.Button(btn_frame, text = "Clear", command = self.clear)
        clear_btn.pack(side = tk.LEFT)

        save_btn = tk.Button(btn_frame, text = "Save", command = self.save)
        save_btn.pack(side = tk.LEFT)

        close_btn = tk.Button(btn_frame, text="Save & Close", command=self.save_and_close)
        close_btn.pack(side=tk.LEFT)

    def clear(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, self.canvas_size, self.canvas_size], fill=255)

    def paint(self, event):
        x, y = event.x, event.y
        r = 12
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill=0)

    def save_and_close(self):
        self.save()
        self.master.destroy()

    def save(self):
        save_folder = "data"
        if not os.path.exists(save_folder):  #to make sure folder exists
            os.makedirs(save_folder)

        #to save files with certain naming system – e.g. image001.png – there's a following algorithm

        filename_pattern = re.compile(r"^image(\d+)\.png$")  #pattern for recognition of filenames

        existing_files = os.listdir(save_folder) #looks for all the files in folder "data"
        existing_file_numbers = [] #will store numbers in names of files

        for f in existing_files:
            match = filename_pattern.match(f)
            if match:
                existing_file_numbers.append(int(match.group(1))) #extracts number from filenames

        if existing_file_numbers: #gives the new image a number
            new_file_number = max(existing_file_numbers) + 1
        else: new_file_number = 1


        filename = f"image{new_file_number:04}.png"

        save_path = os.path.join(save_folder, filename)

        if self.is_empty():
            print("Nothing was written, image not saved.")
            return

        resized = self.image.resize((28, 28), Image.Resampling.LANCZOS)
        inverted = ImageOps.invert(resized) #inverts picture to black-and-white
        inverted.save(save_path)
        print(f"Saved as {filename}")

    def is_empty(self):
        # Convert the image to a numpy array - grayscale values; wanted to use get_data(), but got a warning
        np_image = np.array(self.image)
        # Check if all pixels are 255 (white)
        return np.all(np_image == 255)

root = tk.Tk() #creates the window to work in
root.eval('tk::PlaceWindow . center')
root.attributes('-topmost',True)  #for starting toplevel window on macOS
app = DrawingApp(root) #passes window to DrawingApp class
root.mainloop() #starts tkinter even loop