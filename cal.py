import streamlit as st

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
def generate_result_cards():
    st.title("Mudassir Result Builder")
    
    num_students = st.number_input("Enter the number of students:", min_value=1, step=1)
    
    students_results = []
    total_marks_dict = {}  # Dictionary to store total marks (asked only once)

    for i in range(num_students):
        st.header(f"--- Enter details for Student {i + 1} ---")
        student_name = st.text_input(f"Enter student's name {i + 1}:")

        total_marks = 0  # Initialize total marks to 0
        obtained_marks = 0
        subjects = {}

        # Get marks for each subject, ask for total marks only once
        for subject in ['English', 'Conversation', 'Islamiat', 'Urdu', 'Math', 'Science', 'SST']:
            if subject not in total_marks_dict:
                subject_total = st.number_input(f"Enter total marks for {subject}:", min_value=1)
                total_marks_dict[subject] = subject_total

            marks_obtained = st.number_input(f"Enter marks obtained in {subject} (out of {total_marks_dict[subject]}):", min_value=0, max_value=total_marks_dict[subject])
            subjects[subject] = marks_obtained
            obtained_marks += marks_obtained
            total_marks += total_marks_dict[subject]  # Update total possible marks

        # Calculate percentage and grade
        if total_marks > 0:  # Avoid division by zero
            percentage = (obtained_marks / total_marks) * 100
            grade = calculate_grade(percentage)

            # Store each student's results in a list
            students_results.append((student_name, obtained_marks, percentage, grade))

    # Sort students by percentage to determine rank
    students_results.sort(key=lambda x: x[2], reverse=True)

    # Display result cards with ranks
    st.subheader("--------- All Students Result Cards ---------")
    for rank, (name, obtained, percentage, grade) in enumerate(students_results, start=1):
        st.markdown(f"### Result Card for {name}")
        st.write(f"Obtained Marks: {obtained}")
        st.write(f"Percentage: {percentage:.2f}%")
        st.write(f"Grade: {grade}")
        st.write(f"Rank: {rank}")
        st.markdown("---")

# Run the app
if __name__ == "__main__":
    generate_result_cards()
