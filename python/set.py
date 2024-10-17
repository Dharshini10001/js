first_set={"orange","Apple","Melon","Banana","Lemon"}
print(first_set)
print("Banana" in first_set)
print("Banana" not in  first_set)
first_set.add("cherry")
print(first_set)
second_set={"one","Two","Three","Four","Five"}
first_set.update(second_set)
print(first_set)
third_set=["Six","Seven","Eight","Nine","Ten"]
print(first_set)
first_set.remove("Banana")
print(first_set)
first_set.discard("Apple")
print(first_set)
x=first_set.pop()
print(x)
print(first_set)
