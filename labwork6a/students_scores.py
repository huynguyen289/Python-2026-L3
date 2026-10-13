import pandas as po
import matplotlib.pyplot as plt

d = po.read_csv("scores.csv")
plt.scatter(d["math"], d["python"], d["database"])
plt.xlabel("Math scores")
plt.ylabel("Python scores")
plt.title("Math vs Python scores")
plt.savefig("scattered.png")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].hist(d["math"], bins=10)
axes[0].set_title("Math Scores")
axes[0].set_xlabel("Scores")
axes[0].set_ylabel("Number of Students")

axes[1].hist(d["python"], bins=10)
axes[1].set_title("Python Scores")
axes[1].set_xlabel("Scores")
axes[1].set_ylabel("Number of Students")

axes[2].hist(d["database"], bins=10)
axes[2].set_title("Database Scores")
axes[2].set_xlabel("Scores")
axes[2].set_ylabel("Number of Students")
plt.tight_layout()
plt.savefig("histo.png")

plt.figure(figsize=(8, 6))
plt.boxplot([d["math"], d["python"], d["database"]])
plt.xticks([1, 2, 3], ["Math", "Python", "Database"])
plt.title("Student Scores Comparison")
plt.ylabel("Scores")
plt.savefig("box.png")
plt.show()