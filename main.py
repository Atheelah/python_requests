import requests
from tkinter import messagebox
from tkinter import *

root = Tk()
root.geometry("300x300")
root.config(bg="black")
root.title("Chucks Jokes")

def get_chucks_jokes():

    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    return data["value"]


joke = Message(root, text=get_chucks_jokes(), bg="black", fg="#FF10F0", font="20")
joke.place(x=40, y=50)


def refresh():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        jokes = data["value"]
        joke.config(text=get_chucks_jokes())

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "No internet connection")




refreshBtn = Button(root, text="Get Another Joke", borderwidth="3", bg="#FF10F0", command=refresh)
refreshBtn.place(x=60, y=200)

root.mainloop()
