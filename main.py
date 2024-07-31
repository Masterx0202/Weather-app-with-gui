import customtkinter as ctk
import temperature as tmp

def on_submit():
    user_input = entry.get()
    temp_value = tmp.temp(user_input)
    label.configure(text="Temperature: " + str(temp_value) + "°C")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Weather")


entry = ctk.CTkEntry(root, width=300, placeholder_text="Enter your city here")
entry.pack(pady=20)


label = ctk.CTkLabel(root, text="")
label.pack(pady=20)

submit_button = ctk.CTkButton(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()
