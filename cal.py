from stemlet import app, input, output

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    elif percentage >= 40:
        return 'E'
    else:
        return 'F'

# Function to generate result cards for multiple students
@app.route('/')
def generate_result_cards():
    output.text("Mudassir Result Builder")
    
    num_students = input.number("Enter the number of students:")
    students_results = []
    total_marks_dict = {}  # Dictionary to store total marks (asked only once)

    for i in range(num_students):
        output.text(f"\n--- Enter details for Student {i + 1} ---")
        student_name = input.text(f"Enter student's name {i + 1}:")

        total_marks = 0  # Initialize total marks to 0
        obtained_marks = 0
        subjects = {}

        # Get marks for each subject, ask for total marks only once
        for subject in ['English', 'Conversation', 'Islamiat', 'Urdu', 'Math', 'Science', 'SST']:
            if subject not in total_marks_dict:
                subject_total = input.number(f"Enter total marks for {subject}:")
                total_marks_dict[subject] = subject_total

            marks_obtained = input.number(f"Enter marks obtained in {subject} (out of {total_marks_dict[subject]}):")
            if 0 <= marks_obtained <= total_marks_dict[subject]:
                subjects[subject] = marks_obtained
                obtained_marks += marks_obtained
                total_marks += total_marks_dict[subject]  # Update total possible marks

        # Calculate percentage and grade
        percentage = (obtained_marks / total_marks) * 100
        grade = calculate_grade(percentage)

        # Store each student's results in a list
        students_results.append((student_name, obtained_marks, percentage, grade))

    # Sort students by percentage to determine rank
    students_results.sort(key=lambda x: x[2], reverse=True)

    # Display result cards with ranks
    output.text("\n--------- All Students Result Cards ---------")
    for rank, (name, obtained, percentage, grade) in enumerate(students_results, start=1):
        output.text("\n--------- Result Card ---------")
        output.text(f"Student Name: {name}")
        output.text(f"Total Marks: {total_marks}")  # Display the total possible marks
        output.text(f"Obtained Marks: {obtained}")
        output.text(f"Percentage: {percentage:.2f}%")
        output.text(f"Grade: {grade}")
        output.text(f"Rank: {rank}")
        output.text("--------------------------------")

# Run the app
if __name__ == "__main__":
    app.run()
