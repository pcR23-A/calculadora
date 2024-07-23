import tkinter as tk

tela = tk.Tk()
tela.geometry = ("312x324")
tela.title = ("Calculadora")
def click(item):
    global expression
    expression =  expression + str(item)
    input_texto.set(expression)
def limpar():
    global expression
    expression = ""
    input_texto.set("")
def igual():
    global expression
    result = str(eval(expression))
    input_texto.set(result)
    expression = ""
expression=""
input_texto=tk.StringVar()
telacalc = tk.Frame(
    tela,
    width=312,
    height=50,
    bd=0,
    highlightbackground="black",
    highlightcolor="black",
    highlightthickness=1
)
telacalc.pack(side="top")
input_tela = tk.Entry(
    telacalc,
    font = ('arial', 17),
    textvariable = input_texto, 
    bg="#eee", 
    bd=0, 
    justify="right",
    width=23
)
input_tela.grid(row=0, column=0)
input_tela.pack(ipady=10)
botoes = tk.Frame(
    tela,
    width=312,
    height=272.5,
    bg="grey"
)
botoes.pack()

btlimpar = tk.Button(
    botoes,
    text = "C",
    fg = "black",
    width = 32,
    height = 3,
    bd = 0, 
    bg = "#eee", 
    cursor = "hand2",
    command = lambda: limpar()).grid(
        row = 0, 
        column = 0, 
        columnspan = 3, 
        padx = 1, 
        pady = 1)
divisao = tk.Button(
    botoes,
    text = "÷",
    fg = "black",
    width = 10,
    height = 3,
    bd = 0, 
    bg = "#eee", 
    cursor = "hand2", 
    command = lambda: click("/")).grid(
        row = 0,
        column = 3,
        padx = 1,
        pady = 1
        )
sete = tk.Button(
    botoes,
    text = "7",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(7)).grid(
        row = 1,
        column = 0,
        padx = 1,
        pady = 1
    )
oito = tk.Button(
    botoes,
    text = "8",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(8)).grid(
        row = 1,
        column = 1,
        padx = 1,
        pady = 1
    )
nove = tk.Button(
    botoes,
    text = "9",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(9)).grid(
        row = 1,
        column = 2,
        padx = 1,
        pady = 1
    )
vezes = tk.Button(
    botoes,
    text = "×",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#eee",
    cursor="hand2",
    command=lambda: click("*")).grid(
        row = 1,
        column = 3,
        padx=1,
        pady=1
    )

quatro = tk.Button(
    botoes,
    text = "4",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(4)).grid(
        row = 2,
        column = 0,
        padx = 1,
        pady = 1
    )
cinco = tk.Button(
    botoes,
    text = "5",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(5)).grid(
        row = 2,
        column = 1,
        padx = 1,
        pady = 1
    )
seis = tk.Button(
    botoes,
    text = "6",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
command=lambda: click(6)).grid(
    row = 2,
    column = 2,
    padx = 1,
    pady = 1
)
menos = tk.Button(
    botoes,
    text = "-",
    fg="black",
    width=10,
    height=3,
    bd=0,
    bg="#eee",
    cursor="hand2",
    command=lambda: click("-")).grid(
        row = 2,
        column = 3,
        padx=1,
        pady=1
    )
um = tk.Button(
    botoes,
    text = "1",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(1)).grid(
        row = 3,
        column = 0,
        padx = 1,
        pady = 1
    )
dois = tk.Button(
    botoes,
    text = "2",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(2)).grid(
        row = 3,
        column = 1,
        padx = 1,
        pady = 1
)
tres = tk.Button(
    botoes,
    text = "3",
    fg = "black",
    width = 10,
    height=3,
    bd=0,
    bg="#fff",
    cursor="hand2",
    command=lambda: click(3)).grid(
        row = 3,
        column = 2,
        padx = 1,
        pady = 1
)
mais = tk.Button(
    botoes,
    text = "+",
    fg = "black",
    width = 10,
    height = 3,
    bd = 0,
    bg = "#eee",
    cursor = "hand2",
    command = lambda: click("+")).grid(
        row = 3,
        column = 3,
        padx = 1,
        pady = 1
    )
zero = tk.Button(
    botoes,
    text = "0",
    fg = "black",
    width = 21,
    height = 3,
    bd = 0,
    bg = "#fff",
    cursor = "hand2",
    command = lambda: click(0)).grid(
        row=4,
        column=0,
        columnspan=2,
        padx=1,
        pady=1,
    )
point = tk.Button(botoes, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
btigual = tk.Button(
    botoes,
    text = "=",
    fg = "black",
    width=10,
    height=3,
    bd = 0,
    bg = "#00a1f1",
    cursor = "hand2",
    command = lambda: igual()).grid(
        row = 4,
        column = 3,
        padx=1,
        pady=1
    )


tela.resizable(False,False)
tela.mainloop()