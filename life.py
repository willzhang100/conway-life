from tkinter import *
import time
import copy

class Life:

    def __init__(self, path):
        self.width, self.height = 400, 400
        self.col, self.row = 10, 10
        self.w = 40
        self.p = 5
        self.board = self.build(path)
        self.c = self.setup()
        self.c.pack()

        self.render()
        mainloop()

    def setup(self):
        master = Tk()
        return Canvas(master, width=405, height=405)

    def build(self, path):
        board = []
        with open(path) as f:
            data = f.read()
            for line in data.splitlines():
                cleaned = line.replace(" ", "") # removes all whitespace
                board.append(list(cleaned))
        return board

    def render(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == "1": # the cell is alive
                    self.c.create_rectangle(j*self.w+self.p, i*self.w+self.p, (j+1)*self.w+self.p, (i+1)*self.w+self.p, fill="black")
                else:
                    self.c.create_rectangle(j*self.w+self.p, i*self.w+self.p, (j+1)*self.w+self.p, (i+1)*self.w+self.p, fill="white")
        self.c.after(500, self.generate) # wait 500 ms then generate the new board

    def generate(self):
        nextboard = copy.deepcopy(self.board)
        # only consider the non-border cells
        for i in range(1,self.row-1):
            for j in range(1,self.col-1):
                status = self.board[i][j]
                neighbors = [self.board[i-1][j-1], self.board[i-1][j], self.board[i-1][j+1], self.board[i][j-1], self.board[i][j+1], self.board[i+1][j-1], self.board[i+1][j], self.board[i+1][j+1]]
                alive = neighbors.count("1")
                if status == "1" and alive < 2: # death by underpopulation
                    nextboard[i][j] = "0"
                elif status == "1" and alive > 3: # death by overpopulation
                    nextboard[i][j] = "0"
                elif status == "0" and alive == 3: # birth by reproduction
                    nextboard[i][j] = "1"
        self.board = nextboard
        self.render()

if __name__ == '__main__':
    path = "board_1.txt"
    life = Life(path)
