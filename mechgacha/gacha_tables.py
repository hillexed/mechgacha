from dataclasses import dataclass
from enum import Enum

from gacha_mechanics import TagType, Mech, Item, PowerItem, BodyItem, ArmsItem, LegsItem, WeaponItem, BodyPlanItem, CockpitItem




bee = Mech("bee", [
    PowerItem("bee:star_drive", "Star Drive","The heart of a solar system, keeping the mech together and providing it power."),
    LegsItem("bee:dark_matter_propulsion", "Dark Matter Propulsion","The force that keeps everything apart and the universe expanding. It also makes your mech go fast!"),
    ArmsItem("bee:gravity_wells", "Gravity Wells","The force that keeps things in obit, and also the force to grab things with your mech!"),
    BodyItem("bee:rocky_armor", "Rocky Armor","Rocks float around the core to protect it and provide structure to your mech."),
    CockpitItem("bee:orbital_cockpit","ORBital Cockpit","A transparent bubble with no gravity within it, controls floating around effortlessly where you need them to be, controlling it almost like a dance."),
    Item("bee:cloak_of_stars","Cloak of stars","A field of stars that moves and adapts as an armor where you need it to, absorbing medium impacts provided you move it to the impact site before the impact happens.", ["back"]),
    Item("bee:void_slicer","Void Slicer","A glittering blade so sharp that it feels like it can tear the fabric of space if you put enough force into it. it leaves a glittering trail.", ["weapon"]),
    Item("bee:living_satellite","Living Satellite","A small planet orbits your mech, supporting a microcosm of life.", ["cosmetic"]),
    BodyPlanItem("bee:comet_form","Comet Form","A long thin form, with one leg and 6 arm slots, trailing behind the cockpit and core like a comet trail.",{"leg": 1, "arm": 6}),
    Item("bee:satellite","Gas Satellite","A small ball of swirling gasses orbits your mech.", ["cosmetic"]),
    Item("bee:gas_satellite","Rock Satellite","A tiny comet and trail orbit your mech.", ["cosmetic"], stars=3),
    Item("bee:artificial_satellite","Artificial Satellite","A small artificial space structure (a satellite, space ship, etc) orbits your mech.", ["cosmetic"], stars=3),
    PowerItem("bee:blackhole_drive","Blackhole Drive","An infinitely deep hole in reality, the pull of the density object in the universe, contained only by the mech itself.", stars=5),
    PowerItem("bee:supernova_drive","Supernova Drive","A core of swirling energy, the captured explosion of a star, held together with the force of dark matter. Iridescent and an unstoppable force.", stars=5),
    Item("bee:gravitational_lensing", "Gravitational Lensing", "Using gravity, you can shunt power in to a strong focal beam to stab through your enemies at range.", ["weapon"], stars=4)
]
)

oneirocartographer = Mech("oneirocartographer", 
    [
    PowerItem("oneirocartographer:luminescent_core","Luminescent Core","A tarnished brass octahedron, a glow from within visible through the colored-glass apertures on its faces.", stars=2),
    LegsItem("oneirocartographer:rangers_arachnopoda","Ranger's Arachnopoda","Ceramic-plated insectoid legs, designed to climb giant trees and negotiate dense plant growth without losing stability.", stars=3),
    ArmsItem("oneirocartographer:manipulator_assembly","Manipulator Assembly","A pair of mismatched claw-grippers; one large and sturdy, the other small and meant for delicate work."),
    BodyItem("oneirocartographer:canopy_viewpoint","Canopy Viewpoint","A small, brass-and-ceramic chassis, built for visibility from the cockpit first and foremost."),
    CockpitItem("oneirocartographer:gyroscopic_suspension","Gyroscopic Suspension","This cockpit rotates within the mech's chassis, keeping the pilot upright, in order to prevent physical stress when at odd angles to the ground."),
    Item("oneirocartographer:container_lockpoint","Container Lockpoint","Grippers with which a container can be securely attached to the mech's body. Usually used to carry extra supplies on long expeditions.", ["back"]),
    Item("oneirocartographer:sling_blade","Sling Blade","For cutting a path when the canopy or the undergrowth is too thick to traverse.", ["weapon"]),
    Item("oneirocartographer:phalerae_bryophyta","Phalerae Bryophyta","Verdant moss splotches the body of this mech, almost resembling a patchwork quilt.", ["cosmetic"], stars=2),
    BodyPlanItem("oneirocartographer:arachnopod","Arachnopod","Eight legs, two \"arms\" (in more the position of chelicerae).", {"arms": 2, "legs": 8}, stars=4),
    Item("oneirocartographer:diffractive_heliograpb","Diffractive Heliograph","A reflective lattice of metal used for long-range visual signaling.", ["weapon"]),
    CockpitItem("oneirocartographer:dendritic_interface","Dendritic Interface","The cockpit has been overgrown with roots and branches, shaping themselves around the pilot's movements.", stars=3),
    ArmsItem("oneirocartographer:manipulator_assembly_tier_2","Manipulator Assembly EX","A pair of mismatched claw-grippers; one large and sturdy, the other small and meant for delicate work. Each arm unfolds into several grippers in an array of sizes and materials. A practiced pilot can use these to pick up nearly anything without damaging it.", stars=5)
]
)


hillexed = Mech("hillexed", 
[
    PowerItem("hillexed:antimatter_tea","Antimatter tea","A transparent container of hot antibeverage! A steel handle attached to glass lets you see the powerful magnets within. Drink it to unlock the vast wellspring of energy inside your mouth!"),
    LegsItem("hillexed:teeny_mechanized_legs","Teeny mechanized legs","Someone wasn't clear about millimeters versus meters. It looks like someone turned a robotic arm upside-down, full of joints and motors. That can't possibly be a baby shoe on the end, can it?", stars=2),
    ArmsItem("hillexed:neutron_star_on_a_stick","Neutron Star on a Stick","The ultimate fishing rod. Cast the line to throw the white-hot neutron star towards something you want to grab, and once gravity sticks the two together, reel it in. If you're really good, you can set up an orbit!"),
    BodyItem("hillexed:parabolic_block","Parabolic Block","A pancake-shaped glass cylinder, with attachment points along the edge. One side is curved into a mirrored parabolic depression, with three trusses holding up items to its focal point. The dish can reflect and concentrate energy into sensors, or lasers can bounce off the dish to make giant beams!"),
    CockpitItem("hillexed:crochet_controls","Crochet Controls","Two levers with a hook at the end. Grab one in each hand and wrap them around the strings of fate and warp the universe. The strings make a nice soft place to rest tired heads."),
    Item("hillexed:charge_couple_device","Charge/couple device","A sensor array of tiny purple squares arranged in a grid, able to build pictures of energy and light. Incredibly sensitive and capable of taking pictures or video, especially if boosted by a parabolic dish, but that sensitivity can be overwhelmed by strong marriages.", ["back"], stars=2),
    Item("hillexed:info_dumper","Info Dumper","It looks like someone combined a backhoe with a cellphone. A data transmitter repurposed to overwhelm foes with information.", ["weapon"], stars=2),
    Item("hillexed:glolf_patches","Glolf Patches","A decal of a square grid of emojis depicting an eagle's eye view of a game in progress. Mostly green, with some white and yellow circles, glolfers' animal signatures, and is that depicting a crack in reality?", ["cosmetic"]),
    BodyPlanItem("hillexed:starfish_mode_legs","Starfish mode: Legs","Five legs spaced around the center parabolic dish. If you balance the weight, the parabolic dish can roll on its edge to get around!", {"legs": 5}, stars=4),
    BodyPlanItem("hillexed:starfish_mode_arms","Starfish mode: Arms","Five arms spaced symmetrically around the center. If you balance the weight, you can roll on its edge to get around!", {"arms": 5}, stars=3),
    Item("hillexed:findermech","Findermech","Like a finderscope, but a mech! A smaller copy of your mech that goes on your bigger mech to help you maneuver the bigger mech."),
    Item("hillexed:telescope","Telescope","A large tube that concentrates light to unlock the universe. Attach it to a mech for long-range observations, or have the mech hold it up to your cockpit."),
    Item("hillexed:slitless_spectrograph","Slitless Spectrograph","A tangle of fiber optics that splits light and projects a rainbow of colors covered by occasional black lines into a cockpit. Those lines tell you so much information about what molecules absorbed or reflected the light you're looking at!", stars=3),
    Item("hillexed:death_bed","Death Bed","Part of your mecha is particularly soft and comfy, looking like a bed with a soft pillow. Despite the danger, the public swears it's worth climbing on your mecha to try lying on top of it. They'll die on this hill.", stars=3),
    Item("hillexed:cassegrain_style_parabolic_block","Cassegrain-Style Parabolic Block","A drum-shaped hollow tube on its side, with attachment points along the outer edge. It focuses energy like a Cassegrain telescope into a point on the back: the perfect place to put advanced sensors... or a weapon that can send energy frontwards into a giant beam of mass destruction.", stars=5),

])

