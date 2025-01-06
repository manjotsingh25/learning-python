marks = {
    "manjot": 97,
    "simran": 100,
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"simran":99, "harry": 77})
print(marks)
print(marks.get("simran"))