
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



importLinesFromSpreadsheetToCode("cheesesnack","Biofuel Burner: Accepts most animal and vegetable oils. Smells strongly of french fries when in operation. 	Echinomotion Locomotive System: inspired by starfish and urchins, hundreds of small, pneumatic feet shuffle the mech along. You won't win any races but they're capable of handling any terrain even at extreme angles. 35% of Echinomotion mech pilots develop lifelong grudges with the mechanics who have to maintain them.	Roper Manipulators: originally designed for clearing minefields, each \\\"arm\\\" consists of four tentacles that can snake, coil, and swing independently. Experts with the system can snatch tools and weapons from quite a distance, though many are content learning how to make sick whipcrack noises.	Recycled Vans: looking like a scrapyard sculpture, some enterprising scavenger has gutted and reinforced two vans and welded them together in an intimate pose. Joints for the arms and legs have been installed where the wheels once sat. Only the mad or desperate would entrust themselves to this thing.	Foldaway Kitchenette: a metal cabinet tucked away in a corner conceals a small counter that folds out for simple meal prep with a knife rack, coffee brewer, and some space for food storage. Constructed by a pilot assigned to long and uneventful duties.	Explosive Self-Righting Device: in the event that the mech falls on it's back, an explosive charge can be used to launch the mech upright. Currently subject to several lawsuits regarding back and neck injuries.	Pick Mattock: warfare never really advanced beyond the need for earthworks and trenches. Pilots have discovered that the titanium pick on this tool pierces armor as easily as it does earth and stone.	 Tree limbs have been crudely attached to the shoulders. Enemy spotters might mistake this mech for a particularly mobile tree.	An adapter system that allows the mech to crawl on many small legs					Roper Manipulators: originally designed for clearing minefields, each \\\"arm\\\" consists of four tentacles that can snake, coil, and swing independently. Experts with the system can snatch tools and weapons from quite a distance, though many are content learning how to make sick whipcrack noises. This version comes equipped with an experimental upgrade that allows the tentacles to act completely independently of the mech. Pilots have used this ability to throw individual tentacles like bolases or to interlink tentacles together to form a single very long tentacle.")


