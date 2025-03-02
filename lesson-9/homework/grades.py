import csv

# Read data from CSV
def read_grades(filename):
    grades = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

# Calculate average grade for each subject
def calculate_average(grades):
    subject_grades = {}
    
    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        
        if subject not in subject_grades:
            subject_grades[subject] = []
        
        subject_grades[subject].append(grade)

    averages = {subject: sum(marks) / len(marks) for subject, marks in subject_grades.items()}
    return averages

# Write the average grades to a new CSV file
def write_average_grades(averages, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

# Execution
grades = read_grades('grades.csv')
average_grades = calculate_average(grades)
write_average_grades(average_grades, 'average_grades.csv')

print("Average grades saved to 'average_grades.csv'.")