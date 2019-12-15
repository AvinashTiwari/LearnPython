dict1 = {}
type(dict1)
dict1 = {"Vendor": "Cisco", "Model":"2600", "ISO": "2", "Ports":"4"}

print(dict1["Vendor"])
dict1["RAM"] = "128"
dict1["ISO"] = "3"
del dict1["Ports"]
print(dict1)
print(len(dict1))
print("ISO" in dict1)
print("ISO2" in dict1)
print("ISO2" not in dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())