from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text

root = Tk()
root.geometry("600x675")
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#6F8FAF")#modifies wideget attributes


def send():
    send = entry.get()
    if send.strip() == "":
        text.insert(END, "Me --> (empty input)\n")
        return

    text.insert(END, "Me --> " + send + "\n")

    bot = action.Action(send)

    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")

    if bot == "ok sim":
        root.destroy()


def ask():
    ask_val = speech_to_text.speech_to_text()

    if ask_val is not None:
        text.insert(END, "Me --> " + ask_val + "\n")
        bot_val = action.Action(ask_val)

        if bot_val is not None:
            text.insert(END, "Bot <-- " + str(bot_val) + "\n")

        if bot_val == "ok sim":
            root.destroy()
    else:
        text.insert(END, "Me --> (couldn't understand)\n")


def delete():
    text.delete("1.0", "end")
#FRAME
frame = LabelFrame(root, padx = 120, pady = 7 ,borderwidth= 3, relief="raised")
frame.config(bg = "#F5F5F5")
frame.grid(row = 0, column = 1 , padx = 55 , pady = 10)

text_label = Label(frame, text = "AI Assistant" , font =("Arrus BT" , 20 , "bold"), bg = "Light Sky Blue")
text_label.grid(row = 0, column = 0 , padx = 20 , pady = 10)

#image
image = ImageTk.PhotoImage(Image.open("/Users/administrator/AI Assistant Python & Tkinter/image/assitant.png"))
image_label = Label(frame, image=image)
image_label.grid(row = 1, column = 0 , pady = 20)

#textbox
text=Text(root , font= ("Courier" ,10 , "bold") , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 115, y= 375, width= 375, height= 100)

#entry
entry = Entry(root, justify= CENTER)
entry.place(x = 120 , y = 500 , width = 350 , height = 30)

#button1
button_1 = Button(root, text= "ASK" , bg= "#FFFFFF", pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button_1.place(x= 70, y= 575)

#button2
button_2 = Button(root, text= "SEND" , bg= "#FFFFFF", pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=send)
button_2.place(x= 400, y= 575)

#button3
button_2 = Button(root, text= "DELETE" , bg= "#FFFFFF", pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=delete)
button_2.place(x= 225, y= 575)


root.mainloop()
