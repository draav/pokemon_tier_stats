import json

filename = "smogon.json"

if filename:
    with open(filename, 'r') as f:
        pokedex = json.load(f)

f = open("format_test.csv", "a")
f.write("Number,Name,Type 1,Type 2,Tier,Generation,Final Evolution\n")

for pokemon in pokedex:
    for alt in pokemon["alts"]:
        suffix = alt["suffix"]
        if not suffix == "":
            suffix = alt["suffix"] + "-"
        
        formats = alt["formats"]
        if formats is None:
            formats = ""
        
        type1 = alt["types"][0]

        
        if len(alt["types"]) == 2:
            type2 = alt["types"][1]
        else:
            type2 = ""
        
        evos = pokemon["evos"]
        if len(evos) == 0:
            final = True
        else:
            final = False

        f.write(str(pokemon["dex_number"]) + "," + suffix + pokemon["name"] + "," + type1 + "," + type2 + "," + formats + "," + pokemon["genfamily"][0] + "," + str(final) + "\n")
        print(str(pokemon["dex_number"]) + "," + suffix + pokemon["name"] + "," + type1 + "," + type2 + "," + formats + "," + pokemon["genfamily"][0] + "," + str(final))

f.close()
