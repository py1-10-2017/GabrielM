sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# select a type from the above list
selected_type = mS

current_type = type(selected_type)
if current_type is int:
    if selected_type >= 100:
        print "That is a big number!"
    else:
        print "That is a tiny number!"
elif current_type is str:
    if len(selected_type) >= 50:
        print "That's a long sentence!"
    else:
        print "That is a short sentence!"
elif isinstance(selected_type, list):
    if len(selected_type) >= 10:
        print "That's a long list"
    else:
        print "That's a short list"