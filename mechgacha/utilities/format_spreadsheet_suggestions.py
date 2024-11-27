
def importLinesFromSpreadsheetToCode(mechname, lines):

    

    cells = lines.split("\t")
    if len(cells) < 8:
        raise ValueError("Found {len(lines)}  items in spreadsheet import! Was expecting >8")

    namedescs = []
    for cell in cells:
        if '-' in cell or ':' in cell:

            first_splitter = 999
            if '-' in cell:
                first_splitter = min(first_splitter, cell.index("-"))
            if ':' in cell:
                first_splitter = min(first_splitter, cell.index(":"))

            title = cell[:first_splitter].strip()
            description = cell[first_splitter + 1:].strip()

            namedescs.append([title, description])
        elif cell == "":
            pass
        else:
            print(("Need a name for {cell} - add one using a 'name: description' field"))
            namedescs.append(("ERROR UNKNOWN NAME", cell.strip()))

    def q(x):
      return '"' + x + '"'

    def makeid(line):
      return f"{mechname.lower().replace(' ','')}:{line[0].lower().replace(' ','_')}"
    

    namedescs = [[q(makeid(line))] + [q(str) for str in line] for line in namedescs]

    print(
f"""
{mechname.lower()} = Mech("{mechname.lower()}", 
[
    PowerItem({",".join(namedescs[0])}),
    LegsItem({",".join(namedescs[1])}),
    ArmsItem({",".join(namedescs[2])}),
    BodyItem({",".join(namedescs[3])}),
    CockpitItem({",".join(namedescs[4])}),
    Item({",".join(namedescs[5])}, [\"back\"]),
    Item({",".join(namedescs[6])}, [\"weapon\"]),
    Item({",".join(namedescs[7])}, [\"cosmetic\"]),
""")
    for i in range(8,len(namedescs)):

        if namedescs[i][1] != "":
            print(f'    Item({",".join(namedescs[i])}{", stars=5" if i+1 == len(namedescs) else ""}),')
    print("]")
    print(")")



importLinesFromSpreadsheetToCode("P_rker","Psionic engine: this device syncs with the user's brainwaves to create a potent motive force	Heelies: these digitigrade-shaped piston legs have wheels or tracks on the bottom!	Biomechanical arms: artificial muscles made from bizzare tensile alloys	A sturdy roll cage suspends its cockpit with tense metal springs	An egg-shaped pod that encases the pilot in protective fluids	Sensor suite: a number of sensors measure various atmospheric conditions, reporting to base with a giant radio antenna	Stop Sign: slow without stopping at your own peril!	Caution stripes: black and yellow paint warns away from the mech's most sensitive - and dangerous - joints	Train Body: we strapped arms on this train and called it a mecha	Weapon: Steel Claws: These bestial claws menace with spikes of iron	Climbing equipment: the pitons and steel rope strapped to this mech let it scale sheer cliffs.	Helicoper blades: You know what helicopters are like.	Cosmetic: Fur: This mech appears to have fur growing on it.  Are they simply cosmetic synthetics, or has science finally gone far enough?	Brainwave projector: this device syncs with the user's brainwaves to create a potent motive force.  This advanced variant of the psionic engine can be mentally overclocked to create an invisible defensive shield between itself and an attacker.")


