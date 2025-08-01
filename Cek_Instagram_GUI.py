import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def load_json_file(title):
    path = filedialog.askopenfilename(title=title, filetypes=[("JSON files", "*.json")])
    if not path:
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membuka file:\n{e}")
        return None

def extract_followers(data):
    followers = []
    for item in data:
        for user in item.get("string_list_data", []):
            followers.append(user.get("value", ""))
    return followers

def extract_following(data):
    following = []
    for item in data.get("relationships_following", []):
        for user in item.get("string_list_data", []):
            following.append(user.get("value", ""))
    return following

def compare_lists():
    txt_output.delete("1.0", tk.END)

    followers_data = load_json_file("Pilih file followers_1.json")
    if followers_data is None:
        return

    following_data = load_json_file("Pilih file following.json")
    if following_data is None:
        return

    followers = extract_followers(followers_data)
    following = extract_following(following_data)

    not_following_back = [user for user in following if user not in followers]

    if not not_following_back:
        txt_output.insert(tk.END, "Semua akun yang kamu follow sudah follow kamu balik.\n")
    else:
        txt_output.insert(tk.END, "Akun yang kamu follow tapi tidak follow kamu balik:\n\n")
        for user in not_following_back:
            txt_output.insert(tk.END, f"https://www.instagram.com/{user}\n")

# GUI setup
root = tk.Tk()
root.title("Cek Followers Instagram")
root.geometry("600x500")

btn_check = tk.Button(root, text="Mulai Cek Followers", command=compare_lists, font=('Arial', 12))
btn_check.pack(pady=10)

txt_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=('Courier New', 10))
txt_output.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()
