#Program that creats a tuple of student names and their corresponding scores
#Print out the names of students who scored above 90
students = (
    ("John", 92),
    ("Mary", 88),
    ("Alice", 95),
    ("Bob", 78),
    ("Tom", 91),
    ("Jane", 85),
    ("Mike", 93),
    ("Emily", 97),
)

print("Students who scored above 90:")
for name, score in students:
    if score > 90:
        print(name)