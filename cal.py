from stemlet import *

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
def generate_result_cards(num_students, students_data):
    total_marks_dict = {}
    students_results = []

    for i in range(num_students):
        student_name = students_data[i]['name']
        obtained_marks = 0
        total_marks = 0

        # Get marks for each subject
        for subject in ['English', 'Conversation', 'Islamiat', 'Urdu', 'Math', 'Science', 'SST']:
            subject_total = students_data[i][subject]['total']
            marks_obtained = students_data[i][subject]['obtained']
            obtained_marks += marks_obtained
            total_marks += subject_total  # Update total possible marks

            # Store each student's results
            students_results.append((student_name, obtained_marks, total_marks))

    # Sort students by obtained marks
    students_results.sort(key=lambda x: x[1], reverse=True)

    result_cards = []
    for rank, (name, obtained, total) in enumerate(students_results, start=1):
        percentage = (obtained / total) * 100
        grade = calculate_grade(percentage)
        result_cards.append({
            'name': name,
            'obtained': obtained,
            'total': total,
            'percentage': percentage,
            'grade': grade,
            'rank': rank
        })

    return result_cards

# Stemlet UI
def app():
    title("MUDASSIR AHMED CALCULATOR")

    num_students = input("Enter the number of students:")
    num_students = int(num_students)
    
    students_data = []

    for i in range(num_students):
        student_name = input(f"Enter student's name {i + 1}:")
        subjects = {}
        for subject in ['English', 'Conversation', 'Islamiat', 'Urdu', 'Math', 'Science', 'SST']:
            total_marks = int(input(f"Enter total marks for {subject}:"))
            obtained_marks = int(input(f"Enter marks obtained in {subject} (out of {total_marks}):"))
            subjects[subject] = {'total': total_marks, 'obtained': obtained_marks}
        
        students_data.append({'name': student_name, **subjects})

    result_cards = generate_result_cards(num_students, students_data)

    # Display results
    for card in result_cards:
        print("\n--------- Result Card ---------")
        print(f"Student Name: {card['name']}")
        print(f"Obtained Marks: {card['obtained']}")
        print(f"Total Marks: {card['total']}")
        print(f"Percentage: {card['percentage']:.2f}%")
        print(f"Grade: {card['grade']}")
        print(f"Rank: {card['rank']}")
        print("--------------------------------")

if __name__ == "__main__":
    app()
