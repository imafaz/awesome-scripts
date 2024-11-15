import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    """Generates a random password of fixed length."""
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_files():
    try:
        user_count = int(entry_user_count.get())
        profile_name = entry_profile_name.get()
        shared_user = int(entry_shared_user.get())
        username_start_with = entry_username_start_with.get()
        password_count = int(entry_password_count.get())

        with open("mikrotik.rsc", "w") as rsc_file, open("user.txt", "w") as user_file:
            for i in range(1, user_count + 1):
                password = generate_password(password_count)
                username = f"{username_start_with}{i}"
                rsc_file.write(f"/user-manager user add name={username} password={password} shared-users={shared_user}\n")
                rsc_file.write(f"/user-manager user-profile add profile={profile_name} user={username}\n")
                user_file.write(f"User: {username}   --->  Password: {password}\n")

        messagebox.showinfo("Success", "Files created successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid inputs!")

root = tk.Tk()
root.title("User Generator")

tk.Label(root, text="User Count:").grid(row=0, column=0)
entry_user_count = tk.Entry(root)
entry_user_count.grid(row=0, column=1)

tk.Label(root, text="Profile Name:").grid(row=1, column=0)
entry_profile_name = tk.Entry(root)
entry_profile_name.grid(row=1, column=1)

tk.Label(root, text="Shared User:").grid(row=2, column=0)
entry_shared_user = tk.Entry(root)
entry_shared_user.grid(row=2, column=1)

tk.Label(root, text="Username Start With:").grid(row=3, column=0)
entry_username_start_with = tk.Entry(root)
entry_username_start_with.grid(row=3, column=1)

tk.Label(root, text="Password Count:").grid(row=4, column=0)
entry_password_count = tk.Entry(root)
entry_password_count.grid(row=4, column=1)


btn_submit = tk.Button(root, text="Submit", command=create_files)
btn_submit.grid(row=5, columnspan=2)

root.mainloop()
