users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,"Chicago")]
users_dict={name:age for name,age,city in users if age>18}
print(users_dict)