X, Y = map(str, input().split())

version_list = {
  "Ocelot": 0,
  "Serval": 1,
  "Lynx": 2,
}

if version_list[X] > version_list[Y]:
  print("Yes")
elif version_list[X] == version_list[Y]:
  print("Yes")
else:
  print("No")
