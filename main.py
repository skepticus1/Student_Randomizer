import csv
import random
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


print(os.getcwd())

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Team Generator")

        generate_button = tk.Button(self.root, text="Generate Teams", command=self.generate_teams)
        generate_button.pack(pady=35)

        teams_frame = ttk.LabelFrame(self.root, text="Teams")
        teams_frame.pack(pady=35)

        self.teams_text = tk.Text(teams_frame, height=25, width=50)
        self.teams_text.pack()


    def read_csv(self, file):
        with open(file, 'r') as file:
            reader = csv.reader(file)
            students = [row[0] for row in reader]
        return students

    def write_csv(self, file, data):
        with open(file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def create_teams(self, students):
        random.shuffle(students)
        teams = [students[i:i+2] for i in range(0, len(students), 2)]
        return teams

    def generate_teams(self):
        global teams_text
        # input_file = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
        input_file = 'data/students.csv'
        if input_file:
            students = self.read_csv(input_file)
            teams = self.create_teams(students)
            # output_file = filedialog.asksaveasfilename(title="Save Output", defaultextension=".csv", filetypes=[("CSV Files", ".*csv")])
            output_file = 'data/teams.csv'
            if output_file:
                self.write_csv(output_file, teams)
                # messagebox.showinfo("Success", f"Teams have been create and saved to {output_file}")

                with open(output_file, 'r') as file:
                    reader = csv.reader(file)
                    teams_data = list(reader)
                    self.teams_text.delete('1.0', tk.END)
                    for team in teams_data:
                        self.teams_text.insert(tk.END, ', '.join(team) + '\n')

def main():

    root = tk.Tk()
    app = App(root)
    root.mainloop()


    # input_file = 'data/students.csv'
    # output_file = 'data/teams.csv'
    # students = read_csv(input_file)
    # teams = create_teams(students)
    # write_csv(output_file, teams)
    # print(f"Teams have been created and save to {output_file}")

if __name__ == '__main__':
    main()