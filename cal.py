import streamlit as st

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

def main():
    st.title("Mudassir Result Builder")

    num_students = st.number_input("Enter the number of students:", min_value=1, value=1, step=1)

    total_marks_dict = {}
    students_results = []

    for i in range(num_students):
        st.subheader(f"--- Enter details for Student {i + 1} ---")
        student_name = st.text_input(f"Enter student's name {i + 1}:", key=f"name_{i}")

        total_marks = 0
        obtained_marks = 0
        subjects = {}

        # Input for subjects
        for subject in ['English', 'Conversation', 'Islamiat', 'Urdu', 'Math', 'Science', 'SST']:
            if subject not in total_marks_dict:
                subject_total = st.number_input(f"Enter total marks for {subject}:", min_value=1, value=100, step=1, key=f"total_{subject}")
                total_marks_dict[subject] = subject_total

            marks_obtained = st.number_input(f"Enter marks obtained in {subject} (out of {total_marks_dict[subject]}):", min_value=0, value=0, step=1, key=f"marks_{i}_{subject}")
            if 0 <= marks_obtained <= total_marks_dict[subject]:
                subjects[subject] = marks_obtained
                obtained_marks += marks_obtained
                total_marks += total_marks_dict[subject]

        # Store results when the user submits data for all students
        if st.button(f"Calculate Result for {student_name}", key=f"calculate_{i}"):
            percentage = (obtained_marks / total_marks) * 100 if total_marks > 0 else 0
            grade = calculate_grade(percentage)

            # Store results for each student
            students_results.append((student_name, obtained_marks, total_marks, percentage, grade))

    # Button to show all results
    if st.button("Show All Results"):
        if students_results:
            students_results.sort(key=lambda x: x[3], reverse=True)  # Sort by percentage
            st.write("### All Students Result Cards:")
            for rank, (name, obtained, total, percentage, grade) in enumerate(students_results, start=1):
                st.write(f"**Student Name:** {name}")
                st.write(f"**Total Marks:** {total}")
                st.write(f"**Obtained Marks:** {obtained}")
                st.write(f"**Percentage:** {percentage:.2f}%")
                st.write(f"**Grade:** {grade}")
                st.write(f"**Rank:** {rank}")
                st.write("---")

if __name__ == "__main__":
    main()
