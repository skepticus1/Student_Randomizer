import csv
import random
import os

print(os.getcwd())

def read_csv(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        students = [row[0] for row in reader]
    return students

def write_csv(file, data):
    with open(file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def create_teams(students):
    random.shuffle(students)
    teams = [students[i:i+2] for i in range(0, len(students), 2)]
    return teams

def main():
    input_file = 'data/students.csv'
    output_file = 'data/teams.csv'
    students = read_csv(input_file)
    teams = create_teams(students)
    write_csv(output_file, teams)
    print(f"Teams have been created and save to {output_file}")

if __name__ == '__main__':
    main()