def input_grades():
    grades = {}
    num_subjects = int(input("Enter the number of subjects: "))
    
    for _ in range(num_subjects):
        subject = input("Enter the subject name: ")
        num_grades = int(input(f"Enter the number of grades for {subject}: "))
        subject_grades = []
        
        for _ in range(num_grades):
            grade = float(input(f"Enter a grade for {subject}: "))
            subject_grades.append(grade)
        
        grades[subject] = subject_grades
    
    return grades

def calculate_averages(grades):
    averages = {}
    total_sum = 0
    total_count = 0
    
    for subject, subject_grades in grades.items():
        subject_average = sum(subject_grades) / len(subject_grades)
        averages[subject] = subject_average
        total_sum += sum(subject_grades)
        total_count += len(subject_grades)
    
    overall_average = total_sum / total_count if total_count > 0 else 0
    return averages, overall_average

def main():
    grades = input_grades()
    subject_averages, overall_average = calculate_averages(grades)
    
    print("\nSubject Averages:")
    for subject, average in subject_averages.items():
        print(f"{subject}: {average:.2f}")
    
    print(f"\nOverall Average: {overall_average:.2f}")

if __name__ == "__main__":
    main()
