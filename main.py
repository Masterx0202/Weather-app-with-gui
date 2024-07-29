import customtkinter as ctk
import temperature as tmp


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("CTkLabel Example")

label = ctk.CTkLabel(root, text=tmp.temp("london"))
label.pack(pady=20)

root.mainloop()