styietus = Mech("St. Yietus",
[
    PowerItem("st_yietus:curseheart_engine","CURSEHEART ENGINE","A grinding mass of twisted machinery, alight with horror and hope. Within its bowels, misfortune and cruelty are catalyzed into fiercest resolve. Generates additional energy for each unique debuff affecting your mech.", stars=3),
    LegsItem("st_yietus:rotborn_stomper","ROTBORN STOMPER","A sturdy weatherproofed leg. Slow, but capable of brief bursts of agility. Gains charges over time which can be spent to perform short leaps. Leaps are faster than walking and clear low obstacles and small gaps. Slightly reduces the effects of debuffs.", stars=2),
    ArmsItem("st_yietus:rotborn_fist","ROTBORN FIST","A simple arm, covered in pitted armor and tipped with a large, gauntlet-like hand. Paired with a small remote manipulator for more delicate work. Its fist counts as a melee weapon whenever it is not equipped with a melee weapon. Slightly reduces the effects of debuffs.", stars=2),
    BodyItem("st_yietus:melancholic_visage","MELANCHOLIC VISAGE","A bulky armored torso with a masked head. Despite its battered condition it still looks ever ahead, towards a brighter future. It's tough, has good heat capacity, and reduces the effects of debuffs.", stars=2),
    CockpitItem("st_yietus:psychlink_mpi","PSYCHLINK MPI","A mysterious mask that draws closer the wills of a mech and its pilot, allowing them both to be pushed past their normal limits. Activated abilities can be used before their cooldowns end, at the cost of a large amount of heat and a longer, unskippable cooldown.", stars=3),
    Item("st_yietus:external_utility_pack","EXTERNAL UTILITY PACK","An armored backpack for storing extra-bulky equipment. Improves cooling and speeds up ability cooldowns. Slightly reduces the effects of debuffs.", ["back"], stars=2),
    Item("st_yietus:slaghewn_warpick","SLAGHEWN WARPICK","A warpick crafted from industrial waste, resplendent with signs of use and repair. Not the most elegant of weapons, but its effectiveness is undeniable. Good base stats, effective against armor.", ["weapon"], stars=1),
    Item("st_yietus:titanweave_cloak","TITANWEAVE CLOAK","A massive, well-worn cloak designed to shield a mech's mechanisms from severe weather. Comes in a variety of styles and patterns.", ["cosmetic"], stars=1),
    BodyPlanItem("st_yietus:tech_terror_body_plan","TECH TERROR BODY PLAN","An intricate, skeletal body plan that allows up to four arms or up to two weapons to be equipped instead of a body. Use at your own risk.", {"arms": 4}, stars=4),
    BodyPlanItem("st_yietus:kitbash_kit_adaptor","KITBASH KIT ADAPTER","A set of tools and materials used to combine parts in all sorts of unintended ways. Adds one additional slot of any type other than a body to your mech.", {}, stars=2), # todo: make work
    Item("st_yietus:novelty_mug","NOVELTY MUG", "A plastic novelty mug, obtained through great personal effort. The sense of pride one gets from owning this object gives you a minor all-around stat boost. Nifty!", ["cosmetic"], stars=3),
    Item("st_yietus:crescent_companion","CRESCENT COMPANION", "The moon-headed ghost of a fictional being has made its home in your mind or the systems of your mech. Can create a temporary aura around you that slows nearby enemies' cooldowns and cooling and mildly slows yours. Don't forget it or it'll fade away...", stars=4),
    Item("st_yietus:weird_lil_guy","WEIRD LIL' GUY","A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.", ["cosmetic"], stars=3),
    PowerItem("st_yietus:divinity_tap","DIVINITY TAP","A bony, eerily pristine variant of the CURSEHEART ENGINE. Generates additional energy for each unique debuff affecting you. Gain a toggled ability that greatly improves all stats but creates massive heat while active. You feel tired after using it.", stars=5),
])

triangle = Mech("triangle", 
[
    PowerItem("triangle:intrinsic","Arm: Prefix: Intrinsic","A small orb. The orb has 3 windows; within the darkness inside one can see a gently glowing triangle. No matter how you angle the orb, the triangle always faces you straight on"),
    LegsItem("triangle:leg","Arm: Prefix: Leg","Two stout legs tapering to comically small feet. The feet and part of the calves open up into a two-pronged gripper"),
    ArmsItem("triangle:arm_01","Arm: Prefix: Arm 01","Two seemingly straight-forward arms with quick-release couplers for attaching to the mech. There are pop-out handles in both the forearms and the biceps: the arms can detach/transform into weapons."),
    BodyItem("triangle:central_unit","Arm: Prefix: Central Unit","A nice, rounded, sturdy torso perched atop a small hip/waist joint unit. There is a head, although it flows almost seamlessly into the torso. Folded into/against the chest are two small pincer arms, not unlike a crab's little moutharms. The head detaches to operate as a smaller, crablike mech"),
    CockpitItem("triangle:light","Arm: Prefix: Light","Sourceless mood lighting. Is it glowing like a rainbow? Soothing warm yellows? flickering street lamp? Did you choose the current mood, or did the mech? Regardless, it always feels Perfect for The Moment"),
    Item("triangle:locker","Arm: Suffix: Locker","A large backpack. It can carry multiple accessories inside, as well as features several clamps to hold more on the outside. The entire thing can eject to act as an arms locker", ["back"]),
    Item("triangle:big","Arm: Prefix: Big","It doesn't carry anything; instead this slot is a massive hand/glove the regular arms can interface with. There is only one of these, but it can reposition its thumb to be right or left handed", ["weapon"]),
    Item("triangle:crown","Arm: Prefix: Crown","An ethereal crown of yellow light floating above the mech. Its points flicker like flames or the aurora borealis", ["cosmetic"]),
    Item("triangle:more","Arm: Prefix: More","A smaller backpack that can nest inside/under the normal backpack; this features multiple quick release joint housings to allow a multiplicity of arms"),
    ArmsItem("triangle:arm_05","Arm: Prefix: Arm 05","Two seemingly straight-forward arms with quick-release couplers. There are pop-out handles in both the forearms and the biceps: the arms can detach/transform into weapons. This pair specifically feature the ability to fire projectiles", stars=3),
    ArmsItem("triangle:arm_04","Arm: Prefix: Arm 04: Rocket Arms","Two seemingly straight-forward arms with quick-release couplers. There are pop-out handles in both the forearms and the biceps: the arms can detach/transform into weapons. This pair specifically feature the ability to launch wholesale, like rockets", stars=3),
    ArmsItem("triangle:arm_02","Arm: Prefix: Arm 02","A specialized set of arms, instead of featuring handles and transformations like most, these can split in two general grevious-style.", stars=3),
    WeaponItem("triangle:classic","Arm: Prefix: Classic","A sword. Every mech needs a sword."),
    ArmsItem("triangle:arm_03","Arm: Prefix: Arm 03","Two bulky arms with specialized couplers that can clamp anywhere onto the mech's body or onto other limbs: the arms can detach/transform into weapons. These arms have their own power supplies and can be operated independently of the body.", stars=5),
]
)

cheshire = Mech("cheshire", 

[
    PowerItem("cheshire:amber_heart","Amber Heart","This strange, semi-translucent object is crafted in the rough approximation of an animal heart. Despite being made from yellow resin and metal, it beats.", stars=3),
    LegsItem("cheshire:woven_legs","Woven legs","A single, massive piece of fabric like material obscures whatever the interior of these \"legs\" are. instead, the massive \"Skirt\" undulates and ripples slightly, putting you in mind of a sea slug"),
    ArmsItem("cheshire:the_bangles","The Bangles","A series of ring like structures float, aligning themselves with each other to form the impression of an arm in space. The hand is similar, with a hexagonal plate where the palm would be, and fingers made from several hollow tubes. It appears to be stone.", stars=2),
    BodyItem("cheshire:lithoform","Lithoform","The core of this body appears to be smooth stone, resembling polished cement. small inlays of metal have been hammered into it, or perhaps melted and poured into it. It is not spherical, but has many curves in its shape language.", stars=2),
    CockpitItem("cheshire:synaptic_pool","Synaptic Pool","One of those big old glass tubes or spheres full of goo. Most of the time pilots stand in front of it, touching the outside to make their Mech do cool things, But weirdos like to be completely submerged inside of it. You know, a classic goo chamber.", stars=2),
    Item("cheshire:glyph_thrusters","Glyph Thrusters","A series of runic circles project out from this object, framing the Mech and providing an arcane boost when needed", ["back"], stars=2),
    Item("cheshire:ceremonial_blade","Ceremonial blade","A short, wicked looking dagger. there appears to be some sort of tube from the end of it that runs back into the mech, as though hydraulics add or remove some sort of fluid from it", ["weapon"]),
    Item("cheshire:viewing_chambers","Viewing chambers","Glass that allows you to see the mechanisms inside of the machine.", ["cosmetic"]),
    CockpitItem("cheshire:stowaway_cheshire","Stowaway Cheshire","They have somehow crammed themselves into your glovebox."),  
    BodyPlanItem("cheshire:centaur","Centaur","Four legs, two arms, a power source body and a back slot.", {"legs": 4, "arms": 2}),
    BodyItem("cheshire:sigil_crusted_body","Sigil Crusted Body","What appears to be an old wooden ship or other reclaimed wood, covered in burned sigils that animate it", stars=3),
    Item("cheshire:framed_picture_of_rival","A Framed Picture of your Rival","It''s just a normal, totally platonic rival relationship. This picture is just framed to make you fight them better and not because you're repressed.", stars=2),
    Item("cheshire:a_bunch_of_floating_spheres","A bunch of floating spheres","Some of them glow!", ["cosmetic"], stars=3),
    ArmsItem("cheshire:crystal_arms","Crystal Arms","What look like standard mech arms have been absolutely shredded by some sort of magical crystal growing out of the inside. They don't seem to have impeded the arms' functions at all", stars=4),
    PowerItem("cheshire:the_wheel","Core: The Wheel","A series of gear structures that appear to be powered by some sort of forest animal running very quickly on the center one.", stars=4),
    PowerItem("cheshire:amber_heart_tier_2","Amber Heart", "This strange heart of carved amber beats in time with your own, and pumps a thick, dark ichor into your mech, powering it. The blood in your veins pulses euphorically when near it.", stars=5),
]
)

loading = Mech("loading", 
[
    PowerItem("loading:kinetic_recycler","Kinetic Recycler","A kinetic generator powered by the grounded movement of the mech", stars=2),
    LegsItem("loading:xr2","Loading's XR2","Long double jointed legs that give the mech a low crouching position while stationary, but a long stride", stars=3),
    ArmsItem("loading:knuckle_draggers","Knuckle Draggers","Long and delicate arms twice as long as the torso it is attached to", stars=2),
    BodyItem("loading:elongated_segment_frame","Elongated Segment Frame","Thin segmented spine that allows for maximum flexibility and aerodynamics", stars=3),
    CockpitItem("loading:gyrobomber","Gyrobomber","A gyroscopic cockpit with 300 degrees of visibility to allow for the stabilization of the cockpit even as the body contorts."),
    Item("loading:big_jacket","Big Jacket","A jacket that is two sizes too large. It flows in the wind, increasing evasion the more the mech moves.", ["back", "cosmetic"]),
    Item("loading:hook_lash","Hook Lash","A whip with a spinning metal weight at the end that applies a random debuff on hit", ["weapon"], stars=2),
    Item("loading:lockjaw_needler","Lockjaw Needler","A set of low damage, hig fire rate pistols that corrode any surface their projectiles make contact with", ["weapon"], stars=3),
    Item("loading:big_mechs_jacket","Big Mechs Jacket","A long flowing jacket based on the Mechs bomber jacket that flows behind the mech as it moves obscuring the body. It increases evasion and throws off targeting systems the more the mech moves.", ["back", "cosmetic"], stars=5),
]
)

