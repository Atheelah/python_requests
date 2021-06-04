import requests
from tkinter import *

root = Tk()
root.geometry("300x300")
root.config(bg="black")
root.title("Chucks Jokes")

def get_chucks_jokes():

    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    return data["value"]


joke = Message(root, text=get_chucks_jokes(), bg="black", fg="#33FF00", font="20")
joke.place(x=40, y=50)


def refresh():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    jokes = data["value"]
    joke.config(text=get_chucks_jokes())


refreshBtn = Button(root, text="Get Another Joke", borderwidth="3", bg="#33FF00", command=refresh)
refreshBtn.place(x=40, y=180)

root.mainloop()



































#response = requests.get("https://api.chucknorris.io/jokes/random")
#data = response.json()
#print(data["value"])
