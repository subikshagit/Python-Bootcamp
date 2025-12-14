from re import split
from tkinter import *
import requests 

para ={
    "lat":55.378052,
    "lng":-3.435973,
    "formatted":0,
}

def get_quote():
    response = requests.get("https://api.sunrise-sunset.org/json", params=para)
    data = response.json()
    quote = data["results"]["sunrise"]  # Placeholder for actual quote extraction
    quote2 = data["results"]["sunset"]  # Placeholder for actual quote extraction
    print(quote.split("T")[1])
    print(quote2.split("T")[1])
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()