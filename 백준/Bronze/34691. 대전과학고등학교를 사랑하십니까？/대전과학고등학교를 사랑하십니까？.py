dct = {
    "animal":"Panthera tigris",
    "flower":"Forsythia koreana",
    "tree":"Pinus densiflora"
}
while True:
    s = input()
    if s == "end":
        break
    print(dct.get(s))