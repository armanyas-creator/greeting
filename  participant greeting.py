import tkinter as tk
from datetime import datetime


def check_in():
  name = entry_name.get().strip()

  if not name:
    message = "Please enter your name."
  else:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        f"Welcome to the workshop, {name}!\n"
        f"Check-In Date/Time: {current_date}\n"
        f"Status: Registered Successfully"
    )

  text_output.delete("1.0", tk.end)
  text_output.insert(tk.end, message)

root = tk.Tk()
root.title("Workshop Participant Greeting")
root.geometry("400x350")

lbl_instruction = tk.Label(
    root, text="Enter your name below and click Check In:", font=("Arial", 11)
)
lbl_instruction.pack(pady=10)

entry_name = tk.Entry(root, width=30, font=("Arial", 11))
entry_name.pack(pady=5)
btn_checkin = tk.Button(
    root, text="Check In", command=check_in, font=("Arial", 10, "bold")
)
btn_checkin.pack(pady=10)

text_output = tk.Text(root, width=45, height=8, font=("Arial", 10))
text_output.pack(pady=10)

root.mainloop()


