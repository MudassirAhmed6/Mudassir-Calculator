import streamlit as st

def calculate_grade(percentage):
    # ... (same as before)

def main():
    st.title("Mudassir Result Builder")

    num_students = st.number_input(...)

    # ... (rest of the code)

    if st.button("Show All Results"):
        if students_results:
            # Sort by percentage in descending order
            students_results.sort(key=lambda x: x[3], reverse=True)

            st.write("### All Students Result Cards:")
            for rank, (name, obtained, total, percentage, grade) in enumerate(students_results, start=1):
                # ... (display results as before)

                # Consider adding a visual representation, e.g., a progress bar
                st.progress(percentage / 100)

if __name__ == "__main__":
    main()
        
