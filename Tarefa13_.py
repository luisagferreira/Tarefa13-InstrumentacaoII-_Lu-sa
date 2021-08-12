from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import conversao as conv
from tkinter import messagebox

janela=tk.Tk()
janela.title("Tarefa 13(Instrumentação II)_Luísa")
janela.geometry("620x250")
janela.resizable(0,0)
janela.configure(bg='magenta',background='pink')

temp_label=tk.Label(janela, text="Digite a Temperatura", bg="white")
temp_label.grid(row=0,column=0,pady=20,padx=50)
temperatura=tk.StringVar()
temp_ent=ttk.Entry(janela,width=25,textvariable=temperatura)
temp_ent.grid(row=0,column=1)
temp_ent.focus()

unit_label=tk.Label(janela,text="Selecione a unidade: ",bg="white")
unit_label.grid(row=1,column=0)
unit=tk.StringVar()
unit_box=ttk.Combobox(janela,width=23,textvariable=unit,state="readonly")
unit_box["values"]=("Celsius", "Fahrenheit","Kelvin")
unit_box.current(0)
unit_box.grid(row=1,column=1)

unit1=tk.StringVar()
unit_box1=ttk.Combobox(janela,width=23,textvariable=unit1,state="readonly")
unit_box1["values"]=("Celsius", "Fahrenheit","Kelvin")
unit_box1.current(1)
unit_box1.grid(row=2,column=1,padx=50,pady=20)

ans_label=tk.Label(janela,text="Resultado da conversão: ", bg='white')
ans_label.grid(row=3,column=0)

def converter():

    try:
        if len(temperatura.get())<8:
            ans=conv.converter(int(temperatura.get()),unit.get(),unit1.get())
            global ans_frame
            ans_frame=tk.Frame(janela,width=50,height=50)
            ans_frame.grid(row=3,column=1)
            win=tk.Label(ans_frame,text=f"{round(ans)} {unit1.get()}",background='cyan')
            win.grid(row=0,column=0)
        else:
            messagebox.showerror("Erro", "O limite de entrada é 7")

    except:
            messagebox.showerror("Erro", "Verifique se digitou um valor. Além disso, verifique se as unidades são diferentes!")
def clear():
    ans_frame.destroy()
    pass
def close_window():
    janela.destroy()
    pass
convert_btn=ttk.Button(janela,text="Converter", command=converter,cursor="heart")
convert_btn.grid(row=1,column=2)

clear_btn=ttk.Button(janela,text="Limpar", command=clear,cursor="heart")
clear_btn.grid(row=3,column=2,pady=10)

exit_btn=ttk.Button(text = "Fechar janela", command = close_window,cursor="heart")
exit_btn.grid(row=5,column=1, pady=10)

janela.mainloop()