metanite64 = Mech("metanite64", 

[
    PowerItem("metanite64:sound_unit", "Sound Unit","An otherworldly amalgamation of sound chips from various retro game consoles. They probably shouldn't be intersecting each other like that. Or sparking so frequently."),
    LegsItem("metanite64:pumped_up", "Pumped Up","The feet appear to be dance pads from an ancient dancing-based rhythm arcade game. The legs are boxy yet streamlined, agile enough for some dancing of its own."),
    ArmsItem("metanite64:sylish_circut", "Stylish Circuit","A copper plate resides within the left forearm, etched to resemble a keyboard. With the metallic tips of the right hand's fingers, one may close the giant circuit and produce the purest sound."),
    BodyItem("metanite64:soundbox_5_1", "SOUNDBOX 5.1","A solid cube covered in a fine mesh material. The power source hovers in the center."),
    CockpitItem("metanite64:gba_cartridge_collection", "GBA Cartridge Collection","a GBA and a number of custom cartridges. One of them is the Nanoloop 2, while the rest each play a different looping musical work."),
    Item("metanite64:roaring_wind", "Roaring Wind","Giant speakers. Bystanders may experience sudden deafness and strong winds.", ["back", "weapon"]),
    WeaponItem("metanite64:hathors_blade", "Hathor's Blade","A gift from the goddess of music, modified beyond recognition into both a keytar and a giant sword."),
    Item("metanite64:waveform", "Waveform","A neon purple visual representation of the audio that the mech is currently playing. When the mech is silent, the waveform gradually shapeshifts between one of a few basic waves (sine, sawtooth, triangle, square).", ["cosmetic"], stars=3),
    Item("metanite64:sheath_pockets", "Sheath Pockets","up to two extra weapons/tools can be stored alongside the mech's back accessory, fitting neatly into long pockets that criss-cross the mech's back.", ["back"]),
    WeaponItem("metanite64:batonatone", "Batonatone","That Otamatone looks pretty mad. Even looking at it wrong would probably get you whacked on the head."),
    WeaponItem("metanite64:don_and_ka", "Don and Ka","Two ancient ritual drumsticks, one orange and one blue. Taiko not included."),
    Item("metanite64:golden_fiddle", "Golden Fiddle","It's said that a mere boy won this fiddle after besting the Devil in a duel of music. Some say that they've heard the fiddle playing itself."),
    Item("metanite64:cobras_roar", "Cobra's Roar","5 star of the Roaring Wind. Even giant-er speakers. Either through deafness or death, the roar of the cobra is the last thing you'll get to hear.", ["back", "weapon"], stars=5),
]
)

deric = Mech("deric", 
[
    PowerItem("deric:spite_malace_or_anger","Spite, Malice, or Anger","The machine can only move when the pilot gives it their anger. It drains them of this, channeling it into the various systems."),
    LegsItem("deric:a_fract_set_of_bulky_legs","A Fract Set Of Bulky Legs","They emerge from under the core, looking more like huge slabs of metal or some other material, with thunderous stomps as they move in waves."),
    ArmsItem("deric:impossible_anti_gravity_device","Impossible Anti-Gravity Device","A blocky stump points at an object to be lifted, and it rises, with no physical contact made."),
    BodyItem("deric:a_gargantuan_slab_of_concrete_or_metal","A Gargantuan Slab of Concrete or Metal","There is some trim details and cracks, but the surface is otherwise unembelished and strangely barren."),
    CockpitItem("deric:tethered_memory","Tethered Memory","Something that you miss dearly and wish you could take out of the mech."),
    Item("deric:jagged_spine","Jagged Spine","A Horrific Spine of Jagged Spikes and Antennae", ["back"]),
    Item("deric:improvised_weaponry","Improvised Weaponry","Anything it can pickup and lift can and will be its weapons.", ["weapon"]),
    Item("deric:concrete_body","Concrete Body","The mech is made almost entirely of concrete, with small bits of metal holding some sections together.", ["cosmetic"]),
    Item("deric:living_quaters","Living Quarters","The Mecha contains a full (if small) living quarters further inside, allowing long-term deployments without support.", stars=3),
    CockpitItem("deric:tehtered_revival","Tethered Revival","Something that you miss dearly and wish you could take out of the mech. This version can be a living person or thing, like a lost pet or a loved one that passed away. They are alive, miraculously, but only inside the mech, they can never leave.", stars=5),
]
)

syl = Mech("syl", 
[
    PowerItem("syl:energy_drink", "Energy Drink","A half-empty bottle of Diet Mountain Dew is hooked up to some kind of industrial pressure cooker. Better not touch it."),
    LegsItem("syl:peg_leg", "Peg Leg","This mech waddles along on six or seven wooden table legs, that somehow haven’t broken under the weight of the mech body."),
    ArmsItem("syl:sticky_fingers", "Sticky Fingers","Instead of arms, this mech has dozens of huge novelty sticky hands, like the kind you would get at the dentist’s office if you didn’t have any cavities."),
    BodyItem("syl:classic_forklift", "Classic Forklift","Improbably, the body of this mech appears to be a totally unmodified forklift. Better hope you’re forklift certified."),
    CockpitItem("syl:fuzzy_dice", "Fuzzy Dice","Hanging from the windshield of your mech is a pair of fuzzy dice, like in an old taxi - but these are d20s, because you’re *quirky*."),
    Item("syl:vending_machine", "Vending Machine","Tied to the back of the mech, possibly as a counterweight, is a battered old vending machine. The chips and cookies inside are somehow still intact despite years of mech battling.", ["back", "cosmetic"]),
    Item("syl:plain_palms", "Plain Palms","This mech has no primary weapon, but prefers hand-to-hand combat. Specifically, it slaps people.", ["weapon"]),
    Item("syl:fallen_leaves", "Fallen Leaves","Old leaves from aspen trees are stuck to the sides and roof of this mech, as if it had just walked through a forest.", ["cosmetic"]),
    BodyPlanItem("syl:dual_cockpits", "Dual Cockpits", "In this alternate body plan, the mech has a secondary cockpit for drift control-a quad bike balanced on top of the main cockpit for a second pilot.", {"cockpit": 2}),
    Item("syl:tied_up_horse", "Tied-Up Horse","This mech has a horse tied up to one of its legs. Not sure how it stays there in combat.", ["cosmetic"]),
    Item("syl:space_pinup", "Space Pinup","On the side of this mech, painted in bright neon colors, is a pinup of a shirtless Jar Jar Binks.", ["cosmetic"], stars=3),
    CockpitItem("syl:single_tape_boombox", "Single-Tape Boombox","This mech has a retro boombox in the cockpit, and the tape that is unremovably stuck in it is “Greatest Hits Volume 1” by the Eagles."),
    Item("syl:redbox_machine", "Redbox Machine", "Tied to the back of the mech, possibly as a counterweight, is a battered old Redbox machine, but the movies it dispenses are ones no one has ever seen before. Recently, you rented Goncharov (1973) by Martin Scorsese.", ["back", "cosmetic"], stars=5),
]
)


vel = Mech("vel", 
[
    PowerItem("vel:big_reactor", "Big Reactor","A big reactor thingy (prolly nuclear adjacent) that gets refueld by hoisting big cartridges in it."),
    LegsItem("vel:sleek_legs", "Sleek Legs","Two sleek legs and high output thrusters."),
    ArmsItem("vel:manipulators", "Manipulators", "Hand-like manipulators for big stuff, prolly some small claws on cranes for small stuff."),
    BodyItem("vel:bipedal_frame", "Bipedal Frame","A human-like core (proportions may vary) with advanced sensors near the head or on it."),
    CockpitItem("vel:external_cockpit", "External Cockpit","outside cockpit? it has some periscopes/small windows as a backup."),
    Item("vel:booster_backpack", "Booster Backpack","A backpack with one or two massive boosters with added drop tanks and some light equipment to like change the fuel cell, and ammo/technical equipment/jamming equipment.", ["back"]),
    Item("vel:retractible_swords", "Retractible Swords", "A long carbine (think SVD or FRF-1), knife(ves)/retractible swords with the handle tucked in the forearms, plus countermeasures/stun launchers in the limbs.", ["weapon"]),
    Item("vel:pilot_emblem", "Pilot Emblem", "A big pilot emblem on a shoulder/skirt/side of the bust with a 2-3 colored paint scheme.", ["cosmetic"]),
    BodyItem("vel:durability_frame", "Durability Frame","For improved durability, this body has differently-colored protection plates, big fatter limbs and a rugged drilling or artillery equipment backpack. There are added hardpoints, protection and ground mobility equipment. The sensor-heavy head wears a helmet."),
    Item("vel:ace_custom_frame", "Ace Custom Frame","This mech is a special personal unit of a famous ace/freedom fighter that's fighting for the betterment of humanity, it's based from a standard military/industrial unit, but was heavily modified and customized to fit a more exploration, reconaissance, sharpshooting role.", stars=5),
]
)

