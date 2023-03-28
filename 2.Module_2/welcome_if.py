'Three users are accepted, make a welcome message '
name= input("What's your name? ")
if name.lower() == "alejandro" or ('alejandro' in name.lower()):
    print("Hola Alejandro que bueno tenerte por aqui!")
elif name.lower() == "naomi" or ('naomi' in name.lower()):
    print("Hola Naomi que bueno tenerte por aqui!")
elif name.lower() == "sergio" or ('sergio' in name.lower()):
    print("Hola Sergio que bueno tenerte por aqui!")
else:
    print("Hola invitado!")
