marks = {
    "harry" : 54,
    "hui" : 23,
    "poil" : 78
}
print(marks,type(marks))
print(marks["harry"])
print(marks.items())#it will give output in the form of tupple
print(marks.keys())
print(marks.values())
marks.update({"harry" :90,"renuka": 20})
print(marks)

print(marks.pop("hui"))
print(marks)