import tkinter as tk
from tkinter import messagebox

class MusicEventBookingApp:
    def __init__(self, root):      #intial #root=box config
        self.root = root           #access attributes nd methods
        self.root.title("Music Event Ticket Booking")
        self.root.configure(bg="Powder Blue")

        self.singers = ["A.R.Rahman", "VIdhyasagar", "Ilaiyaraja", "Anirudh", "Karthik"]   #to access the singer name
        self.concert_dates = ["16-09-2023", "22-11-2023", "10-12-2023"]
        self.concert_places = ["Chennai-Nehru Stadium", "Coimbatore-Dhoni Stadium", "Salem-Praga Stadium", "Madurai-Sachin Stadium", "Erode-Kongu Indoor Stadium"]
        self.seat_numbers = list(range(1, 500))

        self.selected_singer = tk.StringVar(value=self.singers[0])
        self.selected_date = tk.StringVar(value=self.concert_dates[0])
        self.selected_place = tk.StringVar(value=self.concert_places[0])
        self.selected_seat = tk.StringVar()

        self.label = tk.Label(root, text="Music Concert Ticket Booking", font=("Times", 25, "bold"))
        self.label.pack(pady=20)

        tk.Label(root, text="Select Singer:", bg="Grey", font=("Times", 10, "bold")).pack()
        self.singer_menu = tk.OptionMenu(root, self.selected_singer, *self.singers)
        self.singer_menu.pack()

        tk.Label(root, text="Select Concert Date:", bg="Grey", font=("Times", 10, "bold")).pack()
        self.date_menu = tk.OptionMenu(root, self.selected_date, *self.concert_dates)
        self.date_menu.pack()

        tk.Label(root, text="Select Concert Place:", bg="grey", font=("Times", 10, "bold")).pack()
        self.place_menu = tk.OptionMenu(root, self.selected_place, *self.concert_places)
        self.place_menu.pack()

        tk.Label(root, text="Select Seat Number:", bg="Grey", font=("Times", 10, "bold")).pack()
        self.seat_menu = tk.OptionMenu(root, self.selected_seat, *self.seat_numbers)
        self.seat_menu.pack()

        self.book_button = tk.Button(root, text="Book Ticket", bg="light yellow", font=("Times", 10, "bold"),  command=self.book_ticket)
        self.book_button.pack()

        self.ticket_listbox = tk.Listbox(root)           # Add Listbox to display booked tickets
        self.ticket_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    def book_ticket(self):
        singer = self.selected_singer.get()
        date = self.selected_date.get()
        place = self.selected_place.get()
        seat = self.selected_seat.get()

        ticket_details = f"Singer: {singer}, Date: {date}, Place: {place}, Seat: {seat}"
        self.ticket_listbox.insert(tk.END, ticket_details)

        message = f"Ticket Details:\nSinger: {singer}\nConcert Date: {date}\nConcert Place: {place}\nSeat Number: {seat}"
        messagebox.showinfo("Ticket Booked", message)
        self.root.focus_set()

root = tk.Tk()
app = MusicEventBookingApp(root)
root.mainloop()