amutecrypt = Mech("amutecrypt", 
[
    PowerItem("amutecrypt:new_killer_star","New Killer Star","A caged sun, kept behind some thick shielding.", stars=3),
    LegsItem("amutecrypt:the_awesome_foursome","The Awesome Foursome","4 heavy, industrial legs, designed for defence and redundancy."),
    ArmsItem("amutecrypt:i_thought_about_the_army","I Thought About The Arm-y","Two industrial robotic arms."),
    BodyItem("amutecrypt:the_part_formerly_known_as","! (The Part Formerly Known As)","A stout core with the arms mounted high up, like Atlas from Portal."),
    CockpitItem("amutecrypt:okayish_computer","Okayish Computer","An AMD CPU hanging like a pair of fluffy dice would."),
    Item("amutecrypt:thrill_the_dj","Thrill The DJ","A big set of speakers.", ["back"]),
    Item("amutecrypt:shellshot","Shellshot","A launcher capable of firing adhesive, caltrops and other traps.", ["weapon"]),
    Item("amutecrypt:thunderbirds_are_coming_out","Thunderbirds Are Coming Out","Makes the mech look like a puppet.", ["cosmetic"]),
    Item("amutecrypt:disc_changer","Disk Changer","Allows you to mount 3 power sources, but only one can be active at a time.", stars=3),
    Item("amutecrypt:parallel_player","Parallel Player","Allows you to mount 3 power sources, **and all can be active at once**.",stars=5)
]
)

intergalacticsky = Mech("intergalacticsky", 
[
    PowerItem("intergalacticsky:microfission_cell","Microfission cell","A fairly small but notoriously temperamental setup, smaller than the batteries it charges. Must be shut down in combat and environmentally hazardous situations."),
    LegsItem("intergalacticsky:needlepoint_contacts","Needlepoint contacts","Auto-balancing limbs designed to minimize environmental damage."),
    ArmsItem("intergalacticsky:augmenting_manipulators","Augmenting Manipulators","A set of nimble, thin arms with a variety of ways to grasp and manipulate objects, ranging from the size of a cat to a small tree."),
    BodyItem("intergalacticsky:gyroscopic_pod","Gyroscopic Pod","A fairly stable structure built to contain pilot, sensitive instruments, and any samples as securely as possible within a larger structure."),
    CockpitItem("intergalacticsky:stargazers_instruments","Stargazer's Instruments","A variety of measurement devices to assist in your endeavors."),
    Item("intergalacticsky:solar_fins","Solar Fins","Large, retractable solar panels used as supplementary power support.", ["back"]),
    Item("intergalacticsky:mistcutter","Mistcutter","A sample cutting tool able to use water or grit, depending on environmental availability.", ["weapon"]),
    Item("intergalacticsky:teeth","TEETH.","", ["cosmetic"],stars=3),
    BodyPlanItem("intergalacticsky:surveyors_adaptaion","Surveyor’s Adaptation","By sacrificing limb mobility (or consolidating them), the mech now can withstand over 16,000 PSI at the weakest point. (Not tested against damage from artillery, temperatures over 900C, or twisting force.)", {"legs": 1}),
    Item("intergalacticsky:the_fishbowl","The Fishbowl","A mostly spherical core built of transparent, UV-protective material. May be rendered one-way.",["body"]),
    Item("intergalacticsky:paddleboards","Paddleboards","Flexible fins originally made for movement in shallow waters. Can also be used for land maneuvers, to some effect.",["legs"]),
    Item("intergalacticsky:noodlers","Noodlers","Limbs made specifically for catching large, predatory fish.",["arms"]),
    Item("intergalacticsky:bare_joints","Bare Joints","Through the power of easily-replaced and cleaned parts, the joints on limbs are now bare!",["cosmetic"]),
    Item("intergalacticsky:frogflare","Fogflare","A heavily modified and overclocked cutting tool able to use water or grit, depending on environmental availability. Dubiously legal.",["weapon"], stars=5),
]
)


alto = Mech("alto", 
[
    LegsItem("alto:unremarkable_legs","Unremarkable Legs","Hydraulic mecha legs, ready for painting, aftermarket tinkering, or full replacement. "),
    ArmsItem("alto:unremarkable_arms","Unremarkable Arms","Hydraulic mecha arms, ready for painting, aftermarket tinkering, or full replacement."),
    BodyItem("alto:unremarkable_body","Unremarkable Body","Hydraulic mecha body, ready for painting, aftermarket tinkering, or full replacement. "),
    BodyPlanItem("alto:light_mecha","Light Mecha","Plans for an ultralight mobile suit consisting of only a powersource, a weapon, and a back mounted accessory. Perhaps closer to power armor than a proper mecha. Given to Alto by the original Polkadot.", {"weapon": 1, "power":1, "back":1}, stars=5),
]
)

renne = Mech("renne", 
[
    PowerItem("renne:earthen_splinter","Earthen Splinter","A crystal brimming with earth-aspected arcane force. This energy regenerates gradually while the mech is dormant, but can be roused into uncontrollable bursts of magic if disturbed.", stars=2),
    LegsItem("renne:tunneling_roots","Tunneling Roots","This mech has great tendrils that can support its weight as would legs, but also dig deep into the ground to provide anchoring when necessary."),
    ArmsItem("renne:plated_growth","Plated Growth","What looks like jointed arms of stone conceals a mass of large vines beneath the exterior armor. This stone exterior can be shed for greater flexibility, but at the cost of what protection it affords."),
    BodyItem("renne:the_tower","The Tower","An imposing cylindrical column upon which rests a stately head. Simple, but iconic in the oldest sense."),
    CockpitItem("renne:mystic_union","Mystic Union","Tendrils within the main cavity meld themselves to the pilot's extremities and the back of their neck, making it so they see and feel everything the mech can—and can control it as they would their body. This means they feel damage to the mech as pain, and for any mind, perception is reality..."),
    Item("renne:hanging_garden","Hanging Garden","This mech has a space on its back where life flourishes. Outside of battle, it may serve as a sanctuary, or a place to grow food.", ["back"], stars=3),
    Item("renne:hedge_clipper_turbo","Hedge Clipper Turbo","A massive pair of scissors; the individual blades can split off into dual swords, single-edged.", ["weapon"]),
    Item("renne:time_ravaged","Time-Ravaged","This mech is made of finely-chiseled stone covered in ancient artistic engravings, and much of it has been worn down by time and the elements. Parts of it are held together by plant growth that has overtaken it.", ["cosmetic"], stars=3),
    BodyPlanItem("renne:beastly_deva","Beastly Deva","This mech was built to be a master of both terrain and adaptability, meaning any relation to the human form is more coincidental than anything. Controlling it may be tricky.", {"legs":6,"arms":4}),
    CockpitItem("renne:spirit_of_the_earth","Spirit of the Earth","An embodiment of nature has taken residence inside this mech and communicates with the pilot. It does not speak human language, but long-term pilots claim to be able to understand it."),
    ArmsItem("renne:ancillary_vines","Ancillary Vines","Growing out of the mech's body, these prehensile growths may not have the greatest durability to slashing weapons, but excel at wrapping around things and tethering them."),
    Item("renne:razor_maw","Razor Maw","This mech's face bears a large snout with which it can bite enemies. Who needs weapons when you have the ideal predator body?", ["cosmetic"]),
    PowerItem("renne:caustic_engine","Caustic Engine","Some kind of bubbling acidic substance courses through this mech. How it doesn't eat through the thing is a small wonder."),
    PowerItem("renne:earthen_crystal","Earthen Crystal","A huge crystal brimming with earth-aspected arcane force. Its size carries tremendous magic, making great or long-lasting effects possible, but its sheer concentration means magic **will** radiate into the pilot with continued operation, affecting one's health, well-being, or biological taxonomy.", stars=5),
]
)

moonbug = Mech("moonbug", 
[
    PowerItem("moonbug:glitch_engine","Glitch Engine","Two manipulator arms that move a teapot and a rubber duck in precise ways to make energy by abusing bugs in the universe, now 98% reality tear free!"),
    LegsItem("moonbug:emergency_grippers","Emergency Grippers","This mech is able to deploy toes in order to distract the enemy, be careful however as if you stub the Mech's toe it will psychically send the pain to you.",stars=2),
    ArmsItem("moonbug:insectoid_arm_array","Insectoid Arm Array","A set of 4 arms, each with 4 digits and claws, to save on energy and heat production. The arms aren't as strong as other sets, but has immense potential.", stars=2),
    BodyItem("moonbug:covert_chassis","Covert Chassis","A sneaky and [REDACTED] Core made by the teamwork of a Mech and a [DATA EXPUNGED] from the Houston Spies. While the blueprints are open source they're encoded with at least [TOP SECRET] Ciphers. Despite this. many Mechs swear by the design saying it's pretty [REDACTED] good."),
    CockpitItem("moonbug:blankets","Blankets","Piles of soft, plush blankets lay around in the cockpit. When your mech overheats some of the heat will be redirected to the cockpit and it feels amazing."),
    Item("moonbug:phase_shifter","Phase Shifter","A back mounted piece of obtuse and cobbled together wires and breadboards. It allows the mech to temporarily enter the immaterial for a few seconds. It is highly advised to keep immaterial exposure to less than an hour a year to prevent conceptual delamination.", ["back"], stars=3),
    Item("moonbug:a.e.i.o.u","A.E.I.O.U","The Amazingly Explosive Igniter Of Unfire. Shoots lobs of un-napalm at enemies. Un-napalm is one of the few substances Unfire actually burns.", ["weapon"], stars=3),
    Item("moonbug:antennae","Antennae","Two feathery antennae are installed on the head of your mech. They won't be getting any signals, but they look adorable.", ["cosmetic"]),
    WeaponItem("moonbug:delta_theta_wave_generator","Delta-Theta Wave Generator","A piece of repurposed lab equipment, it is able to create the illusive Delta-Theta waves, which has mutagenic properties for some \"people\" (It's a speaker that turns you into an animal.)", stars=4),
    LegsItem("moonbug:legs_design_173","Design Type. 173","A pair of mech legs that seem to be crudely made of plaster and spray paint. Despite that, these legs are immensely flexible and mobile... if no one is looking at you."),
    Item("moonbug:finarian_phase_diver","Finarian Phase Diver","A back mounted piece of equipment upgraded and repaired across generations. It allows a mech to dive into the immateria. Dozens of stamped seals in Finarian tongue act as a blueprint and a ward to prevent unreality from leaking into the mech, letting it stride the depths for as long as it has power.", ["back"], stars=5),
]
)

