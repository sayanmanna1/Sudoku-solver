from tkinter import *

root = Tk()
root.geometry("1000x700")
root.config(bg="black")
root.title("Sudoku")

matrix =[]
for r in range(9):
    e=[]
    for c in range(9):
        e.append(Entry(root,width=4,borderwidth=5,font=("Helvetica",20)))
    matrix.append(e)

for r in range(9):
    for c in range(9):
        matrix[r][c].grid(row=r,column=c,padx=10,pady=10)

def click():
    puzzle=[]
    for r in range(9):
        x=[]
        for c in range(9):
            x.append(int(matrix[r][c].get()))
        puzzle.append(x)

    def check_empty(puzzle):
        for r in range(9):
            for c in range(9):
                if puzzle[r][c]==-1:
                    return r,c
        return None,None

    def is_valid(puzzle,guess,row,col):
        row_vals = puzzle[row]
        if guess in row_vals:
            return False
        col_vals = []
        col_vals =[puzzle[i][col] for i in range(9)]
        if guess in col_vals:
            return False
        
        row_start = (row//3)*3
        col_start = (col//3)*3
        for r in range(row_start,row_start+3):
            for c in range(col_start,col_start+3):
                if guess==puzzle[r][c]:
                    return False
        else:
            return True

    def solve(puzzle):
        row,col = check_empty(puzzle)
        if row is None:
            return True
        for guess in range(1,10):
            if is_valid(puzzle,guess,row,col)==True:
                puzzle[row][col]=guess
                if solve(puzzle)==True:
                    return True
            puzzle[row][col]=-1 
        return False

    solve(puzzle)
    for r in range(9):
        for c in range(9):
            matrix[r][c].delete(0,END)
            matrix[r][c].insert(0,puzzle[r][c])
    
mybutton = Button(root,text="Submit",command=click)
mybutton.grid(row=10,column=4)
button_quit = Button(root,text="Exit",command=root.quit)
button_quit.grid(row=11,column=4)


root.mainloop()


