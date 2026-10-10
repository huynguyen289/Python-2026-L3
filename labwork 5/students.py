import pandas as po
#1
d = po.read_csv("students.csv")
#2
print("First 5 row: ")
print(d.head())
#3
print("\nNumber of rows and columns: ")
print(d.shape)
#4
print("\nName anf GPA: ")
print(d[["name", "GPA"]])
#5
print("GPA >= 3.5: ")
print(d["GPA"] >= 3.5)
#6
print("\nStudents sorted by GPA: ")
print(d.sort_values(by = "GPA", ascending = False))
#7
print("\nAverage GPA by major: ")
print(d.groupby("major")["GPA"].mean())