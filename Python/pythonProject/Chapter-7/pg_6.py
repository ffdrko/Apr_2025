list_1 = ["Hi", "Hello", "Welcome"]
list_2 = ["Fahim", "Faisal", "Deepto"]

for item in list_1:
    for name in list_2:
        print(item, name)
        if item == "Hello" and name == "Faisal":
            break
    print("Body of first for.")

print("Out from the body.")