def exercise_1_basics():
    course = "124"
    students = 10
    print(f"The course {course} has {students} students.")

def exercise_2_collections():
    my_list = ["red", "orange", "pink", "gray", "white"]
    my_list.append("green")

    student = {
        "name": "Eric",
        "gpa": 3.9
    }
    print(my_list)
    print(student)



def exercise_3_logic(): 
    numbers = [1,2,3,4,5,6,7,8,9,10]
    even = []
    for i in numbers:
        if i % 2 == 0: 
           even.append(i)
        else: continue

    print(even)



if __name__ == "__main__":
    print("--- Exercise 1 ---")
    exercise_1_basics()
    print("\n--- Exercise 2 ---")
    exercise_2_collections()
    print("\n--- Exercise 3 ---")
    exercise_3_logic()