cheesesnack = Mech("cheesesnack", 
[
    PowerItem("cheesesnack:biofuel_burner","Biofuel Burner","Accepts most animal and vegetable oils. Smells strongly of french fries when in operation."),
    LegsItem("cheesesnack:echinomotion_locomotive_system","Echinomotion Locomotive System","Inspired by starfish and urchins, hundreds of small, pneumatic feet shuffle the mech along. You won't win any races but they're capable of handling any terrain even at extreme angles. 35% of Echinomotion mech pilots develop lifelong grudges with the mechanics who have to maintain them.", stars=3),
    ArmsItem("cheesesnack:roper_manipulators","Roper Manipulators","Originally designed for clearing minefields, each \"arm\" consists of four tentacles that can snake, coil, and swing independently. Experts with the system can snatch tools and weapons from quite a distance, though many are content learning how to make sick whipcrack noises."),
    BodyItem("cheesesnack:recycled_vans","Recycled Vans","Some enterprising scavenger has gutted and reinforced two vans and welded them together in an intimate pose, looking like a scrapyard sculpture. Joints for the arms and legs have been installed where the wheels once sat. Only the mad or desperate would entrust themselves to this thing.", stars=3),
    CockpitItem("cheesesnack:foldaway_kitchenette","Foldaway Kitchenette","A metal cabinet tucked away in a corner conceals a small counter that folds out for simple meal prep with a knife rack, coffee brewer, and some space for food storage. Constructed by a pilot assigned to long and uneventful duties."),
    Item("cheesesnack:self_righting_device","Explosive Self-Righting Device","In the event that the mech falls on it's back, an explosive charge can be used to launch the mech upright. Currently subject to several lawsuits regarding back and neck injuries.", ["back"], stars=3),
    Item("cheesesnack:pick_mattock","Pick Mattock","Warfare never really advanced beyond the need for earthworks and trenches. Pilots have discovered that the titanium pick on this tool pierces armor as easily as it does earth and stone.", ["weapon"], stars=3),
    Item("cheesesnack:branch_camoflage","Branch Camoflage","Tree limbs have been crudely attached to the shoulders. Enemy spotters might mistake this mech for a particularly mobile tree.", ["cosmetic"]),
    BodyPlanItem("cheesesnack:centipede_mode","Centipede Mode","An adapter system that allows the mech to crawl on many small legs", {"legs": 4}),
    ArmsItem("cheesesnack:five_star_roper_manipulators","Roper Manipulators","Originally for clearing minefields, each \"arm\" consists of four moveable tentacles. An experimental upgrade allows them to act completely independently of the mech; pilots can snatch weapons from afar, throw individual tentacles like boluses, or interlink tentacles together into one long tentacle.", stars=5),
]
)

warlock = Mech("warlock", 
[
    PowerItem("warlock:system_of_hamster_wheels","System of Hamster Wheels","They are intricately connected by a mechanism to a generator. The hamsters have a great union contract."),
    LegsItem("warlock:digitigrade_legs","Digitigrade Legs","Strong, animal-like legs with big paws and claws that can dig into the ground for support"),
    ArmsItem("warlock:sable_arms","Sable Arms","Extendible animal-like arms with big paws and claws for grabbing."),
    BodyItem("warlock:forest_sable","Forest Sable","Camouflaged to blend in with dirt and forests, the slender body of this mech is perfect for hiding in plain sight."),
    CockpitItem("warlock:library_membership_card","Library Membership Card","With this, you can download ebooks, audiobooks, music, and games! Plus, you can check out physical materials at your local library.", stars=2),
    Item("warlock:big_backpack","Big Backpack","this comedically large backpack is actually great for storing things. It’s water-resistant, but not waterproof.", ["back"], stars=3),
    Item("warlock:big_hammer","Big Hammer","Giant two-handed war-hammer. Fun to spin around with!", ["weapon"]),
    Item("warlock:pride_&_pronoun_pins","Pride & Pronoun Pins","Colorful, easily legible, allows you to share your identity with the world", ["cosmetic"], stars=2),
    BodyPlanItem("warlock:combat_animal","Combat animal","Four legs, 2 weapon slots on back.", {"legs": 4, "weapon": 2}),
    Item("warlock:giant_beaglepuss","Giant Beaglepuss","Also known as Groucho Marx glasses, they are lensless and have a comedic fake nose and mustache attached.", ["cosmetic"], stars=3),
    BodyItem("warlock:massive_speaker_system","Massive Speaker System","With this, you can blast music, or unleash a bestial roar that can be heard for miles. body", stars=3),
    BodyItem("warlock:winter_marten","Winter Marten","Camouflaged to blend in with ice and snow, the slender body of this mech is perfect for hiding in cold environments.", stars=3),
    PowerItem("warlock:the_soup_engine","The Soup Engine","Just pour some soup in there, or a smoothie, and it’ll run real good!", stars=4),
    LegsItem("warlock:advanced_digitigrade_legs","Advanced Digitigrade Legs","Strong, animal-like legs with big paws and claws that can dig into the ground for support. These legs can be super-charged, crackling with blue electricity to give you incredible speed boosts, letting you run faster than should be reasonably possible, even up walls!", stars=5),
]
)

bytes = Mech("bytes", 
[
    PowerItem("bytes:dying_star","Dying Star","The radioactivity of this source makes it very effective yet very unstable."),
    LegsItem("bytes:hover_jets","Hover Jets","These jets allow universal transit over a variety of terrains by never making contact with the ground.", stars=2),
    ArmsItem("bytes:magnetized_grabbers","Magnetized Grabbers","These claws are extremely effective and lifting and holding magnetic materials."),
    BodyItem("bytes:steel_casket","Steel Casket","This durable chassis has boxy edges and thick armor."),
    CockpitItem("bytes:climate_controller","Climate Controller","This high-tech cockpit accessory provides great comfort to the pilot regardless of the condition."),
    Item("bytes:long_range_warp_boosters","Long Range Warp Boosters","These boosters allow for rapid yet poorly controlled mobility over distance.", ["back"], stars=4),
    Item("bytes:harvest_claw","Harvest Claw","This massive melee weapon is comprised of several blades and is capable of inflicting devastating damage.", ["weapon"]),
    Item("bytes:split_paintjob","Split Paintjob","This chaotic paintjob has no left-right symmetry.", ["cosmetic"], stars=2),

    BodyPlanItem("bytes:cruiser_form","Cruiser Form","This vehicular form is well adapted for high speeds and endurance.", {"legs": 0}),
    Item("bytes:short_range_teleporters","Short Range Teleporters","These devices make use of anomalous technology to teleport short distances to evade attacks.", stars=3), # don't know what type this should be. mobility?
    BodyItem("bytes:aerogel_heat_shell","Aerogel Heat Shell","This lightweight material provides immense resistance to all but the most stellar of heat sources."), # or this
    WeaponItem("bytes:uncertainty_mines","Uncertainty Mines","These mines latch onto mechas sabotaging their control and stability."),
    Item("bytes:antimass_stabilizer","Antimass Stabilizer","This component allows the effects of gravity to be ignored for short period of time.", ["back"], stars=4),
    WeaponItem("bytes:hard_light_harvest_claw","Hard Light Harvest Claw","This massive melee weapon has blades made of hard light capable of shredding any armor.", stars=5),
]
)

thecowofeternalflame = Mech("thecowofeternalflame", 
[
    PowerItem("thecowofeternalflame:fusion_core","Fusion core","High energy production at the expense of high heat output and a tendency to destabilize if shot directly."),
    LegsItem("thecowofeternalflame:spider_legs","Spider Legs", "Four spider-like legs that can be used to climb vertical surfaces"),
    BodyItem("thecowofeternalflame:drone_body","Integrated Drone Port","A bulky body with a drone bay that opens in the middle of it."),
    CockpitItem("thecowofeternalflame:drone_controls","Drone Controls","A drone control panel and keychain thingy hanging from the ceiling of the types of drones the mech produces", stars=2),
    Item("thecowofeternalflame:back_mounted_radio","Back-Mounted Radio", "Large radio pack with long antennae coming up from it, for sending and receiving signals from the drones as well as for long-range communication with teammates", ["back"]),
    Item("thecowofeternalflame:targeting_system","Long-range laser targeting system", "Helps to guide missiles to hit targets, whether from salvos, drones or allies.", ["weapon"], stars=2),
    Item("thecowofeternalflame:lightning_decal","Lightning Decal","A lightning decal, thematically appropriate to put on a targeting system.", ["cosmetic"]),
    BodyItem("thecowofeternalflame:swivel_pivot","Swivel Pivot","The mech's torso sits on a 360° swivel mount with a leg situated at each quarter of the base", stars=2),
    WeaponItem("thecowofeternalflame:drone-factory","Drone Factory", "The mech has a drone bay situated in it. Within the bay is an automated drone factory wherein the mech can slowly produce new drones. This slows the mech down a lot due to the sheer bulk. There is room to hold eight drones in the drone bay at any one time.", stars=4),
    WeaponItem("thecowofeternalflame:error_unknown_name","Long-Range Railgun","This railgun has a huge range, but is slow firing with a long reload.", stars=2),
    Item("thecowofeternalflame:light_armor","Light Armor", "This armor weighs lighter than most to compensate for heavy weapons. It increases speed at the cost of making it vulnerable to smaller, faster flanking mechs", stars=2), # defense?
    WeaponItem("thecowofeternalflame:drone_medium","Medium Gunner Drone","A medium-range flying gunner-drone equipped with a HMG;", stars=3),
    WeaponItem("thecowofeternalflame:drone_long","Long Artillery Drone","A long-range artillery drone that can fire missile salvos. It moves via tank treads.", stars=3),
    WeaponItem("thecowofeternalflame:drone_fast","Fast Spider Drone","A fast moving drone that is effectively an oversized spider mine from SC2", stars=3),
    Item("thecowofeternalflame:drone_radar","Radar Scout Drone","A fast moving flying scout drone equipped with radar tech.", stars=3),
    Item("thecowofeternalflame:five_star_back_radio","Multiplexed Communications Radio","Large radio pack with long antennae coming up from it, for sending and receiving signals from the drones as well as for long-range communication with teammates. This version allows all allies to loop in to eachother's camera feeds in real-time, as well as any drone feeds on the field.", ["back"], stars=5),
]
)

