
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



importLinesFromSpreadsheetToCode("renne", "Earthen Splinter: A crystal brimming with earth-aspected arcane force. This energy regenerates gradually while the mech is dormant, but can be roused into uncontrollable bursts of magic if disturbed.	Tunneling Roots: This mech has great tendrils that can support its weight as would legs, but also dig deep into the ground to provide anchoring when necessary.	Plated Growth: What looks like jointed arms of stone conceals a mass of large vines beneath the exterior armor. This stone exterior can be shed for greater flexibility, but at the cost of what protection it affords.	The Tower: An imposing cylindrical column upon which rests a stately head. Simple, but iconic in the oldest sense.	Mystic Union: Tendrils within the main cavity meld themselves to the pilot's extremities and the back of their neck, making it so they see and feel everything the mech can—and can control it as they would their body. This means they feel damage to the mech as pain, and for any mind, perception is reality...	Hanging Garden: This mech has a space on its back where life flourishes. Outside of battle, it may serve as a sanctuary, or a place to grow food.	Hedge Clipper Turbo: A massive pair of scissors; the individual blades can split off into dual swords, single-edged.	Time-Ravaged: This mech is made of finely-chiseled stone covered in ancient artistic engravings, and much of it has been worn down by time and the elements. Parts of it are held together by plant growth that has overtaken it.	Beastly Deva: This mech was built to be a master of both terrain and adaptability, meaning any relation to the human form is more coincidental than anything. Controlling it may be tricky. [6 legs , 4 arms]	Spirit of the Earth: An embodiment of nature has taken residence inside this mech and communicates with the pilot. It does not speak human language, but long-term pilots claim to be able to understand it. [cockpit]	Ancillary Vines: Growing out of the mech's body, these prehensile growths may not have the greatest durability to slashing weapons, but excel at wrapping around things and tethering them. [arms]	Razor Maw: This mech's face bears a large snout with which it can bite enemies. Who needs weapons when you have the ideal predator body?	Caustic Engine: Some kind of bubbling acidic substance courses through this mech. How it doesn't eat through the thing is a small wonder. [power]	Earthen Crystal: A crystal brimming with earth-aspected arcane force. This energy regenerates gradually while the mech is dormant, but can be roused into uncontrollable bursts of magic if disturbed. This is a full earth crystal rather than just a small splinter/shard of one; its energy wellspring is far greater and can therefore be channeled into greater or longer-lasting effects, but the magic within **will** radiate into the pilot with continued operation due to its sheer concentration. This may have adverse or otherwise unusual effects on one's health, well-being, or biological taxonomy.")


