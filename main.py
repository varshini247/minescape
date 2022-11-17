import tkinter as tk
import utils as u
from cell import Cell
import settings

root = tk.Tk()
#window configuration
root.configure(bg="black")
root.geometry('800x720')
root.title("Minesweeper Game")
root.resizable(False,False)

#frames
top_frame = tk.Frame(root, bg = "blue", height = u.h_percent(25), width = u.w_percent(100) )
top_frame.place(x=0,y=0)

left_frame = tk.Frame(root,bg = "green", height = u.h_percent(75), width = u.w_percent(25))
left_frame.place(x=0, y=u.h_percent(25))

center_frame = tk.Frame(root, bg = "yellow" , height = u.h_percent(75), width = u.w_percent(75))
center_frame.place(x=u.w_percent(25), y=u.h_percent(25))

for i in range(settings.GRID_SIZE):
    for j in range(settings.GRID_SIZE):
        cell = Cell(i,j)
        cell.create_cell(center_frame)
        cell.cell_button_obj.grid(row = i, column=j)

print(Cell.surrounded_cells)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=0,y=0)


Cell.randomize_mines()

root.mainloop()