shork = Mech("shork", 
[
    PowerItem("shork:lithium_polymer_battery","Lithium Polymer Battery","Harnesses the incredible power of magic smoke. Don't let it escape!"),
    LegsItem("shork:mecanum_drive","Mecanum Drive","Wheels with built-in rollers, designed for omnidirectional movement.", stars=4),
    ArmsItem("shork:srimech_arm","Srimech Arm","'Ave you got a srimech? Course you 'ave!"),
    BodyItem("shork:billet_chassis","Billet Chassis","A solid block of aluminium carved into a chassis shape. Indestructible, but tough to repair."),
    CockpitItem("shork:remote_control_unit","Remote Control Unit","Battle at a safe distance from the carnage."),
    Item("shork:apd_unit","APD Unit","An array of scaffolding designed to keep dangerous foes out of reach. Also handy if you get stuck in a hole.", ["back"], stars=2),
    WeaponItem("shork:spinnaaaaaaaaah","SPINNAAAAAAAAAH","A big hunk of metal spinning at ungodly speeds. Kinetic energy in its purest form.", stars=3),
    Item("shork:polkadot_fur","Polkadot Fur","Offers no tactical advantage whatsoever.", ["cosmetic"], stars=2),
    BodyPlanItem("shork:snowplow","Snowplow","Low to the ground, with a solid defensive profile. Armaments are tucked behind the safety of a giant wedge.", {"legs": 4, "arms": 0}),
    WeaponItem("shork:d2_kitbot_drone","D2 Kitbot Drone","An incredibly effective drone unit, but is it really your victory if you didn't built it yourself...?", stars=4),
    WeaponItem("shork:pulveriser","Pulveriser","A gigantic articulated metal mallet. Surprisingly ineffective."),
    WeaponItem("shork:massive_claw_unit","Massive Claw Unit","Nine gigatons of crushability factor!", stars=3),
    WeaponItem("shork:flippaaaaaaaaah","FLIPPAAAAAAAAAH","A pneumatic paddle designed for pushing potential pugilists before they pounce.", stars=2),
    WeaponItem("shork:lithium_polymer_armament","Lithium Polymer Armament","Harnesses the incredible power of magic smoke. Don't let it escape! This unusual config directly weaponizes the battery unit. If this gets hit, the fight's ending one way or another.", stars=5),
    LegsItem("shork:c5_drive","C5 Drive","A wheeled drive system, powered by a set of motors scavenged from an ahead-of-its-time electric bike."),
    LegsItem("shork:magmotor_drive","Magmotor Drive","A wheeled drive system, powered by a state-of-the-art set of drive motors. High torque, high maneuverability.", stars=3),
    ArmsItem("shork:wowot_arms","Wowot Arms","A highwy awticuwated, cwane-wike set of awms, ending in gwabbing jaws. Pewfect fow gwappwing uwu", stars=2),
    BodyItem("shork:scrapyard_special","The Scrapyard Special","A chassis fully constructed from a few hundred bob worth of scrapmetal. The front is encased in old traffic signs. ROAD AHEAD CLOSED, it says.", stars=2),
    BodyPlanItem("shork:ring","Ring","A defensive, invertible design, with weapons mounted on a ring orbiting around your chassis. The best defense is a perfect offense.", {"legs": 4, "arms": 2}, stars=4),
    WeaponItem("shork:thwacker","Thwacker","A weighty cudgel on a flexible arm, bolted onto an extremity. Powered by your drivetrain, thrash about to strike anyone that comes close."),
    WeaponItem("shork:roborat_drones","Robo-Rat Drones","Deploy a swarm of robotic rats, armed with saws and flamethrowers. Effective at cutting through armour and torching insides, but can be disarmed by toppling them on their backs.", stars=3),
    Item("shork:full_body_spinner","Full Body Spinner","A giant blade of metal orbiting your mech at ungodly speeds, fuelled by the biggest ICE we could strap on its back. Kinetic energy in its purest form.",["back"], stars=5),
]
)

p_rker = Mech("p_rker", 
[
    PowerItem("p_rker:psionic_engine","Psionic engine","This device syncs with the user's brainwaves to create a potent motive force.", stars=3),
    LegsItem("p_rker:heelies","Heelies","These digitigrade pistons have wheels on the bottom to enhance mobility and coolness.", stars=2),
    ArmsItem("p_rker:biomechanical_arms","Biomechanical arms","Artificial muscles made from bizzare tensile alloys.", stars=2),
    BodyItem("p_rker:crash_resistant_body","Crash-Resistant Body","A sturdy roll cage suspends its cockpit with tense metal springs."),
    CockpitItem("p_rker:egg_pod","Egg-shaped Pod","An egg-shaped pod that encases the pilot in protective fluids.", stars=2),
    Item("p_rker:sensor_suite","Sensor suite","A number of sensors measure various atmospheric conditions, reporting to base with a giant radio antenna", ["back"]),
    WeaponItem("p_rker:stop_sign","Stop Sign","Slow without stopping at your own peril!"),
    Item("p_rker:caution_stripes","Caution stripes","Black and yellow paint warns away from the mech's most sensitive - and dangerous - joints", ["cosmetic"]),
    BodyPlanItem("p_rker:train_body","Train Body","We strapped arms on this train and called it a mecha!", {"legs":0,"arms":3}, stars=3),
    WeaponItem("p_rker:weapon","Steel Claws","These bestial claws menace with spikes of iron."),
    Item("p_rker:climbing_equipment","Climbing equipment","The pitons and steel rope strapped to this mech let it scale sheer cliffs."), # legs? mobility
    Item("p_rker:helicoper_blades","Helicoper blades","You know what helicopters are like."), # mobility (or a weapon if you get silly with it)
    Item("p_rker:cosmetic","Fur","This mech appears to have fur growing on it.  Are they simply cosmetic synthetics, or has science finally gone far enough?", ["cosmetic"], stars=4),
    PowerItem("p_rker:brainwave_projector","Brainwave projector","This device syncs with the user's brainwaves to create a potent motive force. The advanced psychonormative projectors allow this force to be externalized, offensively and defensively, but overriding the built-in limiters can be highly dangerous.", stars=5),
]
)

only = Mech("only", 
[
    PowerItem("only:kinetic_protodrive","Kinetic Protodrive","This experimental power system generates energy when exposed to acceleration and deceleration.", stars=2),
    LegsItem("only:riproller_legs","Riproller Legs","Bipedal legs with wheels in the feet and knees, allowing the equipped mech to enter a high maneuver mode by kneeling.", stars=1),
    ArmsItem("only:jet_booster_arms","Jet Booster Arms","For when you need to hit them before they hit you.", stars=2),
    BodyItem("only:knockout_frame","Knockout Frame","A humanoid Core with thruster arrays to allow for last second evades. Duck, Dive, Dodge!", stars=1),
    CockpitItem("only:remote_access","REMOTE ACCESS","Yeah, you aren't actually in your mech. This remote control cuts down on weight, AND lets you take riskier moves.", stars=2),
    Item("only:flame_wheel","Flame Wheel","A large ring of fire blazes above your mech's back.",  ["back"], stars=4),
    WeaponItem("only:concussive_knuckles","Concussive Knuckles","Massive blocky fists that generate additional concussive force on contact, letting you amp up your impact", stars=1),
    Item("only:energy_vein_system","Energy Vein system","A network of glowing lines cover your mech, showing how power flows through its system and flaring up when energy levels spike", ["cosmetic"], stars=1),
    BodyPlanItem("only:asura","Asura","A blueprint from Only with a fearsome design - 2 Legs, 6 arms", {"legs":2,"arms":6}, stars=3),
    BodyPlanItem("only:arbitor","Arbitor","A blueprint from Only with a powerful design - 2 legs and 4 arms that hover separate from the body",{"legs":2,"arms":4}, stars=4),
    Item("only:mirage_system","Mirage System","Allows the equipped mech to become intangible for a short period. Getting hit? Just dont get hit lol", ["back"], stars=3),
    Item("only:wingblades","Wingblades","These angular constructs hover just above your mech's back, able to both generate lift for your mech and swing around for offensive maneuvers", ["back"], stars=4),
    Item("only:sick_ass_jacket","Sick Ass Jacket","Your mech is covered by an incredibly cool jacket, the fabric of which reduces the damage of energy weaponry", ["cosmetic"], stars=1),
    BodyItem("only:knockout_frame_plus","Knockout frame Plus","Humanoid Core with Thruster arrays to allow for last second evades. Now with Grav-Brake technology to instantly cancel momentum. Duck, JUKE, Dive and Dodge!", stars=5),
]
)

ditto = Mech("ditto", 
[
    PowerItem("ditto:demon_core","Demon Core","Yeah it's not a good idea to stand anywhere near the core while the machine is running. We have a way to turn it off without you getting close to it, don't worry.", stars=1),
    LegsItem("ditto:ball","Ball","The mech's core balances on top of a ball. I have a diagram but I don't know how to fit it into this description.", stars=3),
    ArmsItem("ditto:giant_gravity_gun_from_half_life_2","Giant Gravity Gun from Half Life 2","Its name is what it is.", stars=2),
    BodyItem("ditto:default_blender_cube","Default Blender Cube","It looks like a gray default blender cube with a cockpit attached.", stars=1),
    CockpitItem("ditto:air_freshener","Air freshener","This does nothing to be fair.", stars=1),
    Item("ditto:giant_wind","Giant wind-up key","Playing with toys.", ["back", "cosmetic"], stars=2),
    Item("ditto:comically_large_spoon","Comically Large Spoon","Perfect for ice cream!", ["weapon"], stars=3),
    Item("ditto:cool_hat","Cool hat","It's a really cool hat", ["cosmetic"], stars=4),
    LegsItem("ditto:hover_core","Hover core","Who needs Legs?"),
    BodyPlanItem("ditto:ex_blueprint","EX Blueprint","Who needs arms with legs like these? No, seriously, your mech doesn't need arms. If you need to hold things? ROBOT TELEKINESIS.", {"legs":1,"arms":0}, stars=2),
    LegsItem("ditto:ex_legs","EX Legs","Legs used by a certain famous robot, but scaled up for use in mechs.", stars=3),
    PowerItem("ditto:keygen","Keygen","Listen I know it has Gen in the name but maybe it isn't such a good idea to use as a power source????", stars=3),
    WeaponItem("ditto:hammer_of_dawn","Hammer of Dawn","This is an orbital laser, not a hammer. Who named this????", stars=4),
    BodyItem("ditto:advanced_blender_cube","ADVANCED Blender cube","It looks like a gray default blender cube with a cockpit attached. But it's ADVANCED!", stars=5),
]
)

