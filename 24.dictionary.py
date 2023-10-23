user = {
    "name" : "Vino Arystio",
    "age" : 22,
    "is_admin" : True
}

user["username"] = "vino_arystio"
user["name"] = "vino ary"

name = user["name"]
temp = user.get("username", "Kosong")
print(name)