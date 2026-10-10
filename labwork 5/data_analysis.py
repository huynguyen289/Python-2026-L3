import pandas as po

students = po.read_csv("students.csv")
scores = po.read_csv("scores.csv")

#2 Missing values
print("\nMissing values in students: ")
print(students.isnull().sum())
print("\nMissing values in scores: ")
print(scores.isnull().sum())


#3
students["age"] = students["age"].fillna(students["age"].mean())
students["GPA"] = students["GPA"].fillna(students["GPA"].mean())

scores["math"] = scores["math"].fillna(scores["math"].mean())
scores["database"] = scores["database"].fillna(scores["database"].mean())

#4
data = po.merge(students, scores, on = "student_id")
print("\nMerged data: ")
print(data.head())
#5
data["average_score"] = data[["python", "math", "database"]].mean(axis=1)
print("\nStudents with average score:")
print(data[["student_id", "name", "average_score"]])

#6
top_5 = data.sort_values(
    by="average_score",
    ascending=False
).head(5)

print("\nTop 5 students:")
print(top_5[["student_id", "name", "average_score"]])

#7
average_data_major = data.groupby("major")["average_score"].mean()
print("\nAverage score by major: ")
print(average_data_major)