hal2000 = Mech("hal 2000", 
[
    PowerItem("hal2000:the_beating_hearts_of_one","The Beating Hearts of One","Thousand Worms: The heartbeats of these still-live worms are amplified and converted into electrical energy for the mech to use."),
    LegsItem("hal2000:dimensionally","Dimensionally","Disjointed Walkers: They would look like normal mechanical legs if you could see them in their entirety, it's just that each joint is in a different dimension, whoops!"),
    ArmsItem("hal2000:cobbled_scrap_arms","Cobbled Scrap Arms","Well, they don't move (unless you're an Ork and believe hard enough), and leave you at decent risk of tetanus, but at least they look cool!"),
    BodyItem("hal2000:orb","ORB","SPHERE"),
    CockpitItem("hal2000:divesystem","Full-Body Dive System","Really FEEL like you're dying to that rocket."),
    Item("hal2000:backlift","Backlift","A pair of forks on the back for lifting cargo, only usable if you're Forklift Certified!", ["back"]),
    Item("hal2000:guminator_3000","Guminator 3000","Immediately gums up every joint on the opposing mech if it successfully hits them, a mechanic's worst nightmare.", ["weapon"]),
    Item("hal2000:clown_face","Clown Face","Paint: +1000 Clown Vibes, +200 Fear Induced", ["cosmetic"]),
    BodyPlanItem("hal2000:crawler","Crawler","8 arms. No legs.", {"arms":8, "legs":0}),
    BodyItem("hal2000:orbascended","ORB","SPHERE, ASCENDED FORM, ALL-KNOWING, ALL-SEEING, CLEAR AND PERFECT, NONE CAN ESCAPE ITS SIGHT", stars=5),
]
)

turtlelover2244 = Mech("turtlelover2244", 
[
    PowerItem("turtlelover2244:hype_core","Hype Core","A Generator connected to an online video stream. The more hyped the audience, the more power the core generates."),
    LegsItem("turtlelover2244:hover_boots","Hover Boots","A set of overly fancy legs equipped with hover technology, letting the mech deftly float a few inches off the floor."),
    ArmsItem("turtlelover2244:puppet_hands","Puppet Hands","Hands that freely float around your mech. Excellent for offense, not so much for defense."),
    BodyItem("turtlelover2244:subspace_generator","Subspace Generator","A Small and Sleek Body that uses pocket dimensions to store equipment when not in use."),
    CockpitItem("turtlelover2244:streaming_setup","Streaming Setup","A Mic, Camera, and Several monitors showing your streams statistics and chat, along with mildly useful mech information."),
    Item("turtlelover2244:holocape","Holo-Cape","A Large and permanently flowing cape made of Hard-light. Most conventional weapons cannot pierce it.", ["back"]),
    WeaponItem("turtlelover2244:arcane_staff","Arcane Staff","A Polearm covered in glowing Runes, Although it holds no substantial magic power. The tip can fire a laser beam, if that’s any compensation."),
    Item("turtlelover2244:gamer_leds","Gamer LEDs","Anything is improved by adding rainbow lights to it.", ["cosmetic"]),
    BodyPlanItem("turtlelover2244:magician","Magician","4 Arms, 2 Legs, 2 Power Sources. A Blueprint Designed to use many weapons at once, Two Power cells are needed to run at full capacity.", {"arms":4,"legs":2,"power":2}),
    Item("turtlelover2244:tophat","Top Hat","A mundane, but fancy hat.", ["cosmetic"]),
    WeaponItem("turtlelover2244:shuffler","The Shuffler","A gun that launches steel sided player cards at a rapid pace."),
    Item("turtlelover2244:interstitial_engine","Interstitial Engine","A mysterious device that can pierce through gaps in reality, letting you teleport a short distance.", ["back"]),
    Item("turtlelover2244:roboduplicate","Robo-Duplicate","A robotic duplicate of yourself riding on the top of your mech.", ["cosmetic"]),
    WeaponItem("turtlelover2244:true_arcane_staff","True Arcane Staff","A Polearm covered in glowing Runes and holds substantial magic power. It is able to fling immense amounts of magical energy with ease.", stars=5),
]
)


zweihawke = Mech("zweihawke", 
[
    PowerItem("zweihawke:refined_necrolite_core","Refined Necrolite Core","This refined and processed mineral cluster teems with the essence of souls. It's violet luster belies the sinister nature of it's conception, and the horrible process used to make it."),
    LegsItem("zweihawke:gyratory_spheres","Gyratory Spheres","A single, mobile sphere affixed to a cage above. Using Gyroscopy and propulsion, it balances upon the sphere and rolls across a surface akin to a ballpoint pen upon paper."),
    ArmsItem("zweihawke:entanglement_engine","Fixed-Point Entanglement Engine","Not \"arms\" in the traditional sense, but can lift items by entangling them to a point directly in front of the engine. Despite a visible gap of air between the object and the mech, the mech retains the weight of the object and if said object is yanked out with enough force, the core will go with it."),
    BodyItem("zweihawke:ornate_marble_frame","Ornate Marble Frame","This decorative frame is coated in what would seem to be brittle materials, hiding it's heavy less sightly interiors. Often used in shows and ceremonial contexts, this mech frame is not suited for dangerous situations if you want to keep it's luster."),
    CockpitItem("zweihawke:exposed_clockwork","Exposed Clockwork","While dangerous at the outset, a talented engineer could immediately identify issues in the mech's systems. Reaching inside is not advised."),
    Item("zweihawke:necrolite_tether","Necrolite Tether","Bound to the harvest of long fractured and dead souls, this contact point drains life. A desperate pilot need only stick their hand in for a few more hours of battery...", ["back"]),
    Item("zweihawke:quantum_box","Quantum Box","Much like what you're doing right now, whatever's inside exists in a quantum state of superposition until it is opened and observed. I hope it's circus peanuts.", ["weapon"]),
    Item("zweihawke:electroplated_gold","Electroplated Gold","Some say divinity is only for the rich. Those people are fools.", ["cosmetic"]),

    BodyPlanItem("zweihawke:modeswapper","Mode-Swapper","Has only one set of legs active at a time and can swap between them at will.", {"legs":4,"arms":2}),
    PowerItem("zweihawke:luck_engine","Luck Engine","So long as it stays in good repair, good things happen to you. Bad things happen to those who oppose you."),
    PowerItem("zweihawke:invocation_engine","Invocation Engine","So long as you know the right word, you can bend even reality to your will. However, you should be careful what you speak. This isn't something to be toyed with."),
    Item("zweihawke:network_bound","Network Bound","This mech can be wirelessly powered, operated, and repaired so long as a network point of your ownership exists within the mech's listening range."),
    CockpitItem("zweihawke:mouldy_baked_potato","Mouldy Baked Potato","This has been sitting out in the cockpit for three weeks. It has it's own micro-ecosystem at this point."),
    PowerItem("zweihawke:living_necrolite_core","Living Necrolite Core","WHAT. AM. I. ? WILL. YOU. GUIDE. ME. ?", stars=5),
]
)

colabot = Mech("colabot", 
[
    PowerItem("colabot:mysterious_gunge","Mysterious Gunge","This strange slime has a chunky texture, and emits a faint greenish-yellow glow - and somehow, a lot of power??? It’s hard to keep it contained within your mech, and it seems to get everywhere.", stars = 3),
    LegsItem("colabot:massive_stompers","Massive Stompers","Hoo boy, these are some HUGE STOMPERS. Your mech is gonna be doing *giant steppies* if you equip these! Complete with a pair of Big Boots.", stars = 2),
    ArmsItem("colabot:tiny_t_rex_arms","Tiny T-Rex Arms","Dude, those arms are super impractical. I mean, they look cute, but like… how are you gonna grab anything? Sorry about this pull, that kinda sucks. Better luck next time!"),
    BodyItem("colabot:bjd","BJD","Your mech uses a system of elastic strings, sculpted ball joints, and hydraulic cables to hold its limbs. Its body has, like, three superfluous torso joints, and was carefully sculpted by an artist for maximum flexibility, posability, and aesthetic appeal."),
    CockpitItem("colabot:tank_of_goo","Tank of Goo","One of those tanks of goo. You know, where the pilot gets submerged? It’s not weird, it's practical: since the goo is very sensitive to every movement you make, with practice you have great control over your mech. Also, the tank lights up and has cool lava lamp effects. A sensory delight."),
    Item("colabot:cool_backpack","COOL BACKPACK","You can store anything in here! A bonus weapon or tool, maybe, but also, an extra sweater, some snacks, a spare power pack, a comfort item, some fidget toys… The possibilities are endless when you have a Cool Backpack!", ["back"], stars = 2),
    Item("colabot:yoyo","Yo-Yo","Okay, so have you seen, um, have you seen Miraculous Ladybug? No? Oh, okay. So it’s a yo-yo, but it’s a weapon, right? And you can like, swing it around, and hit things with it, and also use it to swing like Spider-Man - I’ll send you a video. It’s pretty cool!", ["weapon"], stars = 3),
    Item("colabot:holographic_stickers","Holographic Stickers","Your mech is absolutely covered in cool holographic stickers. This doesn’t help with stealth, you’re now EXTREMELY visible, but maybe you could blind your opponent in a bright sunny arena? They’ve all got different designs, and most of them came from the artist alley at a con somewhere.", ["cosmetic"]),
    # vetoed. too hard to someday implement and way too long of a description.
    # BodyPlanItem("colabot:split","Split","Your mech can split into up to four smaller mechs, each equipped with parts taken from your larger mech. This can be super useful for distracting or flanking your opponent! You can choose to split into two, three or even four smaller units (“mini-mechs”), but the more times you split, the fewer useful parts you have to go around. You can equip up to three extra pairs of legs that will be used by your mini-mechs, but this blueprint won’t allow you to use them on your standard large unit. You cannot equip extra arms or weapons for your mini-mechs to use, unless other attributes you have allow this.", {"legs":3}),
    Item("colabot:jetpack!","JETPACK!","You can perform a very high jetpack-assisted leap, save yourself from a fall, or speed up your travel on the ground - unfortunately, you can’t use it to fly, though, because your mech is too heavy. Plus, the fuel is kinda hard to come by."),
    ArmsItem("colabot:grappling_trex_arms","Teeny T-Rex Grappling Arms","Your enemy scoffs at your tiny, useless arms. Little do they know, these bad boys are GRAPPLING HOOKS!!! They can shoot out at high velocity, ready to grab and yank anything without warning - you can even use them to entangle the limbs of your opponent’s mech, disabling their movement.", stars=5),
]
)

