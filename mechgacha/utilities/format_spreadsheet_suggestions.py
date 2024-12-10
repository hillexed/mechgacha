
def importLinesFromSpreadsheetToCode(lines):


    cells = lines.split("\t")
    if len(cells) < 8:
        raise ValueError("Found {len(lines)}  items in spreadsheet import! Was expecting >8")

    mechname = cells[0]
    cells = cells[1:]

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



importLinesFromSpreadsheetToCode("Shade	Chronomantic Core: A Spherical Device made of spinning 3D Gears inscribed with with runes, the materials of the gears appear to be brand new when in contact with each other, and rusting to dust when not.	Fractal Legs: Just, (Potentially) SO MANY LEGS, Insectile spikes that split into infinities to grasp even the smallest protrusions.	Hexagonal Hands: Metallic Graspers with 6 Digits on the end, positioned in a Hexagonal Pattern.	Crystalline Bathysphere: A Large Dodecahedral Cockpit/Main body made out of a clear crystal material, the pilot is visible seated inside.	Lucky Tesseracts: A Pair of Tesseracts suspended from the rear-view display by Cosmic Strings.	Jump Jet Wings: A Pair of large Robotic Wings, instead of Feathers the span is comprised of Jet Engines evenly spaced.	Harpoon Katars: A Matched pair of Punching Daggers capable of being \"Fired\" off at range and retracted or manipulated by a length of chain.	Woad Enchantments: Twisting Spiral patterns of coruscating magical runes wrap around the mech, hovering just above every surface. They appear to shift and change over time.	Spheroid Transport Form: This Mech is capable of rolling up into a Ball in order to move quicker or minimize surface area.					5-Star Hexagonal Hands: Metallic Graspers with 6 Digits on the end, positioned in a Hexagonal Pattern. Now with built in Phase Cannons in the Palms!")


