import tkinter as tk
import settings
import random
class Cell:
    all_cells = []
    cell_count = settings.CELL_COUNT
    cell_count_label = None
    def __init__(self,x,y,is_mine=False):
        self.is_mine = is_mine
        self.cell_button_obj = None
        self.x = x
        self.y = y
        self.flag = 0
        self.is_open = False
        Cell.all_cells.append(self)

    def create_cell(self, location):
        button = tk.Button(location, text = f"{self.x},{self.y}", width = 12 , height = 4 )
        self.cell_button_obj = button
        button.bind('<Button-1>', self.left_clicked)
        button.bind('<Button-3>', self.right_clicked)

    @staticmethod
    def create_cell_count_label(location):
        lbl = tk.Label(location, bg="black", fg = 'white', text = f"cells left:{Cell.cell_count}")
        Cell.cell_count_label = lbl


    def left_clicked(self,event):
        print('left clicked')
        if self.is_mine :
            self.show_mine()
        else:
            if self.surrounded_mines_count == 0 :
                print(self.__str__(), "is zero")
                for cell in self.surrounded_cells:
                    cell.show_mine_count()
                    print("end of neighbour mines")

                    if cell.surrounded_mines_count == 0:
                        print(cell.__str__() , "is zero")
                        # for cell2 in cell.surrounded_cells:
                        #     print("showing next neighbours of ",cell.__str__() )
                        #     cell2.show_mine_count()
                        #     print("end of neighbour mines")
                        #     if cell2.surrounded_mines_count==0 and  cell2.flag == 0 :
                        self.flag = 1
                        self.zero_count(cell)

            self.show_mine_count()
    def zero_count(self,s_cell):
        # print("recursive")
        s_cell.flag = 1
        # print(f"flsg set to 1 {s_cell.__str__()}")
        #if s_cell.surrounded_mines_count == 0 :
        for cell in s_cell.surrounded_cells:
            print("showing next neighbours of ", s_cell.__str__())
            cell.show_mine_count()
            print("end of neighbour mines")
            if cell.surrounded_mines_count==0  and cell.flag == 0 :
                print(cell.__str__(), "is zero")
                s_cell.zero_count(cell)




    def show_mine(self):
        self.cell_button_obj.configure(bg="red")



    def get_cell_by_axis(self,x,y):
        for cell in Cell.all_cells:
            if cell.x == x and cell.y ==y:
                return cell


    @property
    def surrounded_cells(self):

        cells = []
        n = self.x -1
        m = self.y -1
        for i in range(0, 3):
            for j in range(0, 3):
                if n+i== self.x and m+j == self.y:
                    continue

                cells.append(self.get_cell_by_axis(n+i,m+j))
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_mines_count(self):

        count = 0
       # mine_cells=[]
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count+=1
        return count





    def show_mine_count(self):


        print(f"surrounding ", {self.__str__()})
        for cell in self.surrounded_cells:
           print(cell.__str__())
        # if self.surrounded_cells == 0:
        #     self.show_mine_count()

        if not self.is_open:
            Cell.cell_count -= 1
            print(Cell.cell_count)
            self.cell_button_obj.configure(bg='white', text=self.surrounded_mines_count)
            if Cell.cell_count_label:
                Cell.cell_count_label.configure(bg="black", fg='white', text=f"cells left:{Cell.cell_count}")

        self.is_open = True


    def right_clicked(self,event):
        print(event)
        print('right clicked')

    @staticmethod
    def randomize_mines():
        mines = random.sample(Cell.all_cells, settings.MINES_COUNT)
        for mine in mines:
            mine.is_mine = True

    def __str__(self):
        return f"{self.x} , {self.y}"