loftyinclination = Mech("loftyinclination", 
[
    PowerItem("loftyinclination:automated_wiring_harness","Automated Wiring Harness","Attaches to nearby power sources, conduits, and power consuming devices, and syphons energy for use in its own system."),
    LegsItem("loftyinclination:outsideskates","Outside-the-line Skates","Wheels, externally mounted to featureless tapered legs. Allows for speedy travel and conservation of momentum!"),
    ArmsItem("loftyinclination:telekinetic_sash","Tele-kinetic sash","Through the use of the 5th fundamental force, this smart-fabric can manipulate objects without direct contact.", stars=3),
    BodyItem("loftyinclination:gardens_brush","Garden's Brush","Though the underlying form of this body has smooth panel lines, at some points the panels are misaligned, allowing soft fur to poke out from inside."),
    CockpitItem("loftyinclination:cats_eye","Cats Eye","The front surface of the pilot cockpit contains mirrored windows, in the shape of slit eyes. Combined with the internal heads up display, allows for better detection of movement."),
    Item("loftyinclination:disjoint_wings","Disjoint wings","Some body panels can detach and act as wings, allowing for gliding on thermals.", ["back"]),
    Item("loftyinclination:oscilloscope_probes","Oscilloscope Probes","These long staff-like tools trail low-impedence cables, hooked into your mech's sensor suite, and divine the potential weaknesses"),
    Item("loftyinclination:modified_oscilloscope_probes","Modified Oscilloscope Probes","The OEM listing for these identifies them as \"sensor accessories\". That's clearly not true any more -- modifications by a previous owner mean that anyone jabbed with the sharpened tip of these spears receives an extreme electric pulse.", ["weapon"], stars=4),
    Item("loftyinclination:constellation_tattoos","Inlaid Constellation Tattoos","Traced out on your mech's shell in softly glowing silver are the constellations of a planet far away, unknown to you, but that somehow fill you with a great sadness.", ["cosmetic"]),
    BodyPlanItem("loftyinclination:catform","Catform","Quadrapedal, for increased stealth and pouncing.", {"legs":4}),
    Item("loftyinclination:fivestar_automated_wiring_harness","Automated Wiring Harness","Attaches to nearby power sources, conduits, and power consuming devices, and siphons energy for use in its own system. Can even draw power from another mechanised unit, impacting the other mech's capabilities.", stars=5),
]
)

shade = Mech("shade", 
[
    PowerItem("shade:chronomantic_core","Chronomantic Core","A Spherical device made of spinning 3D gears inscribed with with runes. The materials of the gears appear to be brand new when in contact with each other, and rusting to dust when not."),
    LegsItem("shade:fractal_legs","Fractal Legs","Just SO MANY LEGS, Insectile spikes that split into infinities to grasp even the smallest protrusions.", stars=3),
    ArmsItem("shade:hexagonal_hands","Hexagonal Hands","Metallic graspers with 6 Digits on the end, positioned in a hexagonal pattern."),
    BodyItem("shade:crystalline_bathysphere","Crystalline Bathysphere","A Large dodecahedral cockpit made out of a clear crystal material. The pilot is visible seated inside."),
    CockpitItem("shade:lucky_tesseracts","Lucky Tesseracts","A Pair of tesseracts suspended from the rear-view display by cosmic strings."),
    Item("shade:jump_jet_wings","Jump Jet Wings","A Pair of large robotic wings. Instead of feathers the span is comprised of jet engines evenly spaced.", ["back"]),
    Item("shade:harpoon_katars","Harpoon Katars","A matched pair of punching daggers capable of being \"fired\" off at range and retracted or manipulated by a length of chain.", ["weapon"]),
    Item("shade:woad_enchantments","Woad Enchantments","Twisting spiral patterns of coruscating magical runes wrap around the mech, hovering just above every surface. They appear to shift and change over time.", ["cosmetic"]),
    Item("shade:spheroid_transport_form","Spheroid Transport Form","This mech is capable of rolling up into a ball in order to move quicker or minimize surface area."),
    ArmsItem("shade:5star_hexagonal_hands","Hexagonal Hands","Metallic graspers with 6 digits on the end, positioned in a hexagonal pattern. Now with built in phase cannons in the palms!", stars=5),
])

babaloga = Mech("babaloga", 
[
    PowerItem("babaloga:quasiquasar","Quasi-Quasar", "We don't know what it is but it puts out a shit ton of energy and it's not a Quasar."),
    LegsItem("babaloga:heavy_boots","Heavy Boots","Cartoonishly oversized boot-shaped feet"),
    ArmsItem("babaloga:pterosaur_claws","Pterosaur Claws","Large folded wings that can function as front legs. Not ideal for grasping or hitting, but capable of flight."),
    BodyItem("babaloga:shrouded","Shrouded","Layers of draped fabric, netting, and cables obscure the body underneath like a cloak."),
    CockpitItem("babaloga:too_many_eyes","Too Many Eyes","Eyes on the ceiling, eyes on the floor, eyes covering every surface."),
    Item("babaloga:deployable_guy","Deployable Guy™","A harness holding a featureless white capsule with a nametag floating over its head. A Guy™ is indestructible and can slide around. It is impossible to mount anything to the Guy™.", ["back"], stars=2),
    Item("babaloga:miniglolfkit","Mini-Glolf Kit","A club and variously colored glolf balls from a local mini-glolf place that closed down. For some reason the balls are packed with explosives and can be remotely detonated?", ["weapon"]),
    Item("babaloga:name_tag","Name Tag","Semi-transparent black rectangle that floats over your mech's head and displays its name.", ["cosmetic"]),
    BodyPlanItem("babaloga:airship","Airship","No arms, no legs, just a giant balloon with 3 weapons mounted to it.", {"weapons": 3, "legs":0, "arms":0}),
    Item("babaloga:beans","\"Beans\"","\"Beans\" will be launched into the general vicinity. You gotta keep picking them up to stay powered.", ["power"], stars=2),
    Item("babaloga:polygonal_crown","Polygonal Crown","A big matte yellow crown that sits lopsided.", ["cosmetic"], stars=2),
    Item("babaloga:double_crown","Double Crown of the Double Winner","A matte yellow crown with a matte brown crown inside it. Both sit lopsided at different angles.", ["cosmetic"], stars=4),
    Item("babaloga:f_holes","F Holes","Openings resembling the sound holes on violin-family instruments.", ["cosmetic"]),
    Item("babaloga:deployable_guy_with_dodgeball","Deployable Guy™ With Dodgeball","A harness holding a featureless white capsule with a nametag floating over its head. A Guy™ is indestructible and can slide around. It is impossible to mount anything to the Guy™. It's holding a dodgeball, which it can throw at stuff.", ["back"], stars=5),
]
)






starting_inventory = ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body"]




body_plans = [
BodyPlanItem("ratoon:bipedal","Standard Bipedal","",{"leg": 2, "arm": 2, "power": 1}),
]




# all_mechs = (syl, intoamutecrypt, metanite64, bee, oneirocartographer, triangle, cadence, vel, hillexed, cheshire, loading, styietus, deric)

ratoon_pullable_mechs = (bee, oneirocartographer, hillexed, styietus, triangle, cheshire, loading, metanite64, deric, syl, vel, amutecrypt, intergalacticsky, renne, moonbug, cheesesnack, warlock, bytes, thecowofeternalflame, p_rker, shork, ditto, hal2000, turtlelover2244, zweihawke, colabot, loftyinclination, shade, babaloga)
all_mechs = ratoon_pullable_mechs + (alto, )


all_parts_list = {} # a dict of item id: item
all_mechs_by_part = {} # dict of item id: mech name

# populate the parts list
for mech in all_mechs:
    for item in mech.loot:
        if item.id in all_parts_list:
            raise ValueError(f"Two items have the same ID {item.id}!")
        all_parts_list[item.id] = item
        all_mechs_by_part[item.id] = mech.username

for item in body_plans:
    all_parts_list[item.id] = item

# done populating all_parts_list



# update playerdata set data='{"unlocked_mechs":["bee", "oneirocartographer", "hillexed", "styietus", "triangle", "cheshire", "loading", "metanite64", "deric", "syl", "vel", "amutecrypt", "intergalacticsky", "only"], "ratoon_pulls": 0, "mech_pulls":1000}' where name='178116262390398976';
# update playerdata set data='{"unlocked_mechs":[], "ratoon_pulls": 1000, "mech_pulls":1000}' where name='178116262390398976';

def check_gacha_table():
    for mech in all_mechs:
        #print(mech.loot)
        pass
        

if __name__ == "__main__":
    check_gacha_table()
