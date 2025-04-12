from dataclasses import dataclass
from enum import Enum

from gacha_mechanics import TagType, Mech, Item, PowerItem, BodyItem, ArmsItem, LegsItem, WeaponItem, BodyPlanItem, CockpitItem, BackItem, CosmeticItem, KitItem




bee = Mech("bee", [
    PowerItem("bee:star_drive", "Star Drive","The heart of a solar system, keeping the mech together and providing it power.", stars=2),
    LegsItem("bee:dark_matter_propulsion", "Dark Matter Propulsion","The force that keeps everything apart and the universe expanding. It also makes your mech go fast!", stars=2),
    ArmsItem("bee:gravity_wells", "Gravity Wells","The force that keeps things in orbit, and also the force to grab things with your mech!"),
    BodyItem("bee:rocky_armor", "Rocky Armor","Rocks float around the core to protect it and provide structure to your mech."),
    CockpitItem("bee:orbital_cockpit","ORBital Cockpit","A transparent bubble with no gravity within it, controls floating around effortlessly where you need them to be, controlling it almost like a dance."),
    BackItem("bee:cloak_of_stars","Cloak of stars","A field of stars that moves and adapts as an armor where you need it to, absorbing medium impacts provided you move it to the impact site before the impact happens.", stars=4),
    WeaponItem("bee:void_slicer","Void Slicer","A glittering blade so sharp that it feels like it can tear the fabric of space if you put enough force into it. it leaves a glittering trail.", stars=2),
    CosmeticItem("bee:living_satellite","Living Satellite","A small planet orbits your mech, supporting a microcosm of life.", stars=3),
    BodyPlanItem("bee:comet_form","Comet Form","A long thin form, with one leg and 6 arm slots, trailing behind the cockpit and core like a comet trail.",{"legs": 1, "arms": 6}, stars=4),
    CosmeticItem("bee:satellite","Gas Satellite","A small ball of swirling gasses orbits your mech.", stars=3),
    CosmeticItem("bee:gas_satellite","Rock Satellite","A tiny comet and trail orbit your mech.", stars=3),
    CosmeticItem("bee:artificial_satellite","Artificial Satellite","A small artificial space structure (a satellite, space ship, etc) orbits your mech.", stars=3),
    PowerItem("bee:blackhole_drive","Blackhole Drive","An infinitely deep hole in reality, the pull of the density object in the universe, contained only by the mech itself.", stars=5),
    PowerItem("bee:supernova_drive","Supernova Drive","A core of swirling energy, the captured explosion of a star, held together with the force of dark matter. Iridescent and an unstoppable force.", stars=5),
    WeaponItem("bee:gravitational_lensing", "Gravitational Lensing", "Using gravity, you can shunt power in to a strong focal beam to stab through your enemies at range.", stars=4),
    WeaponItem("bee:gravity_mines", "Gravity Mines", "These mines stick to surfaces and change gravity in their radius, both strength and direction can be changed upon, but not after, throwing. ", stars=4)
]
)

oneirocartographer = Mech("oneirocartographer", 
    [
    PowerItem("oneirocartographer:luminescent_core","Luminescent Core","A tarnished brass octahedron, a glow from within visible through the colored-glass apertures on its faces.", stars=2),
    LegsItem("oneirocartographer:rangers_arachnopoda","Ranger's Arachnopoda","Ceramic-plated insectoid legs, designed to climb giant trees and negotiate dense plant growth without losing stability.", stars=3),
    ArmsItem("oneirocartographer:manipulator_assembly","Manipulator Assembly","A pair of mismatched claw-grippers; one large and sturdy, the other small and meant for delicate work."),
    BodyItem("oneirocartographer:canopy_viewpoint","Canopy Viewpoint","A small, brass-and-ceramic chassis, built for visibility from the cockpit first and foremost."),
    CockpitItem("oneirocartographer:gyroscopic_suspension","Gyroscopic Suspension","This cockpit rotates within the mech's chassis, keeping the pilot upright, in order to prevent physical stress when at odd angles to the ground."),
    BackItem("oneirocartographer:container_lockpoint","Container Lockpoint","Grippers with which a container can be securely attached to the mech's body. Usually used to carry extra supplies on long expeditions."),
    WeaponItem("oneirocartographer:sling_blade","Sling Blade","For cutting a path when the canopy or the undergrowth is too thick to traverse."),
    CosmeticItem("oneirocartographer:phalerae_bryophyta","Phalerae Bryophyta","Verdant moss splotches the body of this mech, almost resembling a patchwork quilt.", stars=2),
    BodyPlanItem("oneirocartographer:arachnopod","Arachnopod","Eight legs, two \"arms\" (in more the position of chelicerae).", {"arms": 2, "legs": 8}, stars=4),
    KitItem("oneirocartographer:diffractive_heliograpb","Diffractive Heliograph","A reflective lattice of metal used for long-range visual signaling."),
    CockpitItem("oneirocartographer:dendritic_interface","Dendritic Interface","The cockpit has been overgrown with roots and branches, shaping themselves around the pilot's movements.", stars=3),
    ArmsItem("oneirocartographer:manipulator_assembly_tier_2","Manipulator Assembly EX","A pair of mismatched claw-grippers; one large and sturdy, the other small and meant for delicate work. Each arm unfolds into several grippers in an array of sizes and materials. A practiced pilot can use these to pick up nearly anything without damaging it.", stars=5),
    KitItem("oneirocartographer:remote_hardlight_gauntlets","Remote Hardlight Gauntlets","Allows hardlight 'echoes' of the mech's arms to be summoned at a distance, copying its movements. Pilots should note that while the Gauntlets are fully capable of manipulating objects, they will not replicate items held by the mech's physical arms.", stars=4),
    CosmeticItem("oneirocartographer:silva_phasma","Silva Phasma","A tiny forest spirit has stowed away aboard your mech to see more of the world.", stars=3),
]
)


hillexed = Mech("hillexed", 
[
    PowerItem("hillexed:antimatter_tea","Antimatter tea","A transparent container of hot antibeverage! A steel handle attached to glass lets you see the powerful magnets within. Drink it to unlock the vast wellspring of energy inside your mouth!"),
    LegsItem("hillexed:teeny_mechanized_legs","Teeny mechanized legs","Someone wasn't clear about millimeters versus meters. It looks like someone turned a robotic arm upside-down, full of joints and motors. That can't possibly be a baby shoe on the end, can it?", stars=2),
    ArmsItem("hillexed:neutron_star_on_a_stick","Neutron Star on a Stick","The ultimate fishing rod. Cast the line to throw the white-hot neutron star towards something you want to grab, and once gravity sticks the two together, reel it in. If you're really good, you can set up an orbit!"),
    BodyItem("hillexed:parabolic_block","Parabolic Block","A pancake-shaped glass cylinder, with attachment points along the edge. One side is curved into a mirrored parabolic depression, with three trusses holding up items to its focal point. The dish can reflect and concentrate energy into sensors, or lasers can bounce off the dish to make giant beams!"),
    CockpitItem("hillexed:crochet_controls","Crochet Controls","Two levers with a hook at the end. Grab one in each hand and wrap them around the strings of fate and warp the universe. The strings make a nice soft place to rest tired heads."),
    BackItem("hillexed:charge_couple_device","Charge/couple device","A sensor array of tiny purple squares arranged in a grid, able to build pictures of energy and light. Incredibly sensitive and capable of taking pictures or video, especially if boosted by a parabolic dish, but that sensitivity can be overwhelmed by strong marriages.", stars=2),
    WeaponItem("hillexed:info_dumper","Info Dumper","It looks like someone combined a backhoe with a cellphone. A data transmitter repurposed to overwhelm foes with information.", stars=2),
    CosmeticItem("hillexed:glolf_patches","Glolf Patches","A decal of a square grid of emojis depicting an eagle's eye view of a game in progress. Mostly green, with some white and yellow circles, glolfers' animal signatures, and is that depicting a crack in reality?"),
    BodyPlanItem("hillexed:starfish_mode_legs","Starfish mode: Legs","Five legs spaced around the center parabolic dish. If you balance the weight, the parabolic dish can roll on its edge to get around!", {"legs": 5}, stars=4),
    BodyPlanItem("hillexed:starfish_mode_arms","Starfish mode: Arms","Five arms spaced symmetrically around the center. If you balance the weight, you can roll on its edge to get around!", {"arms": 5}, stars=3),
    KitItem("hillexed:findermech","Findermech","Like a finderscope, but a mech! A smaller copy of your mech that goes on your bigger mech to help you maneuver the bigger mech."),
    KitItem("hillexed:telescope","Telescope","A large tube that concentrates light to unlock the universe. Attach it to a mech for long-range observations, or have the mech hold it up to your cockpit."),
    KitItem("hillexed:slitless_spectrograph","Slitless Spectrograph","A tangle of fiber optics that splits light and projects a rainbow of colors covered by occasional black lines into a cockpit. Those lines tell you so much information about what molecules absorbed or reflected the light you're looking at!", stars=3),
    BackItem("hillexed:death_bed","Death Bed","Part of your mecha is particularly soft and comfy, looking like a bed with a soft pillow. Despite the danger, the public swears it's worth climbing on your mecha to try lying on top of it. They'll die on this hill.", stars=3),
    BodyItem("hillexed:cassegrain_style_parabolic_block","Cassegrain-Style Parabolic Block","A drum-shaped hollow tube on its side, with attachment points along the outer edge. It focuses energy like a Cassegrain telescope into a point on the back: the perfect place to put advanced sensors... or a weapon that can send energy frontwards into a giant beam of mass destruction.", stars=5),

])

styietus = Mech("St. Yietus",
[
    PowerItem("st_yietus:curseheart_engine","CURSEHEART ENGINE","A grinding mass of twisted machinery, alight with horror and hope. Within its bowels, misfortune and cruelty are catalyzed into fiercest resolve. Generates additional energy for each unique debuff affecting your mech.", stars=3),
    LegsItem("st_yietus:rotborn_stomper","ROTBORN STOMPER","A sturdy weatherproofed leg. Slow, but capable of brief bursts of agility. Gains charges over time which can be spent to perform short leaps. Leaps are faster than walking and clear low obstacles and small gaps. Slightly reduces the effects of debuffs.", stars=2),
    ArmsItem("st_yietus:rotborn_fist","ROTBORN FIST","A simple arm, covered in pitted armor and tipped with a large, gauntlet-like hand. Paired with a small remote manipulator for more delicate work. Its fist counts as a melee weapon whenever it is not equipped with a melee weapon. Slightly reduces the effects of debuffs.", stars=2),
    BodyItem("st_yietus:melancholic_visage","MELANCHOLIC VISAGE","A bulky armored torso with a masked head. Despite its battered condition it still looks ever ahead, towards a brighter future. It's tough, has good heat capacity, and reduces the effects of debuffs.", stars=2),
    CockpitItem("st_yietus:psychlink_mpi","PSYCHLINK MPI","A mysterious mask that draws closer the wills of a mech and its pilot, allowing them both to be pushed past their normal limits. Activated abilities can be used before their cooldowns end, at the cost of a large amount of heat and a longer, unskippable cooldown.", stars=3),
    BackItem("st_yietus:external_utility_pack","EXTERNAL UTILITY PACK","An armored backpack for storing extra-bulky equipment. Improves cooling and speeds up ability cooldowns. Slightly reduces the effects of debuffs.", stars=2),
    WeaponItem("st_yietus:slaghewn_warpick","SLAGHEWN WARPICK","A warpick crafted from industrial waste, resplendent with signs of use and repair. Not the most elegant of weapons, but its effectiveness is undeniable. Good base stats, effective against armor.", stars=1),
    CosmeticItem("st_yietus:titanweave_cloak","TITANWEAVE CLOAK","A massive, well-worn cloak designed to shield a mech's mechanisms from severe weather. Comes in a variety of styles and patterns.", stars=1),
    BodyPlanItem("st_yietus:tech_terror_body_plan","TECH TERROR BODY PLAN","An intricate, skeletal body plan that allows up to four arms or up to two weapons to be equipped instead of a body. Use at your own risk.", {"arms": 4}, stars=4),
    BodyPlanItem("st_yietus:kitbash_kit_adaptor","KITBASH KIT ADAPTER","A set of tools and materials used to combine parts in all sorts of unintended ways. Adds one additional slot of any type other than a body to your mech.", {}, stars=2), # todo: make work
    CosmeticItem("st_yietus:novelty_mug","NOVELTY MUG", "A plastic novelty mug, obtained through great personal effort. The sense of pride one gets from owning this object gives you a minor all-around stat boost. Nifty!", stars=3),
    KitItem("st_yietus:crescent_companion","CRESCENT COMPANION", "The moon-headed ghost of a fictional being has made its home in your mind or the systems of your mech. Can create a temporary aura around you that slows nearby enemies' cooldowns and cooling and mildly slows yours. Don't forget it or it'll fade away...", stars=4),
    CosmeticItem("st_yietus:weird_lil_guy","WEIRD LIL' GUY","A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.", stars=3),
    PowerItem("st_yietus:divinity_tap","DIVINITY TAP","A bony, eerily pristine variant of the CURSEHEART ENGINE. Generates additional energy for each unique debuff affecting you. Gain a toggled ability that greatly improves all stats but creates massive heat while active. You feel tired after using it.", stars=5),
    WeaponItem("st_yietus:megaton_impact","MEGATON IMPACT","Your mech's forearms have been enlarged to make room for titanic piston assemblies that can imbue a punch with devastating force when properly charged.", stars=2),
    WeaponItem("st_yietus:duo_turbines","DUO TURBINES","Your mech's forearms have been replaced by colossal turbojet engines that allow it to take to the sky. Its hands have been modified to act as propellers, sacrificing manual dexterity for the awesome power of flight! (and a sick sawblade attack)", stars=3),
    WeaponItem("st_yietus:gimmick_weapon","GIMMICK WEAPON","A specialized weapon built directly into the body of your mech. Will it fire a storm of bullets or a single mighty beam? Thunderbolts, harpoons, or a ring of pure light? Perhaps something entirely unique? Strike a pose, and lay waste to your enemies!", stars=2),
    WeaponItem("st_yietus:earthbreaker_dxl","EARTHBREAKER DXL","It's a big drill. A really big drill. So big, in fact, that even your mech struggles to wield it. A digging tool of truly cyclopean proportions. Capable of massive destruction, if you can handle the torque.", stars=3),
    WeaponItem("st_yietus:terremoto_devastation_cannon","TERREMOTO DEVASTATION CANNON","Never fire the Devastation Cannon without proper sonic, seismic, and psychic protection. Never aim the Devastation Cannon at anything you do not wish to destroy. Firing the Devastation Cannon in an inhabited area is considered an act of war.", stars=4),
    WeaponItem("st_yietus:torcha_lance","TORCHA LANCE","Somewhere between a beam weapon and an overgrown blowtorch, the Torcha Lance nonetheless proves effective at dispatching armored targets at medium range. Just remember your eye protection.", stars=2),
    WeaponItem("st_yietus:rattlegun","RATTLEGUN","A crude mech-grade automatic weapon, built quickly to be discarded just as fast... and yet, this one shows shows signs of care and customization.", stars=1),
    PowerItem("st_yietus:subbotin_ultradense_atom_drive","SUBBOTIN ULTRADENSE ATOM DRIVE","A bulky but reliable power source dating back to the earliest mech designs. Although widely considered obsolete due to its high weight, it remains a favorite among veteran pilots-and repair crews.", stars=1),
    BodyPlanItem("st_yietus:supertitan_body_plan","SUPERTITAN BODY PLAN","We've all asked ourselves the question: what if, instead of adding more parts to a mech, we just made it bigger? Finally, the answer is here! Now, I ask a new question: who needs agility when you have overwhelming force?", {"body":3}, stars=4),
    CosmeticItem("st_yietus:rust_and_meat","RUST AND MEAT","Your mech looks mechanical from a distance, but peer into the cracks in its corroded frame and you will find muscles and organs entwined with the mechanics.", stars=2),
])

triangle = Mech("triangle", 
[
    PowerItem("triangle:intrinsic","Arm: Prefix: Intrinsic","A small orb. The orb has 3 windows; within the darkness inside one can see a gently glowing triangle. No matter how you angle the orb, the triangle always faces you straight on", stars=3),
    LegsItem("triangle:leg","Arm: Prefix: Leg","Two stout legs tapering to comically small feet. The feet and part of the calves open up into a two-pronged gripper",stars=1),
    ArmsItem("triangle:arm_01","Arm: Prefix: Arm 01","Two seemingly straight-forward arms with quick-release couplers for attaching to the mech. There are pop-out handles in both the forearms and the biceps: the arms can detach/transform into weapons.", stars=1),
    BodyItem("triangle:central_unit","Arm: Prefix: Central Unit","A nice, rounded, sturdy torso perched atop a small hip/waist joint unit. There is a head, although it flows almost seamlessly into the torso. Folded into/against the chest are two small pincer arms, not unlike a crab's little moutharms. The head detaches to operate as a smaller, crablike mech", stars=4),
    CockpitItem("triangle:light","Arm: Prefix: Light","Sourceless mood lighting. Is it glowing like a rainbow? Soothing warm yellows? flickering street lamp? Did you choose the current mood, or did the mech? Regardless, it always feels Perfect for The Moment", stars=3),
    BackItem("triangle:locker","Arm: Suffix: Locker","A large backpack. It can carry multiple accessories inside, as well as features several clamps to hold more on the outside. The entire thing can eject to act as an arms locker", stars=2),
    WeaponItem("triangle:big","Arm: Prefix: Big","A massive hand/glove a regular arm can interface with. There is only one of these, but it can reposition its thumb to be right or left handed", stars=1),
    CosmeticItem("triangle:crown","Arm: Prefix: Crown","An ethereal crown of yellow light floating above the mech. Its points flicker like flames or the aurora borealis", stars=4),
    BackItem("triangle:more","Arm: Prefix: More","A smaller backpack that can nest inside/under another backpack; this features multiple quick release joint housings to allow a multiplicity of arms", stars=3),
    ArmsItem("triangle:arm_05","Arm: Prefix: Arm 05","Two seemingly straight-forward arms with quick-release couplers. There are pop-out handles in both the forearms and the biceps: the arms can detach/transform into weapons. This pair specifically feature the ability to fire projectiles", stars=2),
    ArmsItem("triangle:arm_04","Arm: Prefix: Arm 04: Rocket Arms","Two seemingly straight-forward arms with quick-release couplers. There are pop-out handles in both the forearms and the biceps: the arms can detach/transform into weapons. This pair specifically feature the ability to launch wholesale, like rockets", stars=4),
    ArmsItem("triangle:arm_02","Arm: Prefix: Arm 02","A specialized set of arms, instead of featuring handles and transformations like most, these can split in two general grevious-style.", stars=3),
    WeaponItem("triangle:classic","Arm: Prefix: Classic","A sword. Every mech needs a sword.", stars=2),
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
    BackItem("cheshire:glyph_thrusters","Glyph Thrusters","A series of runic circles project out from this object, framing the Mech and providing an arcane boost when needed", stars=2),
    WeaponItem("cheshire:ceremonial_blade","Ceremonial blade","A short, wicked looking dagger. There appears to be some sort of tube from the end of it that runs back into the mech, as though hydraulics add or remove some sort of fluid from it"),
    CosmeticItem("cheshire:viewing_chambers","Viewing chambers","Specialized glass that allows you to see the mechanisms inside of the machine. Designed to make repairs nice and easy."),
    CockpitItem("cheshire:stowaway_cheshire","Stowaway Cheshire","You've found them hidden in the right leg of your mech, siphoning gasoline with their mouth."),  
    BodyPlanItem("cheshire:centaur","Centaur","With four legs, this bodyplan is typically fashioned into a centaur like configuration, allowing an additional back slot to be equipped as well", {"legs": 4, "arms": 2, "back": 2}),
    BodyItem("cheshire:sigil_crusted_body","Sigil Crusted Body","What appears to be an old wooden ship or other reclaimed wood, covered in the still-burning sigils that animate it.", stars=3),
    CosmeticItem("cheshire:framed_picture_of_rival","A Framed Picture of your Rival","It's just a normal, totally platonic rival relationship. This picture is just framed to make you fight them better and not because you're repressed.", stars=2),
    CosmeticItem("cheshire:a_bunch_of_floating_spheres","A bunch of floating spheres","Strange energies have recently been detected coming off of these spheres. UP has asked you to keep a close eye on them for any changes.", stars=3),
    ArmsItem("cheshire:crystal_arms","Crystal Arms","What look like standard mech arms have been absolutely shredded by some sort of magical crystal growing out of the inside. They don't seem to have impeded the arms' functions at all", stars=4),
    PowerItem("cheshire:the_wheel","Core: The Wheel","A series of gear structures that appear to be powered by some sort of forest animal running very quickly on the center one.", stars=2),
    ArmsItem("cheshire:guardian_gauntlets","Guardian Gauntlets","Wide and flat, these arms can extend an energy barrier to deflect projectiles and force.", stars=2),	
    ArmsItem("cheshire:matryoshka_uppercut","Matryoshka Uppercut","When damaged, these arms eject their outer layer, revealing smaller and faster arms underneath.", stars=3),	
    ArmsItem("cheshire:sun_out_guns_out","Suns Out, Guns Out","	Solar powered forearms loaded with artillery that fire when activated. Artillery is more powerful with more intense light", stars=2),	
    PowerItem("cheshire:bottled_ghost","Bottled Ghost","The result of scrapping all those stowaway Cheshires. Technically, it only haunts the mech, it doesn't possess it.", stars=2),
    PowerItem("cheshire:friendship","Friendship","We all believe in you!", stars=3),
    BodyItem("cheshire:matryoshka_special","Matryoshka Special","When damaged, this armor violently ejects off of the mecha, revealing a smaller, faster, and more lethal mech.", stars=2),	
    BodyItem("cheshire:crystaline_armor","Crystalline Armor","Glowing crystal rising off of this mech give it a jagged and violent shape. The gems grow brighter as it stores energy, allowing them to rip into the body of grappled mechs", stars=3),
    LegsItem("cheshire:crystalline_greaves","Crystalline Greaves", "A faint glow emminates from these vibrant gemstone legs. The razor sharp crystals seem to resonate with magical energy", stars=2),
    WeaponItem("cheshire:bank_vault_shield","Bank Vault Shield","Ripped from the vault's hinges, nobody knows what happened to the rest of the bank", stars=2),	
    WeaponItem("cheshire:swarm_sheild","Swarm Shield","Six flat drones that form a shield of projected energy between them. Highly power consumptive", stars=4),	
    LegsItem("cheshire:matryoshka_kneesocks","Matryoshka Kneesocks","These long heavily armored legs are designed to explode plating off after taking damage, reducing your mechs weight and increasing its speed.", stars=3),
    ArmsItem("cheshire:castigator_arms", "Castigator Arms", "Covered in hooks and barbs, critical damage to these limbs causes them to erupt with energy, ideally while grappling with an enemy", stars=3),	
    ArmsItem("cheshire:socketed_slugger","Socketed Slugger","This limb is designed with a socket, allowing it to terminate in the weapon of your choice.", stars=2),
    WeaponItem("cheshire:gorgons_grace","Gorgon's Grace","Inscribed with terrifying images, this object calcifies and embrittles those that gaze upon it, corroding armor and spirit. Ranged", stars=4),	
    BackItem("cheshire:scorpions_talent","Scorpion's Talent","A massive chitinous tail tipped with a wicked barb. Designed to inject corrosive or pressurized gas directly into the enemy's cockpit.", stars=3),	
    BackItem("cheshire:back_mounted_turret","Back Mounted Turret","A platform for mounting ranged weapons on the back of your mech. Options include a railgun, laser rifle, or catapult", stars=3),
    KitItem("cheshire:monologue_protector","Monologue Protector","This device provides invincible plot armor for exactly 1 monologue during a mech fight. Additional (or needlessly long) monologues are not covered by this protection.", stars=3),	
    PowerItem("cheshire:amber_heart_tier_2","Amber Heart","This strange heart of carved amber beats in time with your own, and pumps a thick, dark ichor into your mech, powering it. The blood in your veins pulses euphorically when near it.", stars=5),
]
)

loading = Mech("loading", 
[
    PowerItem("loading:kinetic_recycler","Kinetic Recycler","A kinetic generator powered by the grounded movement of the mech", stars=2),
    LegsItem("loading:xr2","Loading's XR2","Long double jointed legs that give the mech a low crouching position while stationary, but a long stride", stars=3),
    ArmsItem("loading:knuckle_draggers","Knuckle Draggers","Long and delicate arms twice as long as the torso it is attached to", stars=2),
    BodyItem("loading:elongated_segment_frame","Elongated Segment Frame","Thin segmented spine that allows for maximum flexibility and aerodynamics", stars=3),
    CockpitItem("loading:gyrobomber","Gyrobomber","A gyroscopic cockpit with 300 degrees of visibility to allow for the stabilization of the cockpit even as the body contorts."),
    BackItem("loading:big_jacket","Big Jacket","A jacket that is two sizes too large. It flows in the wind, increasing evasion the more the mech moves.", ["cosmetic"]),
    WeaponItem("loading:hook_lash","Hook Lash","A whip with a spinning metal weight at the end that applies a random debuff on hit", stars=2),
    WeaponItem("loading:lockjaw_needler","Lockjaw Needler","A set of low damage, hig fire rate pistols that corrode any surface their projectiles make contact with", stars=3),
    KitItem("Loading:Power_Vents","Core Ventilation","In exchange for a more trimmed down mech you gain the ability to explosively vent waste from your power source.", stars=4),
    BackItem("loading:big_mechs_jacket","Big Mechs Jacket","A long flowing jacket based on the Mechs bomber jacket that flows behind the mech as it moves obscuring the body. It increases evasion and throws off targeting systems the more the mech moves.", ["cosmetic"], stars=5),
]
)

metanite64 = Mech("metanite64", 

[
    PowerItem("metanite64:sound_unit", "Sound Unit","An otherworldly amalgamation of sound chips from various retro game consoles. They probably shouldn't be intersecting each other like that. Or sparking so frequently."),
    LegsItem("metanite64:pumped_up", "Pumped Up","The feet appear to be dance pads from an ancient dancing-based rhythm arcade game. The legs are boxy yet streamlined, agile enough for some dancing of its own."),
    ArmsItem("metanite64:sylish_circut", "Stylish Circuit","A copper plate resides within the left forearm, etched to resemble a keyboard. With the metallic tips of the right hand's fingers, one may close the giant circuit and produce the purest sound."),
    BodyItem("metanite64:soundbox_5_1", "SOUNDBOX 5.1","A solid cube covered in a fine mesh material. The power source hovers in the center."),
    CockpitItem("metanite64:gba_cartridge_collection", "GBA Cartridge Collection","a GBA and a number of custom cartridges. One of them is the Nanoloop 2, while the rest each play a different looping musical work.", stars=2),
    BackItem("metanite64:roaring_wind", "Roaring Wind","Giant speakers. Bystanders may experience sudden deafness and strong winds.", ["weapon"], stars=3),
    WeaponItem("metanite64:hathors_blade", "Hathor's Blade","A gift from the goddess of music, modified beyond recognition into both a keytar and a giant sword.", stars=4),
    CosmeticItem("metanite64:waveform", "Waveform","A neon purple visual representation of the audio that the mech is currently playing. When the mech is silent, the waveform gradually shapeshifts between one of a few basic waves (sine, sawtooth, triangle, square).", stars=3),
    BackItem("metanite64:sheath_pockets", "Sheath Pockets","up to two extra weapons/tools can be stored alongside the mech's back accessory, fitting neatly into long pockets that criss-cross the mech's back.", stars=2),
    WeaponItem("metanite64:batonatone", "Batonatone","That Otamatone looks pretty mad. Even looking at it wrong would probably get you whacked on the head.", stars=2),
    WeaponItem("metanite64:don_and_ka", "Don and Ka","Two ancient ritual drumsticks, one orange and one blue. Taiko not included.", stars=2),
    CosmeticItem("metanite64:golden_fiddle", "Golden Fiddle","It's said that a mere boy won this fiddle after besting the Devil in a duel of music. Some say that they've heard the fiddle playing itself.", stars=3),
    BackItem("metanite64:cobras_roar", "Cobra's Roar","5 star of the Roaring Wind. Even giant-er speakers. Either through deafness or death, the roar of the cobra is the last thing you'll get to hear.", ["weapon"], stars=5),
]
)

deric = Mech("deric", 
[
    PowerItem("deric:spite_malace_or_anger","Spite, Malice, or Anger","The machine can only move when the pilot gives it their anger. It drains them of this, channeling it into the various systems."),
    LegsItem("deric:a_fract_set_of_bulky_legs","A Fract Set Of Bulky Legs","They emerge from under the core, looking more like huge slabs of metal or some other material, with thunderous stomps as they move in waves."),
    ArmsItem("deric:impossible_anti_gravity_device","Impossible Anti-Gravity Device","A blocky stump points at an object to be lifted, and it rises, with no physical contact made."),
    BodyItem("deric:a_gargantuan_slab_of_concrete_or_metal","A Gargantuan Slab of Concrete or Metal","There is some trim details and cracks, but the surface is otherwise unembelished and strangely barren."),
    CockpitItem("deric:tethered_memory","Tethered Memory","Something that you miss dearly and wish you could take out of the mech."),
    BackItem("deric:jagged_spine","Jagged Spine","A Horrific Spine of Jagged Spikes and Antennae"),
    WeaponItem("deric:improvised_weaponry","Improvised Weaponry","Anything it can pickup and lift can and will be its weapons."),
    CosmeticItem("deric:concrete_body","Concrete Body","The mech is made almost entirely of concrete, with small bits of metal holding some sections together."),
    KitItem("deric:living_quaters","Living Quarters","The Mecha contains a full (if small) living quarters further inside, allowing long-term deployments without support.", stars=3),
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
    BackItem("syl:vending_machine", "Vending Machine","Tied to the back of the mech, possibly as a counterweight, is a battered old vending machine. The chips and cookies inside are somehow still intact despite years of mech battling.", ["cosmetic"]),
    WeaponItem("syl:plain_palms", "Plain Palms","This mech has no primary weapon, but prefers hand-to-hand combat. Specifically, it slaps people."),
    CosmeticItem("syl:fallen_leaves", "Fallen Leaves","Old leaves from aspen trees are stuck to the sides and roof of this mech, as if it had just walked through a forest."),
    BodyPlanItem("syl:dual_cockpits", "Dual Cockpits", "This mech has two seats for two pilots to sit alongside, if they are Drift Compatible. (A second player joins your mech in battle to split the task of operating it.)", {"cockpit": 2}, stars=5),
    CosmeticItem("syl:tied_up_horse", "Tied-Up Horse","This mech has a horse tied up to one of its legs. Not sure how it stays there in combat."),
    CosmeticItem("syl:space_pinup", "Space Pinup","On the side of this mech, painted in bright neon colors, is a pinup of a shirtless Jar Jar Binks.", stars=3),
    CockpitItem("syl:single_tape_boombox", "Single-Tape Boombox","This mech has a retro boombox in the cockpit, and the tape that is unremovably stuck in it is “Greatest Hits Volume 1” by the Eagles."),
    BackItem("syl:redbox_machine", "Redbox Machine", "Tied to the back of the mech, possibly as a counterweight, is a battered old Redbox machine, but the movies it dispenses are ones no one has ever seen before. Recently, you rented Goncharov (1973) by Martin Scorsese.", ["cosmetic"], stars=5),
    BackItem("syl:guavapon","Guavapon","Dispenses guavas of varying rarities, from Common to Legendary.",stars=2),
    CosmeticItem("syl:horse_head","Horse Head","Found in the bed of some mafioso, it drips blood constantly and occasionally eats oats.",stars=2),
    BackItem("syl:ponytail","Ponytail","Hair put up in a style associated with young girls and butch lesbians. Goes all the way down your mech’s back.",stars=2),
    WeaponItem("syl:horse_gun","Horse Gun","Fires a Clydesdale horse at relativistic speeds.",stars=5),
    WeaponItem("syl:horse_summoning_staff","Horse Summoning Staff","Summons normal but very angry horses to fight alongside you.",stars=3),
    KitItem("syl:bag_of_oats","Bag of Oats","It’s a bag of oats. ",stars=2),
    WeaponItem("syl:curry_comb","Curry Comb","You can brush a horse with it, or throw it at someone in a pinch.",stars=1),
    LegsItem("syl:pony_express","Pony Express","Gives your mech the speed and stamina of a cross-country horseback mail courier.",stars=4),
    CosmeticItem("syl:horse_joker","Horse Joker","A paper playing card with a horse in clown makeup on it. +1 Mult for every horse-themed part equipped.",stars=3),
    CockpitItem("syl:saddle","Saddle","Found in village chests and underground mine shafts. ",stars=1),
    CockpitItem("syl:epona","Epona","This iconic horse has blocky N64-era graphics but a pure heart. Pilots your mech for you and is “equipped” as a second cockpit.",stars=3),
    WeaponItem("syl:glue_factory","Glue Factory","Sprays Elmer’s glue at opponents. Don’t worry about what it was made out of.",stars=2),
    KitItem("syl:horse_girl_hypnosis","Horse Girl Hypnosis","Upon viewing this battered VHS tape, you become filled with the urge to put your hair in a ponytail and buy plastic horse models.",["cosmetic"],stars=5),
]
)


vel = Mech("vel", 
[
    PowerItem("vel:big_reactor", "Big Reactor","A big reactor thingy (prolly nuclear adjacent) that gets refueled by hoisting big cartridges in it.", stars=3),
    LegsItem("vel:sleek_legs", "Sleek Legs","Two sleek legs and high output thrusters.", stars=2),
    ArmsItem("vel:manipulators", "Manipulators", "Hand-like manipulators for big stuff, prolly some small claws on cranes for small stuff."),
    BodyItem("vel:bipedal_frame", "Bipedal Frame","A human-like core (proportions may vary) with advanced sensors near the head or on it."),
    CockpitItem("vel:external_cockpit", "External Cockpit","outside cockpit? it has some periscopes/small windows as a backup."),
    BackItem("vel:booster_backpack", "Booster Backpack","A backpack with one or two massive boosters with added drop tanks and some light equipment to like change the fuel cell, and ammo/technical equipment/jamming equipment.", stars=4),
    WeaponItem("vel:retractible_swords", "Battle-Tested Loadout", "A long carbine (think SVD or FRF-1), knife(ves)/retractible swords with the handle tucked in the forearms, plus countermeasures/stun launchers in the limbs.", stars=3),
    CosmeticItem("vel:pilot_emblem", "Pilot Emblem", "A big pilot emblem on a shoulder/skirt/side of the bust with a 2-3 colored paint scheme.", stars=2),
    BodyItem("vel:durability_frame", "Durability Frame","For improved durability, this body has differently-colored protection plates, big fatter limbs and a rugged drilling or artillery equipment backpack. There are added hardpoints, protection and ground mobility equipment. The sensor-heavy head wears a helmet.", stars=3),
    BodyItem("vel:ace_custom_frame", "Ace Custom Frame","This mech is a special personal unit of a famous ace/freedom fighter that's fighting for the betterment of humanity, it's based from a standard military/industrial unit, but was heavily modified and customized to fit a more exploration, reconaissance, sharpshooting role.", stars=5),
]
)

amutecrypt = Mech("amutecrypt", 
[
    PowerItem("amutecrypt:new_killer_star","New Killer Star","A caged sun, kept behind some thick shielding.", stars=3),
    LegsItem("amutecrypt:the_awesome_foursome","The Awesome Foursome","4 heavy, industrial legs, designed for defence and redundancy."),
    ArmsItem("amutecrypt:i_thought_about_the_army","I Thought About The Arm-y","Two industrial robotic arms."),
    BodyItem("amutecrypt:the_part_formerly_known_as","! (The Part Formerly Known As)","A stout core with the arms mounted high up, like Atlas from Portal."),
    CockpitItem("amutecrypt:okayish_computer","Okayish Computer","An AMD CPU hanging like a pair of fluffy dice would."),
    BackItem("amutecrypt:thrill_the_dj","Thrill The DJ","A big set of speakers."),
    WeaponItem("amutecrypt:shellshot","Shellshot","A launcher capable of firing adhesive, caltrops and other traps."),
    CosmeticItem("amutecrypt:thunderbirds_are_coming_out","Thunderbirds Are Coming Out","Makes the mech look like a puppet."),
    KitItem("amutecrypt:disc_changer","Disk Changer","Allows you to mount 3 power sources, but only one can be active at a time.", stars=3),
    KitItem("amutecrypt:parallel_player","Parallel Player","Allows you to mount 3 power sources, **and all can be active at once**.",stars=5)
]
)

intergalacticsky = Mech("intergalacticsky", 
[
    PowerItem("intergalacticsky:microfission_cell","Microfission cell","A fairly small but notoriously temperamental setup, smaller than the batteries it charges. Must be shut down in combat and environmentally hazardous situations."),
    LegsItem("intergalacticsky:needlepoint_contacts","Needlepoint contacts","Auto-balancing limbs designed to minimize environmental damage."),
    ArmsItem("intergalacticsky:augmenting_manipulators","Augmenting Manipulators","A set of nimble, thin arms with a variety of ways to grasp and manipulate objects, ranging from the size of a cat to a small tree."),
    BodyItem("intergalacticsky:gyroscopic_pod","Gyroscopic Pod","A fairly stable structure built to contain pilot, sensitive instruments, and any samples as securely as possible within a larger structure."),
    CockpitItem("intergalacticsky:stargazers_instruments","Stargazer's Instruments","A variety of measurement devices to assist in your endeavors."),
    BackItem("intergalacticsky:solar_fins","Solar Fins","Large, retractable solar panels used as supplementary power support."),
    WeaponItem("intergalacticsky:mistcutter","Mistcutter","A sample cutting tool able to use water or grit, depending on environmental availability."),
    CosmeticItem("intergalacticsky:teeth","TEETH.","",stars=3),
    BodyPlanItem("intergalacticsky:surveyors_adaptaion","Surveyor’s Adaptation","By sacrificing limb mobility (or consolidating them), the mech now can withstand over 16,000 PSI at the weakest point. (Not tested against damage from artillery, temperatures over 900C, or twisting force.)", {"legs": 1}),
    BodyItem("intergalacticsky:the_fishbowl","The Fishbowl","A mostly spherical core built of transparent, UV-protective material. May be rendered one-way."),
    LegsItem("intergalacticsky:paddleboards","Paddleboards","Flexible fins originally made for movement in shallow waters. Can also be used for land maneuvers, to some effect."),
    ArmsItem("intergalacticsky:noodlers","Noodlers","Limbs made specifically for catching large, predatory fish."),
    CosmeticItem("intergalacticsky:bare_joints","Bare Joints","Through the power of easily-replaced and cleaned parts, the joints on limbs are now bare!"),
    WeaponItem("intergalacticsky:frogflare","Fogflare","A heavily modified and overclocked cutting tool able to use water or grit, depending on environmental availability. Dubiously legal.", stars=5),
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
    CockpitItem("renne:mystic_union","Mystic Union","Tendrils within the main cavity meld themselves to the pilot's extremities and the back of their neck, making it so they see and feel everything the mech can—and can control it as they would their body. This means they feel damage to the mech as pain, and for any mind, perception is reality...", stars=3),
    BackItem("renne:hanging_garden","Hanging Garden","This mech has a space on its back where life flourishes. Outside of battle, it may serve as a sanctuary, or a place to grow food.", stars=3),
    WeaponItem("renne:hedge_clipper_turbo","Hedge Clipper Turbo","A massive pair of scissors; the individual blades can split off into dual swords, single-edged."),
    CosmeticItem("renne:time_ravaged","Time-Ravaged","This mech is made of finely-chiseled stone covered in ancient artistic engravings, and much of it has been worn down by time and the elements. Parts of it are held together by plant growth that has overtaken it.", stars=3),
    BodyPlanItem("renne:beastly_deva","Beastly Deva","This mech was built to be a master of both terrain and adaptability, meaning any relation to the human form is more coincidental than anything. Controlling it may be tricky.", {"legs":6,"arms":4}, stars=4),
    CockpitItem("renne:spirit_of_the_earth","Spirit of the Earth","An embodiment of nature has taken residence inside this mech and communicates with the pilot. It does not speak human language, but long-term pilots claim to be able to understand it.", stars=2),
    ArmsItem("renne:ancillary_vines","Ancillary Vines","Growing out of the mech's body, these prehensile growths may not have the greatest durability to slashing weapons, but excel at wrapping around things and tethering them.", stars=2),
    CosmeticItem("renne:razor_maw","Razor Maw","This mech's face bears a large snout with which it can bite enemies. Who needs weapons when you have the ideal predator body?", stars=4),
    PowerItem("renne:caustic_engine","Caustic Engine","Some kind of bubbling acidic substance courses through this mech. How it doesn't eat through the thing is a small wonder.", stars=2),
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
    BackItem("moonbug:phase_shifter","Phase Shifter","A back mounted piece of obtuse and cobbled together wires and breadboards. It allows the mech to temporarily enter the immaterial for a few seconds. It is highly advised to keep immaterial exposure to less than an hour a year to prevent conceptual delamination.", stars=3),
    WeaponItem("moonbug:a.e.i.o.u","A.E.I.O.U","The Amazingly Explosive Igniter Of Unfire. Shoots lobs of un-napalm at enemies. Un-napalm is one of the few substances Unfire actually burns.", stars=3),
    CosmeticItem("moonbug:antennae","Antennae","Two feathery antennae are installed on the head of your mech. They won't be getting any signals, but they look adorable."),
    WeaponItem("moonbug:delta_theta_wave_generator","Delta-Theta Wave Generator","A piece of repurposed lab equipment, it is able to create the illusive Delta-Theta waves, which has mutagenic properties for some \"people\" (It's a speaker that turns you into an animal.)", stars=4),
    LegsItem("moonbug:legs_design_173","Design Type. 173","A pair of mech legs that seem to be crudely made of plaster and spray paint. Despite that, these legs are immensely flexible and mobile... if no one is looking at you."),
    BackItem("moonbug:finarian_phase_diver","Finarian Phase Diver","A back mounted piece of equipment upgraded and repaired across generations. It allows a mech to dive into the immateria. Dozens of stamped seals in Finarian tongue act as a blueprint and a ward to prevent unreality from leaking into the mech, letting it stride the depths for as long as it has power.", stars=5),
    LegsItem("moonbug:jpeg_leg","JPEG Leg","One leg is perfectly fine, the other is a crusty artifact ridden .JPG of a pegleg propping your mech up. ",stars=1),
    CosmeticItem("moonbug:tamagacha_toy","Tamagacha Toy","A mecha-sized digital pet held somewhere on your mech, make sure to keep it fed!",stars=2),
    KitItem("moonbug:l0ki_cyberwarfare_suite","L0KI Cyberwarfare Suite","A suite of automated scripts and exploits made by Core based cracking group Team L0KI allowing you to hack anything your mech can connect to, including other mechs. Wireless by default, it can use wired connections for more hardened targets.",stars=3),
    WeaponItem("moonbug:datablade","Datablade","An intricate blade embedded in the wrist of your mech that allows anything stabbed by it to connect to your mech. A locking mechanism allows the pilot to “unlatch” the blade inside the target and still wirelessly connect to it. ",stars=3),
    KitItem("moonbug:merriment_blockwall","Merriment Blockwall","Somehow, this B.A.C.K Archivist has found her way onto your mech. Her hair is grey, and her body isn't what it used to be... But she is glad for the adventure once again.",stars=4),
    CockpitItem("moonbug:neural_sync_array","Neural Sync Array","An array of connectors and hardware to allow 2 pilots to sync their thoughts with both the mech and eachother. While improvements in mech design has made copilots unnecessary, you can't beat that two heads are better than one.",stars=2),
    WeaponItem("moonbug:replica_glolf_club","Replica Glolf Club","A mech sized replica of a Glolf Club, an artifact of the forbidden splort. Does not come with a surfer pen.",stars=1),
    WeaponItem("moonbug:monarchs_club","Monarch's Club","An extradimensional instrument of the Forbidden Splort. No matter what, the cold metal of the club feels as it's in your own hands, and with it... The power to rend reality asunder. Engraved in the handle is RM <3 FM",stars=5),
]
)

cheesesnack = Mech("cheesesnack", 
[
    PowerItem("cheesesnack:biofuel_burner","Biofuel Burner","Accepts most animal and vegetable oils. Smells strongly of french fries when in operation."),
    LegsItem("cheesesnack:echinomotion_locomotive_system","Echinomotion Locomotive System","Inspired by starfish and urchins, hundreds of small, pneumatic feet shuffle the mech along. You won't win any races but they're capable of handling any terrain even at extreme angles. 35% of Echinomotion mech pilots develop lifelong grudges with the mechanics who have to maintain them.", stars=3),
    ArmsItem("cheesesnack:roper_manipulators","Roper Manipulators","Originally designed for clearing minefields, each \"arm\" consists of four tentacles that can snake, coil, and swing independently. Experts with the system can snatch tools and weapons from quite a distance, though many are content learning how to make sick whipcrack noises."),
    BodyItem("cheesesnack:recycled_vans","Recycled Vans","Some enterprising scavenger has gutted and reinforced two vans and welded them together in an intimate pose, looking like a scrapyard sculpture. Joints for the arms and legs have been installed where the wheels once sat. Only the mad or desperate would entrust themselves to this thing.", stars=3),
    CockpitItem("cheesesnack:foldaway_kitchenette","Foldaway Kitchenette","A metal cabinet tucked away in a corner conceals a small counter that folds out for simple meal prep with a knife rack, coffee brewer, and some space for food storage. Constructed by a pilot assigned to long and uneventful duties."),
    CockpitItem("cheesesnack:caravan","Caravan","The cockpit in this mech has a cabin that can be outfitted as a workspace, field kitchen, market stall, or a small apartment. Originally designed and manufactured for wilderness surveyors and prospectors, this item is prized among traveling merchants and nomadic tradespeople.", stars=3), 
    BackItem("cheesesnack:self_righting_device","Explosive Self-Righting Device","In the event that the mech falls on it's back, an explosive charge can be used to launch the mech upright. Currently subject to several lawsuits regarding back and neck injuries.", stars=3),
    WeaponItem("cheesesnack:pick_mattock","Pick Mattock","Warfare never really advanced beyond the need for earthworks and trenches. Pilots have discovered that the titanium pick on this tool pierces armor as easily as it does rock and stone.", stars=3),
    CosmeticItem("cheesesnack:branch_camoflage","Branch Camoflage","Tree limbs have been crudely attached to the shoulders. Enemy spotters might mistake this mech for a particularly mobile tree."),
    BodyPlanItem("cheesesnack:centipede_mode","Centipede Mode","An adapter system that allows the mech to crawl on many small legs", {"legs": 4}),
    ArmsItem("cheesesnack:five_star_roper_manipulators","Roper Manipulators","Originally for clearing minefields, each \"arm\" consists of four moveable tentacles. An experimental upgrade allows them to act completely independently of the mech; pilots can snatch weapons from afar, throw individual tentacles like boluses, or interlink tentacles together into one long tentacle.", stars=5),
    CosmeticItem("cheesesnack:superpositional_jacket","Superpositional Jacket","The downside of reversible jackets was that you could only wear one side at a time. This is no longer the case."),
]
)

spellweaver = Mech("spellweaver", 
[
    PowerItem("spellweaver:system_of_hamster_wheels","System of Hamster Wheels","They are intricately connected by a mechanism to a generator. The hamsters have a great union contract."),
    LegsItem("spellweaver:digitigrade_legs","Digitigrade Legs","Strong, animal-like legs with big paws and claws that can dig into the ground for support"),
    ArmsItem("spellweaver:sable_arms","Sable Arms","Extendible animal-like arms with big paws and claws for grabbing."),
    BodyItem("spellweaver:forest_sable","Forest Sable","Camouflaged to blend in with dirt and forests, the slender body of this mech is perfect for hiding in plain sight."),
    CockpitItem("spellweaver:library_membership_card","Library Membership Card","With this, you can download ebooks, audiobooks, music, and games! Plus, you can check out physical materials at your local library.", stars=2),
    BackItem("spellweaver:big_backpack","Big Backpack","this comedically large backpack is actually great for storing things. It’s water-resistant, but not waterproof.", stars=3),
    WeaponItem("spellweaver:big_hammer","Big Hammer","Giant two-handed war-hammer. Fun to spin around with!"),
    CosmeticItem("spellweaver:pride_&_pronoun_pins","Pride & Pronoun Pins","Colorful, easily legible, allows you to share your identity with the world", stars=2),
    BodyPlanItem("spellweaver:combat_animal","Combat animal","Four legs, 2 weapon slots on back.", {"legs": 4, "weapon": 2}),
    CosmeticItem("spellweaver:giant_beaglepuss","Giant Beaglepuss","Also known as Groucho Marx glasses, they are lensless and have a comedic fake nose and mustache attached.", stars=3),
    BodyItem("spellweaver:massive_speaker_system","Massive Speaker System","With this, you can blast music, or unleash a bestial roar that can be heard for miles.", stars=3),
    BodyItem("spellweaver:winter_marten","Winter Marten","Camouflaged to blend in with ice and snow, the slender body of this mech is perfect for hiding in cold environments.", stars=3),
    PowerItem("spellweaver:the_soup_engine","The Soup Engine","Just pour some soup in there, or a smoothie, and it’ll run real good!", stars=4),
    LegsItem("spellweaver:advanced_digitigrade_legs","Advanced Digitigrade Legs","Strong, animal-like legs with big paws and claws that can dig into the ground for support. These legs can be super-charged, crackling with blue electricity to give you incredible speed boosts, letting you run faster than should be reasonably possible, even up walls!", stars=5),
]
)

bytes = Mech("bytes", 
[
    PowerItem("bytes:dying_star","Dying Star","The radioactivity of this source makes it very effective yet very unstable."),
    LegsItem("bytes:hover_jets","Hover Jets","These jets allow universal transit over a variety of terrains by never making contact with the ground.", stars=2),
    ArmsItem("bytes:magnetized_grabbers","Magnetized Grabbers","These claws are extremely effective and lifting and holding magnetic materials."),
    BodyItem("bytes:steel_casket","Steel Casket","This durable chassis has boxy edges and thick armor."),
    CockpitItem("bytes:climate_controller","Climate Controller","This high-tech cockpit accessory provides great comfort to the pilot regardless of the condition."),
    BackItem("bytes:long_range_warp_boosters","Long Range Warp Boosters","These boosters allow for rapid yet poorly controlled mobility over distance.", stars=4),
    WeaponItem("bytes:harvest_claw","Harvest Claw","This massive melee weapon is comprised of several blades and is capable of inflicting devastating damage."),
    CosmeticItem("bytes:split_paintjob","Split Paintjob","This chaotic paintjob has no left-right symmetry.", stars=2),
    BodyPlanItem("bytes:cruiser_form","Cruiser Form","This vehicular form is well adapted for high speeds and endurance.", {"legs": 0}),
    KitItem("bytes:short_range_teleporters","Short Range Teleporters","These devices make use of anomalous technology to teleport short distances to evade attacks.", stars=3),
    BodyItem("bytes:aerogel_heat_shell","Aerogel Heat Shell","This lightweight material provides immense resistance to all but the most stellar of heat sources."), 
    WeaponItem("bytes:uncertainty_mines","Uncertainty Mines","These mines latch onto mechas sabotaging their control and stability."),
    BackItem("bytes:antimass_stabilizer","Antimass Stabilizer","This component allows the effects of gravity to be ignored for short period of time.", stars=4),
    WeaponItem("bytes:hard_light_harvest_claw","Hard Light Harvest Claw","This massive melee weapon has blades made of hard light capable of shredding any armor.", stars=5),
]
)

thecowofeternalflame = Mech("thecowofeternalflame", 
[
    PowerItem("thecowofeternalflame:fusion_core","Fusion core","High energy production at the expense of high heat output and a tendency to destabilize if shot directly."),
    LegsItem("thecowofeternalflame:spider_legs","Spider Legs", "Four spider-like legs that can be used to climb vertical surfaces."),
    BodyPlanItem("thecowofeternalflame:drone_body","Integrated Drone Port","A bulky drone bay that opens in the middle of the body. Allows for an extra drone-specific weapon or kit.", {"weapon": 3, "kit":2}),
    CockpitItem("thecowofeternalflame:drone_controls","Drone Controls","A dedicated drone control panel for finer control of deployed drones.", stars=2),
    BackItem("thecowofeternalflame:back_mounted_radio","Back-Mounted Radio", "Large radio pack with long antennae coming up from it, for sending and receiving signals from the drones as well as for long-range communication with teammates"),
    KitItem("thecowofeternalflame:targeting_system","Long-range laser targeting system", "Helps to guide missiles to hit targets, whether from salvos, drones or allies.", stars=2),
    CosmeticItem("thecowofeternalflame:lightning_decal","Lightning Decal","A lightning decal, thematically appropriate to put on a targeting system."),
    BodyItem("thecowofeternalflame:swivel_pivot","Swivel Pivot","A sturdy torso that sits on a 360° swivel mount for maximum weapon coverage."),
    BodyPlanItem("thecowofeternalflame:drone-factory","Drone Factory", "The mech has a drone bay, within which is an automated drone factory that can slowly produce new drones. This slows the mech down due to the bulk. This allows the mech to equip four additional drone-specific weapon and/or kit parts. The bay can hold eight drones in it at any one time during battle.", {"weapon": 6, "kit":5}, stars=4),
    WeaponItem("thecowofeternalflame:error_unknown_name","Long-Range Railgun","This railgun has a huge range, but is slow firing with a long reload.", stars=2),
    KitItem("thecowofeternalflame:light_armor","Light Armor", "This armor weighs lighter than most to compensate for heavy weapons. It increases speed at the cost of making it vulnerable to smaller, faster flanking mechs", stars=2),
    WeaponItem("thecowofeternalflame:drone_medium","Medium Gunner Drone","A medium-range flying gunner-drone equipped with a HMG;", stars=3),
    WeaponItem("thecowofeternalflame:drone_long","Long Artillery Drone","A long-range artillery drone that can fire missile salvos. It moves via tank treads.", stars=3),
    WeaponItem("thecowofeternalflame:drone_fast","Fast Spider Drone","A fast moving drone that is effectively an oversized spider mine.", stars=3),
    KitItem("thecowofeternalflame:drone_radar","Radar Scout Drone","A fast moving flying scout drone equipped with radar tech.", stars=2),
    BackItem("thecowofeternalflame:five_star_back_radio","Multiplexed Communications Radio","Large radio pack with long antennae coming up from it, for sending and receiving signals from the drones as well as for long-range communication with teammates. This version allows all allies to loop into eachother's camera feeds in real-time, as well as any drone feeds on the field.", stars=5),
    ArmsItem("thecowofeternalflame:cracker_jacks","Cracker Jacks","A pair of spindly arms with retractable tools in the fingertips that allows the mech to interface directly with electronics. This includes other mechs, provided you can get them to stay still long enough that is.", stars=3),
    ArmsItem("thecowofeternalflame:trojan_arms","Trojan Arms","Like the Trojan Horse, these arms aren't all they appear to be. Each arm holds a swarm of nanodrones within that can be released through a hatch to attack and hamper your opponent independant of you.", stars=4),
    CockpitItem("thecowofeternalflame:drone_keychains","Drone Keychains","A set of keychains hanging from the ceiling by the windshield with replicas of the types of drones the mech produces.", stars=5)
]
)

shork = Mech("shork", 
[
    PowerItem("shork:lithium_polymer_battery","Lithium Polymer Battery","Harnesses the incredible power of magic smoke. Don't let it escape!", stars=1),
    ArmsItem("shork:wowot_arms","Wowot Arms","A highwy awticuwated, cwane-wike set of awms, ending in gwabbing jaws. Pewfect fow gwappwing uwu", stars=2),
    ArmsItem("shork:diabolical_grippers","Diabolical Grippers","Hydraulic industrial claws, paired with articulated wrist-mounted sawblades, built to cut through whatever you've latched onto. Slice into weakly armored opponents, or throw some sparks off of tougher foes for style points.",stars=4),
    LegsItem("shork:c5_drive","C5 Drive","A wheeled drive system, powered by a set of motors scavenged from an ahead-of-its-time electric bike.", stars=1),
    LegsItem("shork:mecanum_drive","Mecanum Drive","Wheels with built-in rollers, designed for omnidirectional movement. With the right setup, you can smoothly drift around your opponents, whilst facing any direction you want.", stars=4),
    BodyItem("shork:hedgehog_armor","Hedgehog Armor","Covering your bot in nails, spikes-out, is certainly *a* defensive option.", stars=1),
    BodyItem("shork:scrapyard_special","The Scrapyard Special","A chassis fully constructed from a few hundred bob worth of scrapmetal. The front is encased in old traffic signs. ROAD AHEAD CLOSED, it says.", stars=2),
    BodyItem("shork:billet_chassis","Billet Chassis","A solid block of aluminium carved into a chassis. Nigh indestructible, but tough to repair.", stars=3),
    CockpitItem("shork:remote_control_unit","Remote Control Unit","Battle at a safe distance from the carnage. Comes with a choice of RC remote styles to use.", stars=1),
    BackItem("shork:apd_unit","APD Unit","An array of scaffolding designed to keep dangerous foes out of reach. Also handy if you get stuck in a hole.", stars=1),
    BackItem("shork:shame_cube","Shame Cube","A massive dumpster bolted to the back of your bot, capable of trapping any mech caught within it. It's positioned so a suplex will dump your target right into it!", stars=4),
    BackItem("shork:full_body_spinner","Full Body Spinner","A giant blade of metal orbiting your mech at ungodly speeds, fuelled by the biggest ICE we could strap on its back. Kinetic energy in its purest form, putting a deadly wall between your opponent and your chassis.", stars=5),
    WeaponItem("shork:pulveriser","Pulveriser","A hefty metal mallet, powered by a pneumatic system to give it an extra kick. Not ideal for external damage, but excellent at shaking up internals.", stars=1),
    WeaponItem("shork:thwacker","Thwacker","A weighty cudgel on a flexible arm, bolted onto an extremity. Powered by your drivetrain, thrash about to strike anyone that comes close.", stars=2),
    WeaponItem("shork:flippaaaaaaaaah","FLIPPAAAAAAAAAH","A reinforced pneumatic panel built into the chassis or limb of your mech. Can be fired to knock foes away, or kept up as a surprise shield. Also useful for self-righting.", ["kit"], stars=2),
    WeaponItem("shork:spinnaaaaaaaaah","SPINNAAAAAAAAAH","A big hunk of metal spinning at ungodly speeds. Kinetic energy in its purest form.", stars=3),
    WeaponItem("shork:mangler","The Mangler","A high-speed chain flail with a wide attacking radius. Although the blades struggle against armour, the sheer volume of strikes mean that it's effective at catching on exposed machinery in joints and gaps.",stars=2),
    WeaponItem("shork:kinetic_puncher","Kinetic Puncher","A compact S7 tool steel drum on a sliding rack, attached to the forearm. Passively charges with kinetic energy, before it can be deployed to add some extra kick to a strike.",stars=3),
    WeaponItem("shork:massive_claw_unit","Massive Claw Unit","Nine gigatons of crushability factor!", stars=3),
    WeaponItem("shork:roborat_drones","Robo-Rat Drones","Deploy a swarm of robotic rats, armed with saws and flamethrowers. Effective at cutting through armour and torching insides, but can be disarmed by toppling them on their backs.", stars=3),
    WeaponItem("shork:d2_kitbot_drone","D2 Kitbot Drone","An incredibly effective drone unit, but is it really your victory if you didn't build it yourself...?", stars=4),
    WeaponItem("shork:drop_zone","Drop Zone","A high-altitude drone attempts to drop junk on the battlefield. Avoid the X it projects on the ground, unless you want to get slammed by washing machines, bowling balls, TVs, scrapped mech parts...",stars=4),
    WeaponItem("shork:lithium_polymer_armament","Lithium Polymer Armament","Harnesses the incredible power of magic smoke. Don't let it escape! This unusual config directly weaponizes the battery unit. If this gets hit, the fight's ending one way or another.",["power"], stars=5),
    BodyPlanItem("shork:snowplow","Snowplow","A defensive profile that's low to the ground, with four legs, no arms, and a tanky, ground-scraping wedge protecting your weaponry. Nothing's getting under you any time soon, if you're using the right sort of locomotion.", {"legs": 4, "arms": 0}, stars=1),
    BodyPlanItem("shork:ring","Ring","A defensive, invertible design, with weapons built into a ring orbiting around your chassis. The best defense is a perfect offense.", {"legs": 4, "arms": 2}, stars=3),
    BodyPlanItem("shork:clusterbot","Clusterbot","Two matching, half-sized, half-power chassis, attached together magnetically. Able to split apart and recombine, but if either half is offlined, it takes the other down with it. The body, limbs and power source are duplicated for each half, but all other parts must be assigned to one or the other.", {"legs": 2, "arms": 2}, stars=5),
    KitItem("shork:selfdestruct_button","Self-Destruct Button","When all else fails, this button can ensure you take your opponent down with you. It actually just deploys a bunch of smoke and pyrotechnics, but it's good for making threats with.", stars=2),
    KitItem("shork:meltybrain_unit","MeltyBrain Unit","A program that micro-adjusts drive motors, allowing for translational movement whilst the entire mech spins at high speed. This lets you put the entire mech's weight and speed behind a spin attack whilst remaining aggressive.", stars=3),
    CosmeticItem("shork:rival_poster","Rival Poster","A life-size poster of your opponent's mech, stolen from their merch line and pasted onto the front of your mech. Useful as a confusion tactic.",stars=1),
    CosmeticItem("shork:polkadot_fur","Polkadot Fur","Incredibly flammable. Offers no tactical advantage whatsoever. Mechs that fight against one equipped with the fur seem to end up with some fur of their own in future fights, strangely.", stars=2),
    
]
)

p_rker = Mech("p_rker", 
[
    PowerItem("p_rker:psionic_engine","Psionic engine","This device syncs with the user's brainwaves to create a potent motive force.", stars=3),
    LegsItem("p_rker:heelies","Heelies","These digitigrade pistons have wheels on the bottom to enhance mobility and coolness.", stars=2),
    ArmsItem("p_rker:biomechanical_arms","Biomechanical arms","Artificial muscles made from bizzare tensile alloys.", stars=2),
    BodyItem("p_rker:crash_resistant_body","Crash-Resistant Body","A sturdy roll cage suspends its cockpit with tense metal springs."),
    CockpitItem("p_rker:egg_pod","Egg-shaped Pod","An egg-shaped pod that encases the pilot in protective fluids.", stars=2),
    BackItem("p_rker:sensor_suite","Sensor suite","A number of sensors measure various atmospheric conditions, reporting to base with a giant radio antenna"),
    WeaponItem("p_rker:stop_sign","Stop Sign","Slow without stopping at your own peril!"),
    CosmeticItem("p_rker:caution_stripes","Caution stripes","Black and yellow paint warns away from the mech's most sensitive - and dangerous - joints"),
    BodyPlanItem("p_rker:train_body","Train Body","We strapped arms on this train and called it a mecha!", {"legs":0,"arms":3}, stars=3),
    WeaponItem("p_rker:weapon","Steel Claws","These bestial claws menace with spikes of iron."),
    KitItem("p_rker:climbing_equipment","Climbing equipment","The pitons and steel rope strapped to this mech let it scale sheer cliffs."),
    KitItem("p_rker:helicoper_blades","Helicoper blades","You know what helicopters are like.",["back","weapon"]), 
    CosmeticItem("p_rker:cosmetic","Fur","This mech appears to have fur growing on it.  Are they simply cosmetic synthetics, or has science finally gone far enough?", stars=4),
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
    BackItem("only:flame_wheel","Flame Wheel","A large ring of fire blazes above your mech's back.", stars=4),
    WeaponItem("only:concussive_knuckles","Concussive Knuckles","Massive blocky fists that generate additional concussive force on contact, letting you amp up your impact", stars=1),
    CosmeticItem("only:energy_vein_system","Energy Vein system","A network of glowing lines cover your mech, showing how power flows through its system and flaring up when energy levels spike", ["cosmetic"], stars=1),
    BodyPlanItem("only:asura","Asura","A blueprint from Only with a fearsome design - 2 Legs, 6 arms", {"legs":2,"arms":6}, stars=3),
    BodyPlanItem("only:arbitor","Arbitor","A blueprint from Only with a powerful design - 2 legs and 4 arms that hover separate from the body",{"legs":2,"arms":4}, stars=4),
    BackItem("only:mirage_system","Mirage System","Allows the equipped mech to become intangible for a short period. Getting hit? Just dont get hit lol", stars=3),
    BackItem("only:wingblades","Wingblades","These angular constructs hover just above your mech's back, able to both generate lift for your mech and swing around for offensive maneuvers", stars=4),
    CosmeticItem("only:sick_ass_jacket","Sick Ass Jacket","Your mech is covered by an incredibly cool jacket, the fabric of which reduces the damage of energy weaponry", stars=1),
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
    BackItem("ditto:giant_wind","Giant wind-up key","Playing with toys.", ["cosmetic"], stars=2),
    WeaponItem("ditto:comically_large_spoon","Comically Large Spoon","Perfect for ice cream!", stars=3),
    CosmeticItem("ditto:cool_hat","Cool hat","It's a really cool hat", stars=4),
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
    PowerItem("hal2000:the_beating_hearts_of_one","The Beating Hearts of One Thousand Worms","The heartbeats of these still-live worms are amplified and converted into electrical energy for the mech to use. They yearn for the sweet taste of the earth, and will give your mech a power boost to its weapon systems relative to how close your mech is to dirt.", stars=4),
    PowerItem("hal2000:cote_blue_flame","Cot3's Blue-Flame Generator","A powerful generator that uses a special blue flame to supercharge the mech, but leads to an odd kind of smoke build-up on the inside that cannot be ventilated normally.", stars=2),
    LegsItem("hal2000:dimensionally","Dimensionally Disjointed Walkers","These standard-issue mech legs have been dimensionally modified so that every joint below the hip is connected but stored in an alternate dimension. Makes you hard to hit below the waist."),
    LegsItem("hal2000:kelvin_drumset","Kelvin's Mechanical Drumset","A reproduction of Kelvin's drumset/spider leg set-up, properly sized for usage as a set of mech legs!", stars=2),
    ArmsItem("hal2000:cobbled_scrap_arms","Glistening Ichor Infectors","After much use, an odd oil is dripping out of these Glistening Platinum Punchers. They’re still durable and lithe, but any enemy mech that touches the ichor will find their computer systems slowly corrupted and the mech’s operating fluid infected by ichor. Maybe these were scrapped for a reason...", stars=4),
    ArmsItem("hal2000:jaw_claws","Jaw-Claws","A pair of thick and heavy arms with giant mechanical mouths on the end. These mouths can be used to hold stuff, and can also be fired on a chain to grapple from afar!", stars=3),
    BodyItem("hal2000:orb","ORB","SPHERE SPHERE SPHERE SPHERE SPHERE, ALL PRAISE."),
    BodyItem("hal2000:house","House","It's well furnished on the inside, and moderately sized for a family of 4. It has 2 bedrooms and 2 bathrooms, and even has a porch if you like to sit outside and watch the neighborhood."),
    CockpitItem("hal2000:divesystem","Full-Body Dive System","Really FEEL like you're dying to that rocket. This system makes controlling your mech fluid and effortless, allowing you to pull off stylish moves with ease... but you also feel all the damage the mech takes."),
    CockpitItem("hal2000:early_alert_system","Early Alert System", "Equips your mech with a series of external sensors that are wired up to the cockpit. Whenever these sensors detect offensive action, they’ll send that information over, and if you’re watching for the warning you'll gain you more time to dodge.", stars=2),
    CockpitItem("hal2000:ratoon_plushie","Ratoon Plushie","A life-sized plush of everyone's favorite mouse mechanic and the perfect co-pilot. They do not know when this was made, but it sure is cute!", stars=2),
    BackItem("hal2000:backlift","Backlift","A pair of forks on the back for lifting cargo, only usable if you're Forklift Certified!"),
    BackItem("hal2000:realistic_moth_wings","Realistic Moth Wings","They look so true-to-life and work too! Fragile but nimble, these insectoid wings will get you where you need to go and fast!", stars=2),
    BackItem("hal2000:realistic_angel_wings","Realistic Angel Wings","They look so true-to-life and work too! They're so realistic in fact, that one would think they were taken from an actual angel... hey wait a sec-", stars=4),
    WeaponItem("hal2000:guminator_3000","Etheric Condenser","A gun that shoots a special kind of etheric matter. In addition to doing damage, strange crystal growths will appear where the enemy mech is hit, gumming up joints or corrupting electrical systems they come in contact with", stars=3),
    WeaponItem("hal2000:the_blattilizer","The Blattilizer","A very special baseball bat for a very special person. Swing for the fences!", stars=3),
    WeaponItem("hal2000:monologue_piercer","Monologue Piercer","A spear made of captured language, solidified into usable form. Deals extra damage to opponents who are talking, and breaks through any protections they may have.", stars=3),
    CosmeticItem("hal2000:blender_head","Blender Head","Your mech has an oversized blender as a head. That is all. It is very cool-looking but impractical for actual combat.", stars=2),
    CosmeticItem("hal2000:bouncy_blorbo","Bouncy Blorbo","A little blorbo made from some kind of goo, potentially industrial waste. It has somehow come alive, and very much wants to be as close to you as possible.", stars=2),
    KitItem("hal2000:clown_face","Clown Face Paint","A crude imitation of joy, warped beyond recognition into a face that can only terrify. Enemies who stare into the visage for too long may find it staring back, leaving them stunned and unable to move. Honk.", ["cosmetic"], stars=3),
    KitItem("hal2000:zirconium_pants","Zirconium Pants","These fancy pants are actually an alien information blocking tool, and once per fight you can use them to replace all nouns with \"pants\" and all adjectives with \"zirconium\" in the next turn post as reality is obfuscated. Actions will take place normally, but neither fighter will know the outcome.", ["cosmetic"], stars=3),
    KitItem("hal2000:the_bagel","The Bagel", "This small ring can be thrown and then sized up, creating a miniature black hole inside of it that draws everything on the battlefield closer to it over time. Getting sucked in may lead to an existential crisis and/or death.", stars=4),
    KitItem("hal2000:glutton","Glutton","They say you are what you eat, and that's true! Gives your mech a giant mouth and working system of stomachs. Your mech can additionally gain any part it eats off the enemy mech, congealing a replica of flesh and bone as it finishes digesting the part.", stars=4),
    KitItem("hal2000:credits_roll", "Credits Roll", "Adds a button to your cockpit that, when pressed, plays an unskippable credits roll across all the screens in your opponent's cockpit detailing all the people in your life. Exceedingly annoying and only usable once per fight."),
    BodyPlanItem("hal2000:crawler","Crawler","8 arms. No legs. Become a monstrosity of mechanical engineering.", {"arms":8, "legs":0}, stars=4),
    BodyPlanItem("hal2000:apartment","Apartment","A mech? In this economy?? Just remove the arms and legs, I'd rather have a place to live.", {"arms":0, "legs":0}),
    BodyItem("hal2000:orbascended","ORB ENLIGHTENED","SPHERE, ASCENDED FORM, ALL-KNOWING, ALL-SEEING, CLEAR AND PERFECT, NONE CAN ESCAPE ITS SIGHT, GRANTS VISIONS OF THE FUTURE.", stars=5),
    PowerItem("hal2000:cote_true_blue_flame","Cot3's Blue-Flame Generator","A powerful generator that uses a special blue flame to supercharge the mech, but leads to an odd kind of smoke build-up on the inside. It has been upgraded with a special mechanism for rapidly expelling this smoke and creating a smokescreen as needed.", stars=5),
    PowerItem("hal2000:limit_breaker","Limit Breaker","This dense metal core serves as your mech’s power source, pumping raw energy through its systems. As your mech takes damage, a gauge on it fills, and once full it will break your limits, sending a shock that refreshes all items on cooldown and grants an additional use to all one-time use items.", stars=5),
    WeaponItem("hal2000:gunis", "GunIsGunIsGunIsGunIsGunIsGun", "A cruel, warped reflection of weaponry that spits on the definition of a gun. This orb of pure violence breaks causality itself to shoot your opponent at point blank with incredible force no matter the actual range. Can only be used once per fight before collapsing in on itself.", stars=5),
]
)

turtlelover2244 = Mech("turtlelover2244", 
[
    PowerItem("turtlelover2244:hype_core","Hype Core","A Generator connected to an online video stream. The more hyped the audience, the more power the core generates."),
    LegsItem("turtlelover2244:hover_boots","Hover Boots","A set of overly fancy legs equipped with hover technology, letting the mech deftly float a few inches off the floor."),
    ArmsItem("turtlelover2244:puppet_hands","Puppet Hands","Hands that freely float around your mech. Excellent for offense, not so much for defense."),
    BodyItem("turtlelover2244:subspace_generator","Subspace Generator","A Small and Sleek Body that uses pocket dimensions to store equipment when not in use."),
    CockpitItem("turtlelover2244:streaming_setup","Streaming Setup","A Mic, Camera, and Several monitors showing your streams statistics and chat, along with mildly useful mech information."),
    BackItem("turtlelover2244:holocape","Holo-Cape","A Large and permanently flowing cape made of Hard-light. Most conventional weapons cannot pierce it."),
    WeaponItem("turtlelover2244:arcane_staff","Arcane Staff","A Polearm covered in glowing Runes, Although it holds no substantial magic power. The tip can fire a laser beam, if that’s any compensation."),
    CosmeticItem("turtlelover2244:gamer_leds","Gamer LEDs","Anything is improved by adding rainbow lights to it."),
    BodyPlanItem("turtlelover2244:magician","Magician","4 Arms, 2 Legs, 2 Power Sources. A Blueprint Designed to use many weapons at once, Two Power cells are needed to run at full capacity.", {"arms":4,"legs":2,"power":2}),
    CosmeticItem("turtlelover2244:tophat","Top Hat","A mundane, but fancy hat."),
    WeaponItem("turtlelover2244:shuffler","The Shuffler","A gun that launches steel sided player cards at a rapid pace."),
    BackItem("turtlelover2244:interstitial_engine","Interstitial Engine","A mysterious device that can pierce through gaps in reality, letting you teleport a short distance."),
    CosmeticItem("turtlelover2244:roboduplicate","Robo-Duplicate","A robotic duplicate of yourself riding on the top of your mech."),
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
    BackItem("zweihawke:necrolite_tether","Necrolite Tether","Bound to the harvest of long fractured and dead souls, this contact point drains life. A desperate pilot need only stick their hand in for a few more hours of battery..."),
    WeaponItem("zweihawke:quantum_box","Quantum Box","Much like what you're doing right now, whatever's inside exists in a quantum state of superposition until it is opened and observed. I hope it's circus peanuts."),
    CosmeticItem("zweihawke:electroplated_gold","Electroplated Gold","Some say divinity is only for the rich. Those people are fools."),

    BodyPlanItem("zweihawke:modeswapper","Mode-Swapper","Has only one set of legs active at a time and can swap between them at will.", {"legs":4,"arms":2}),
    PowerItem("zweihawke:luck_engine","Luck Engine","So long as it stays in good repair, good things happen to you. Bad things happen to those who oppose you."),
    PowerItem("zweihawke:invocation_engine","Invocation Engine","So long as you know the right word, you can bend even reality to your will. However, you should be careful what you speak. This isn't something to be toyed with."),
    KitItem("zweihawke:network_bound","Network Bound","This mech can be wirelessly powered, operated, and repaired so long as a network point of your ownership exists within the mech's listening range."),
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
    BackItem("colabot:cool_backpack","COOL BACKPACK","You can store anything in here! A bonus weapon or tool, maybe, but also, an extra sweater, some snacks, a spare power pack, a comfort item, some fidget toys… The possibilities are endless when you have a Cool Backpack!", stars = 2),
    WeaponItem("colabot:yoyo","Yo-Yo","Okay, so have you seen, um, have you seen Miraculous Ladybug? No? Oh, okay. So it’s a yo-yo, but it’s a weapon, right? And you can like, swing it around, and hit things with it, and also use it to swing like Spider-Man - I’ll send you a video. It’s pretty cool!", stars = 3),
    CosmeticItem("colabot:holographic_stickers","Holographic Stickers","Your mech is absolutely covered in cool holographic stickers. This doesn’t help with stealth, you’re now EXTREMELY visible, but maybe you could blind your opponent in a bright sunny arena? They’ve all got different designs, and most of them came from the artist alley at a con somewhere."),
    # vetoed. too hard to someday implement and way too long of a description.
    # BodyPlanItem("colabot:split","Split","Your mech can split into up to four smaller mechs, each equipped with parts taken from your larger mech. This can be super useful for distracting or flanking your opponent! You can choose to split into two, three or even four smaller units (“mini-mechs”), but the more times you split, the fewer useful parts you have to go around. You can equip up to three extra pairs of legs that will be used by your mini-mechs, but this blueprint won’t allow you to use them on your standard large unit. You cannot equip extra arms or weapons for your mini-mechs to use, unless other attributes you have allow this.", {"legs":3}),
    BackItem("colabot:jetpack!","JETPACK!","You can perform a very high jetpack-assisted leap, save yourself from a fall, or speed up your travel on the ground - unfortunately, you can’t use it to fly, though, because your mech is too heavy. Plus, the fuel is kinda hard to come by."),
    ArmsItem("colabot:grappling_trex_arms","Teeny T-Rex Grappling Arms","Your enemy scoffs at your tiny, useless arms. Little do they know, these bad boys are GRAPPLING HOOKS!!! They can shoot out at high velocity, ready to grab and yank anything without warning - you can even use them to entangle the limbs of your opponent’s mech, disabling their movement.", stars=5),
    CockpitItem("colabot:plushies","Pile o' Plushies","A large pile of stuffed animals of various sizes. They’re excellent moral support, and can be napped on in a pinch.", stars=2),
    CockpitItem("colabot:scale_model","Scale Model","A very cool miniature scale model of your mech, displayed on your dashboard. It has realistic texturing and led lighting elements, and it articulates in all the same ways as your real mech. The company that makes it has sponsored you, and will send you a miniature version of any new parts you equip.", ["cosmetic"], stars=2),
    CosmeticItem("colabot:sailor_suit","Little Guy Sailor Suit","A full outfit for your mech, which includes a shirt with a sailor collar and bow tie, a little sailor hat, and a pair of shorts with shiny brass buttons. It comes in a fetching sky-blue colour."),
    WeaponItem("colabot:thagomizer","Thagomizer","A long, powerful, heavily armoured tail ending in an arrangement of spikes that can cause significant damage to enemy mecha. This weapon conveniently leaves the mech’s hands free to grapple or hold other items.", stars=3),
    CosmeticItem("colabot:lolita","OTT Sweet Lolita Coordinate","A full outfit for your mech, including an extreme amount of frills, layered petticoats, and accessories - this particular outfit is strawberry themed! Your mech is wearing cute bracelets and frilly lace wrist cuffs, an oversized bow or bonnet, and carrying a cute strawberry shaped bag.", stars=4),
    BodyPlanItem("colabot:tail_prehensile","Prehensile Tail","Your mech has a highly flexible tail that can be used to improve mobility or to equip one extra short range weapon.", {"weapon":2}),
    BodyPlanItem("colabot:tall","Tall","Your mech is very tall, but all the height comes from its torso - you can equip an extra back slot item. It can be hard to keep track of your legs though… they’re an awfully long way down.", {"back":2}, stars=2),
    LegsItem("colabot:paaaaaws","Paaaaaws","You got some freakin paaaws, dude! They got cute liddle toe beans, and retractible claws!", stars=2),
    PowerItem("colabot:spell","**The Spell**","The deepest, most secret chamber of your mech is suffused with a sickening octarine glow. **The Spell** is etched into the very fabric of existence. It is unspeakably ancient; your mech was constructed around it in a desperate attempt to channel its energy into something less hazardous to life.",stars=4),
    WeaponItem("colabot:spellbook","The Spellbook","A hazardous spellbook containing multivarious methods of arcane combat. FIREBALL! Be careful, pilot; the overeager caster can lose themselves to the rush of power, and some spells backfire...", ["cockpit"], stars=4),
]
)

loftyinclination = Mech("loftyinclination", 
[
    PowerItem("loftyinclination:automated_wiring_harness","Automated Wiring Harness","Attaches to nearby power sources, conduits, and power consuming devices, and syphons energy for use in its own system."),
    LegsItem("loftyinclination:outsideskates","Outside-the-line Skates","Wheels, externally mounted to featureless tapered legs. Allows for speedy travel and conservation of momentum!"),
    ArmsItem("loftyinclination:telekinetic_sash","Tele-kinetic sash","Through the use of the 5th fundamental force, this smart-fabric can manipulate objects without direct contact.", stars=3),
    BodyItem("loftyinclination:gardens_brush","Garden's Brush","Though the underlying form of this body has smooth panel lines, at some points the panels are misaligned, allowing soft fur to poke out from inside."),
    CockpitItem("loftyinclination:cats_eye","Cats Eye","The front surface of the pilot cockpit contains mirrored windows, in the shape of slit eyes. Combined with the internal heads up display, allows for better detection of movement."),
    BackItem("loftyinclination:disjoint_wings","Disjoint wings","Some body panels can detach and act as wings, allowing for gliding on thermals."),
    KitItem("loftyinclination:oscilloscope_probes","Oscilloscope Probes","These long staff-like tools trail low-impedence cables, hooked into your mech's sensor suite, able to divine the potential weaknesses of your opponent's form"),
    WeaponItem("loftyinclination:modified_oscilloscope_probes","Modified Oscilloscope Probes","The OEM listing for these identifies them as \"sensor accessories\". That's clearly not true any more -- modifications by a previous owner mean that anyone jabbed with the sharpened tip of these spears receives an extreme electric pulse.", stars=4),
    CosmeticItem("loftyinclination:constellation_tattoos","Inlaid Constellation Tattoos","Traced out on your mech's shell in softly glowing silver are the constellations of a planet far away, unknown to you, but that somehow fill you with a great sadness."),
    BodyPlanItem("loftyinclination:catform","Catform","Quadrapedal, for increased stealth and pouncing.", {"legs":4}),
    PowerItem("loftyinclination:fivestar_automated_wiring_harness","Automated Wiring Harness","Attaches to nearby power sources, conduits, and power consuming devices, and siphons energy for use in its own system. Can even draw power from another mechanised unit, impacting the other mech's capabilities.", stars=5),
    WeaponItem("loftyinclination:ble_spec","Bluetooth Core Specification, v6","This hefty spellbook contains detailed instructions and guidelines for remote communication, which may give you a leg up in electronic warfare. It's also over three thousand pages, so you could also just hit people with it", stars=2),
    CockpitItem("loftyinclination:workbench","Lorentz Workspace","Stored in a pocket dimension, this workspace allows for on the fly reconfiguration, reverse engineering, or just hanging out and relaxing", stars=3),
    KitItem("loftyinclination:ladder","Ladder","After countless hours toiling away, scientists have finally unlocked deep enough into the tech tree to invent ladders! Surprisingly difficult to get right, even after they'd already mastered dimensional engineering and stellar manipulation...", stars=4),
    PowerItem("loftyinclination:ancillary","Ancillary System: Seaglass","If ever your pilot were to be rendered a non-functional part of the mech, this unit ensures that your mech would be able to continue the soiree; a backup of an earlier pilot lives inside your mech, tuning the systems, and sometimes able to operate them", stars=3),
    ArmsItem("loftyinclination:gantry","Polar Gantry","Two gantries span your mech, capable of accellerating at up to 180000m/s, perfectly suited to speedily maneouvering the sensor suite and manipulators of your mech around your form. However, they don't have much reach...", ["weapon"], stars=2),
]
)

shade = Mech("shade", 
[
    PowerItem("shade:chronomantic_core","Chronomantic Core","A Spherical device made of spinning 3D gears inscribed with with runes. The materials of the gears appear to be brand new when in contact with each other, and rusting to dust when not."),
    LegsItem("shade:fractal_legs","Fractal Legs","Just SO MANY LEGS, Insectile spikes that split into infinities to grasp even the smallest protrusions.", stars=3),
    ArmsItem("shade:hexagonal_hands","Hexagonal Hands","Metallic graspers with 6 Digits on the end, positioned in a hexagonal pattern."),
    BodyItem("shade:crystalline_bathysphere","Crystalline Bathysphere","A Large dodecahedral cockpit made out of a clear crystal material. The pilot is visible seated inside."),
    CockpitItem("shade:lucky_tesseracts","Lucky Tesseracts","A Pair of tesseracts suspended from the rear-view display by cosmic strings."),
    BackItem("shade:jump_jet_wings","Jump Jet Wings","A Pair of large robotic wings. Instead of feathers the span is comprised of jet engines evenly spaced."),
    WeaponItem("shade:harpoon_katars","Harpoon Katars","A matched pair of punching daggers capable of being \"fired\" off at range and retracted or manipulated by a length of chain."),
    CosmeticItem("shade:woad_enchantments","Woad Enchantments","Twisting spiral patterns of coruscating magical runes wrap around the mech, hovering just above every surface. They appear to shift and change over time."),
    KitItem("shade:spheroid_transport_form","Spheroid Transport Form","This mech is capable of rolling up into a ball in order to move quicker or minimize surface area."),
    ArmsItem("shade:5star_hexagonal_hands","Hexagonal Hands","Metallic graspers with 6 digits on the end, positioned in a hexagonal pattern. Now with built in phase cannons in the palms!", stars=5),
])

babaloga = Mech("babaloga", 
[
    PowerItem("babaloga:quasiquasar","Quasi-Quasar", "We don't know what it is but it puts out a shit ton of energy and it's not a Quasar."),
    LegsItem("babaloga:heavy_boots","Heavy Boots","Cartoonishly oversized boot-shaped feet"),
    ArmsItem("babaloga:pterosaur_claws","Pterosaur Claws","Large folded wings that can function as front legs. Not ideal for grasping or hitting, but capable of flight."),
    BodyItem("babaloga:shrouded","Shrouded","Layers of draped fabric, netting, and cables obscure the body underneath like a cloak."),
    CockpitItem("babaloga:too_many_eyes","Too Many Eyes","Eyes on the ceiling, eyes on the floor, eyes covering every surface."),
    BackItem("babaloga:deployable_guy","Deployable Guy™","A harness holding a featureless white capsule with a nametag floating over its head. A Guy™ is indestructible and can slide around. It is impossible to mount anything to the Guy™.", stars=2),
    WeaponItem("babaloga:miniglolfkit","Mini-Glolf Kit","A club and variously colored glolf balls from a local mini-glolf place that closed down. For some reason the balls are packed with explosives and can be remotely detonated?"),
    CosmeticItem("babaloga:name_tag","Name Tag","Semi-transparent black rectangle that floats over your mech's head and displays its name."),
    BodyPlanItem("babaloga:airship","Airship","No arms, no legs, just a giant balloon with 3 weapons mounted to it.", {"weapon": 3, "legs":0, "arms":0}),
    PowerItem("babaloga:beans","\"Beans\"","\"Beans\" will be launched into the general vicinity. You gotta keep picking them up to stay powered.", stars=2),
    CosmeticItem("babaloga:polygonal_crown","Polygonal Crown","A big matte yellow crown that sits lopsided.", stars=2),
    CosmeticItem("babaloga:double_crown","Double Crown of the Double Winner","A matte yellow crown with a matte brown crown inside it. Both sit lopsided at different angles.", stars=4),
    CosmeticItem("babaloga:f_holes","F Holes","Openings resembling the sound holes on violin-family instruments."),
    BackItem("babaloga:deployable_guy_with_dodgeball","Deployable Guy™ With Dodgeball","A harness holding a featureless white capsule with a nametag floating over its head. A Guy™ is indestructible and can slide around. It is impossible to mount anything to the Guy™. It's holding a dodgeball, which it can throw at stuff.", stars=5),
    #New Items:
    BodyItem("babaloga:apparatus","Apparatus","A formless mess of ducts, belts, tubing, and wires. Completely unshielded and unmanaged."),
    CockpitItem("babaloga:corndog_dispenser","Corndog Dispenser","An infinite supply of corndogs from a factory somewhere deep in the mech."),
    BackItem("babaloga:disciple_of_denny","Disciple of Denny","A cube-shaped robotic artist. The Disciple can be sent to deploy pancake spirals across the battlefield. You can probably mix other things into the pancake batter...", stars=2),
    PowerItem("babaloga:unprotected_fission_reactor","Unprotected Fission Reactor", "It's probably fine. What's the worst that could happen?"),
    BodyItem("babaloga:towering_spire","Towering Spire","In place of a head, the mech's body is extends upward into a tower-like protrusion. The spire does not articulate like a head or neck.", stars = 3),
]
)

theoddman = Mech("theoddman", 
[
    PowerItem("theoddman:roz_fusion_generator","ROZ Fusion Generator","Old and a little hefty for its size, this steel-cased reactor was once one of the best on the market, still is.",stars=3),
    LegsItem("theoddman:unified_field_enhanced","Unified Field Enhanced","Two sleek legs with built-in thrusters, enhanced by gravity manipulation to allow them to leap and boost further.",stars=2),
    ArmsItem("theoddman:gravity_gauntlet","Gravity Gauntlet","The hands of the mech utilize local gravity manipulation to assist in manipulation, and can activate magnets to guarantee a firm grip.",stars=1),
    BodyItem("theoddman:crz1_n41da","CRZ1-N41DA","Features two small central point defense lasers. A reasonably armored core that protects the pilot rather well. It has strong, sleek lines when viewed from the front, the back being somewhat blocky, but a good place to mount thrusters.",stars=4),
    CockpitItem("theoddman:crest_factory_new","Crest Factory New","Equipped with a direct neural link, the cockpit is cushioned but otherwise spartan. Sometimes you hear a mercenary on comms exclaim that they don't want to be babysitting some new guy. You don't see them anywhere and you're probably doing a lot more than them anyway.",stars=1),
    CosmeticItem("theoddman:oob_rival","Out-of-bounds Rival","They're getting to grips with the controls and are having problems turning and are getting stuck on terrain. They are being rather theatric about what's going on, but they can't seem to find the path and participate. They will probably fight you after trying to help, but you aren't sure.",stars=2),
    WeaponItem("theoddman:16ergh_python","16ERGH-PYTHON","A lightweight, hand-held, 3 rail particle rifle. Takes a second to charge, but hits hard for its weight.",stars=4),
    CosmeticItem("theoddman:teleporting_bowmeow","Teleporting Bowmeow","A teleporting alien cat dog that you cannot get to just stay at home no matter how hard you try. They will keep themself safe but will cuddle you when they feel like it.",stars=4),
    WeaponItem("theoddman:wpu_lamia","KWG-ORBIT","A weapon that uses gravity and powerful electromagnets to accelerate it's projectiles in a circular chamber before firing out the front. Wants good mounts to keep steady. You can set it up to fire a wide variety of things.",stars=3),
    BackItem("theoddman:rt05_pegasus","RT05-PEGASUS","Auxiliary back mounted thrusters that provide a lot of thrust, but are hard to control.",stars=2),
    WeaponItem("theoddman:as_gz03","AS-GZ03","An energy shield that uses an artificial gravity field to enhance protection, and houses two laser sword emitters on its end. It looks really cool, but has a high energy drain.",stars=1),
    PowerItem("theoddman:roz_prototype_n","ROZ Prototype N","Old and a little hefty for its size, this steel-cased reactor was once one of the best on the market and still is. This one has been given a lightened casing and been fitted with something old that no one has quite seen before; it runs hot but stably outputs an almost concerning amount of energy.",stars=5),
])



chillychilichelle = Mech("chillychilichelle", 
[
    LegsItem("chillychilichelle:pike_walkers","Pike Walkers","A set of 4 tall, spindly, spiked manufacturing actuators that protrude from the mech body and puncture into the ground. They move 2 at a time, retracting into themselves before plunging back into the floor.",stars=1),
    ArmsItem("chillychilichelle:talos_hands","Talos Hands","A pair of giant steel arms modeled after human anatomy. Covered in a soft fiberglass skin. Allows for precise articulation in the elbows and finger joints.",stars=1),
    WeaponItem("chillychilichelle:telephone_pole","Telephone Pole","A utility pole seemingly ripped straight from the ground. Live wires crackle, dangling from the arms. 2 transformers are still attached, while a third appears to have been broken off. Dirt still clings to its base.",stars=1),
    PowerItem("chillychilichelle:160000_aaa_batteries","160,000 AAA Batteries","A set of ~160,000 AAA batteries bound together with cable ties, hot glue, hope, and hubris. They are crudely affixed to a metal plate, where faded signatures and greetings are written on the back in marker.",stars=1),
    CockpitItem("chillychilichelle:a_rock","A Rock","A small greyish rock, roughly the size of your fist. Covered in a few brown and black specks. Totally unremarkable. You picked it up and placed it in your cockpit as a joke, but it's been 2 years and it's still here.",["cosmetic"],stars=1),
    CockpitItem("chillychilichelle:glass_closet","Glass Closet","A tall, plexiglass closet fixed to the ground. Everyone seems to be able to see through it just fine except you. The perfect place to store copious amounts of memorabilia of your rival.",["cosmetic"],stars=1),
    
    BodyItem("chillychilichelle:stripped_framework","Stripped Framework","The bare skeleton of a long-defunct mech. Composed of hollow steel tubes and dangling wires. Originally the leftovers from a salvage, it reaches only the barest minimum of what is considered a mech.",stars=2),
    CockpitItem("chillychilichelle:black_box","Black Box","A large steel cube, wrapped in a dozen layers of insulation and armor. Lacks any way to directly view the outside world. Contains up to 2 months of food, water, and oxygen. Requires the pilot to be hermetically sealed in each mission.",stars=2),
    Item("chillychilichelle:overgrowth","Overgrowth","Countless vines and leaves that have made the mech their home. Foliage blooms in the in-betweens of joints, and moss cakes every crack. Vibrant flowers dot the highest surfaces.",["cosmetic"],stars=2),
    KitItem("chillychilichelle:mechalogue","Mechalogue","A small portable computer encased in a hardened orange plastic. Attached to the front is an orb-shaped digital camera. Connected to an unspecified database, it is able to identify and provide information on any mech or mech part. No one is quite sure how it accesses this information.",stars=2),
    KitItem("chillychilichelle:boggart_boarding_system","Boggart Boarding System","A long, pointed cannon on a swivel loaded with boarding pods intended for the various creatures popular among mech pilots, weaponizing them as effective disruptors for burrowing into cockpits, jamming weapons, or simply being a general nuisance.",stars=2),
    
    BodyPlanItem("chillychilichelle:buddy_system","Buddy System","At the cost of a little bit of legroom, the mech has been modified to accommodate 2 cockpits, delegating responsibilities between them. However, 2 pilots are now required to properly pilot the mech.", {"cockpit": 2},stars=3),
    CockpitItem("chillychilichelle:childhood_sweets","Childhood Sweets","A small drawer in the cockpit filled with old, discontinued candies from your youth. They don't taste as great as you remember, but they still make you feel warm and fuzzy.",["cosmetic"],stars=3),
    CockpitItem("chillychilichelle:unsettling_figurine","Unsettling Figurine","A grotesque bobblehead depicting some type of horned imp or devil. Its pale yellow flesh is made of a flabby rubber, where two bulbous red eyes poke out. You think it's inching closer to you when you're not looking, but you can't quite tell.",["cosmetic"],stars=3),
    KitItem("chillychilichelle:shared_history","Shared History","You know your opponent better than the back of your hand. Whether as former friends, rivals, or nemeses, you understand what makes them tick. With that knowledge, you can make a risky, precarious maneuver to predict their next move to counteract it - the more specific, the more effective.",stars=3),
    
    BodyPlanItem("chillychilichelle:decommissioned","Decommissioned","A machine of combat and war from a bygone era, now used for agriculture, construction, or logistics. Foregoing all weapons, the mech now sports up to 5 kits to maximize utility.",{"kit": 5},stars=4),
    CockpitItem("chillychilichelle:crumpled_letters","Crumpled Letters","Old letters exchanged between you and a rival pilot. You keep them gingerly tucked in a small folder underneath your seat.",["cosmetic"],stars=4),
    CockpitItem("chillychilichelle:corner_entity","Corner Entity","A tall, lanky shadow creature has taken shelter in the eastern end of your cockpit. She seems docile and doesn't seem to be bothering anyone, so you do your best to keep the cockpit dim. Sometimes you play with her using hand shadow puppets.",["cosmetic"],stars=4),
    BodyPlanItem("chillychilichelle:mobius","Mobius","Something is deeply wrong with your mech. From everything you can gather, you have to conclude that it simply has no back - a flat, depthless image always facing toward any observer trying to perceive it. It feels like it's watching you as much as you it.",{"back": 0},stars=4),
    
    PowerItem("chillychilichelle:the_hole","The Hole","A floating-point error in the fabric of space-time, long-forgotten by the world. A small black pinprick in reality is suspended in layers of protective glass and steel. Whenever you try to look at it, you find yourself looking somewhere else - and the world looks a bit different.",stars=5),
    KitItem("chillychilichelle:last_hope_protocol","Last Hope Protocol","A 2-meter tall circular steel frame at the back of the cockpit. Upon ignition, the pilot will be tethered to this reality before being shifted into an unknown plane for 365 days, while only a split second passes. When they return, they will have gained something they didn't know they needed.",stars=5),
])

chimera = Mech("chimera",
[
    CockpitItem("chimera:library", "Personal Library", "A cozy space filled with your favorite books. The mech can be controlled from a comfy reading chair.", stars=2),
    BodyItem("chimera:ancient_tablet", "Ancient Tablet", "A massive and nearly unbreakable stone tablet engraved with an ancient language of giants.", stars=2),
    ArmsItem("chimera:floating_ink", "Antigravity Ink", "Ink generators that produce floating globules in the shape of arms.", stars=2),
    LegsItem("chimera:rolling_ladders", "Rolling Ladders", "An unreasonable amount of ladders with little wheels for rolling around.", stars=1),
    WeaponItem("chimera:word_changer", "Wordplay", "A strange energy cannon. When it hits a mech's fourth wall, one of the words in the description of its actions is changed.", stars=4),
    BackItem("chimera:endless_scroll", "Endless Scroll", "A scroll of paper that can never be fully unrolled.", stars=2),
    KitItem("chimera:writer_drone", "Auto-Chronicler", "A small, enthusiastic drone that can observe the mech's fights and write \"slightly\" embellished descriptions of them.", stars=3),
    CosmeticItem("chimera:onomatopoeia", "Onomatopoeia Projector", "A device that projects holograms of comic-style onomatopoeia in the air for any nearby sounds.", stars=3),
    PowerItem("chimera:story_power", "Story Gorger", "A thin wormhole connected to a bored extradimensional entity who will supply energy in exchange for stories.", stars=4),
    BodyPlanItem("chimera:floating_cockpit", "Floating Cockpit", "No body, arms, or legs. Just a floating cockpit with gizmos attached.", {"body": 0, "arms": 0, "legs": 0}, stars=3),
    CockpitItem("chimera:super_library", "Memory Archive", "A cozy space extrapolated from your memory and imagination, filled with books and other media created from your experiences and favorite stories. The mech can be controlled by writing in the empty book containing the future.", stars=5),
    KitItem("chimera:martial_arts", "Martial Manual", "A reference manual detailing how to control a mech to perform various feats of martial arts.", stars=1),
    WeaponItem("chimera:trap_runes", "Trap Runes", "A set of magical runes that can be painted on any surface and detonated at will.", stars=2),
    CosmeticItem("chimera:rival_plushie", "Rival Plushie", "A cute plushie version of your rival's mech. It's very huggable and makes a satisfying sound when thrown at the wall.", stars=1),
    BodyPlanItem("chimera:phase_2", "Multi-Phase Boss", "Allows the mech to equip another weapon and kit item. Both additional parts are disabled at first, but can be swapped to, disabling your original weapon and kit items permanently.", {"weapon": 2, "kit": 2}, stars=3),
    LegsItem("chimera:teleport_legs", "Fantasy Strider", "Legs covered in swirling spells and tales of faraway places. With every step, they pierce through space and carry the mech a far distance while ignoring obstacles.", stars=4),
    WeaponItem("chimera:papercuts", "Papercut Curse", "A failed paper talisman that causes a mech's pilot to inexplicably suffer papercuts from anything they do.", stars=1),
])

homeslice = Mech("homeslice",
[
    WeaponItem("homeslice:fast_food_sign", "Fast Food Sign", "The sign of a fast food joint torn from the ground and ready to be wielded as a makeshift weapon.", stars=2),
    KitItem("homeslice:kinetic_shields", "Kinetic Shields", "Absorb a portion of the kinetic energy from an opponent's attack and redirect it to empower your own strikes.", stars=3),
    CosmeticItem("homeslice:cowboy_hat", "Cowboy Hat", "Keep the sun off your mech's face with this stylish leather cowboy hat!", stars=2),
    PowerItem("homeslice:big_money_no_wammies!", "Big Money No Wammies","A risky but powferful energy core devised by a partially mad mech engineer with a perchant for gambling. With a slot machine grafted into the pilot's controls that could either supercharge one's mech or blow it to pieces, there's only one question left to answer...Are ya feelin lucky punk?", stars=5),
    LegsItem("homeslice:chicken_legs", "Chicken Legs", "Give your mech that slavic mythology flair with these baba yaga style robotic chicken legs.", stars=2),
    BodyItem("homeslice:spartan_cuirass", "Spartan Cuirass", "A bronze humanoid torso hammered to resemble a chiseled set of abs, flattering and intimidating all at once.", stars=2),
    LegsItem("homeslice:8_foot_vertical_leap", "8 Foot Vertical Leaps" ,"A hydrologic set of legs resembling those of a rabbit or kangaroo and built to excel in Huge Leaps and Powerful Kicks.", stars=4),
    ArmsItem("homeslice:king_of_the_ring", "King of the Ring", "For those who like to get up and personal these powerful punchers are where it's at, complete with reinforced fists of steel.", stars=3),
    BodyPlanItem("homeslice:carcinization", "Carcinization", "ALL BECOMES CRAB", {"legs":6, "arms":2}, stars=4),
    WeaponItem("homeslice:reaper_man", "Reaper Man", "a giant scythe with a razor sharp edge and a sick skull carving at the top", stars=3),
    BackItem("homeslice:escape_pod", "Escape Pod","Fight not going your way? Climb into this rocked powered ejection pod and bail outta there.", stars=2),
    CosmeticItem("homeslice:sick_ass_demon_horns", "Sick Ass Demon Horns", "+10 Headbutt Damage", stars=3),
    LegsItem("homeslice:rockin_rollerblades", "Rocking Rollerblades", "Give your mech an extra boost of speed with these rocket propelled rollerblades- remember to wear a helmet!", stars=4),
    BackItem("homeslice:lashers", "Lashers", "Two thick snakelike appendages that extend from the back of the mech that can be used to restrain/grapple an opponent", stars=3),
])

shieldcaptain = Mech("shield captain",
[
    ArmsItem("shieldcaptain:fightin_forks","Fightin' Forks","Standard issue power loader arms rigged with freight forks at the forearm. Great for committing OSHA violations and getting work done.",stars=2),
    ArmsItem("shieldcaptain:linemans_longarms","Lineman's Longarms","Hydraulic cherry picker armatures fitted with hands for all the fun stuff uncertified people never got to touch.",stars=2),
    ArmsItem("shieldcaptain:uppercut_manifolds","Uppercut Manifolds","Aerodynamic arms optimized for swift CQC.",stars=2),
    BackItem("shieldcaptain:bloc_rockers_doombox","Bloc-Rockers Doombox","Brutalist vibes, epic sound. Originally an early warning siren system, it's been retrofitted to accept input from this cool 30 gig ipod I found.",stars=3),
    BackItem("shieldcaptain:sidewinder_saddlebag","Sidewinder Saddlebag","It's like a purse full of missiles. Well, only one (1) missile. Stackable item.",stars=2),
    BodyItem("shieldcaptain:pollywog_bulwark","Pollywog Bulwark","Frog shaped plating to make your Mecha more friend-shaped. Includes novelty keychain.",stars=5),
    BodyPlanItem("shieldcaptain:mechataur","Mechataur","Two sets of legs probably makes you faster right? Gain centaur stature and an extra set of legs but miss out on back items. Matching sets of legs make you even cooler.",{"legs":4,"arms":2,"back":0},stars=2),
    BodyItem("shieldcaptain:pipe_frame_chassis","Pipe Frame Chassis","No armour? No problem. Feel the wind in your hair and the lack of all nonessential safety equipment at your very exposed sides.",stars=2),
    CockpitItem("shieldcaptain:panopticon","PANOPTICON ","SEE EVERYTHING FROM YOUR TOWER - LEAVE NO WEAKNESS UNOBSERVED (interior accommodations of swiveling captains seat and gyroscopically stable coffee machine available with request)",stars=2),
    CosmeticItem("shieldcaptain:salvagers_sallet","Salvagers Sallet","The patron hardhat of warriors in the scrapyard, let your opponent feel your gaze and see your smile, all while not exposing too much of the face.",stars=2),
    CosmeticItem("shieldcaptain:firebreak_festoon","Firebreak Festoon","*Wear your laurels with pride, oh noble combatant.* A mark of honor, a garland of grease, the premier in fancy flowers that show you mean business.",stars=5),
    KitItem("shieldcaptain:more_cowbell","More Cowbell","Time marches on, for whom the cowbell ding-a-ling-a-lings. Destroy this item to deafen opponent.",stars=1),
    CosmeticItem("shieldcaptain:depot_deputy","Depot Deputy","50-Gallon bucket for a hat. Various colors available, but only in shades of orange.",stars=1),
    KitItem("shieldcaptain:space_jam_dvd","Space Jam DVD ","Metaphorically dunk on your opponents no more, dunk for real with the Space Jam DVD. Boosts jump height and grants a basketball size grenade. You know what to do.",stars=1),
    KitItem("shieldcaptain:kickass_combo_meter","Kickass Combo Meter","Chain hits without getting hit to increase the combo up to 10. When full, hit your opponent with an unavoidable monologue that gives you enough time to make 1 repair.",stars=4),
    KitItem("shieldcaptain:rally_spec","Rally Spec","Flared fenders, massive coilover suspension augmentations, and KC daylighter 100,000 lumen pod lights.",stars=2),
    KitItem("shieldcaptain:emergency_brake","Emergency Brake","Initiate a drift with a careful pull, or completely arrest all momentum at a moments notice. I hope you have a 5 point harness in there.",stars=1),
    KitItem("shieldcaptain:ravishing_capelet","Ravishing Capelet","Stitched with style and zeal, two very real elements, bewilder your opponent as you shroud deft maneuvers from sight and scanners alike. It's also like, really fancy.",["cosmetic"],stars=4),
    LegsItem("shieldcaptain:komatsu_battletread","Komatsu Battletread","Stylish kicks to get you and the earth moving. These repurposed treads make for a great option in quick repositioning and gliding stance charges.",stars=2),
    LegsItem("shieldcaptain:courier_cargopants","Courier Cargopants","You would not believe how many pockets these things have. Gain a kit slot that can hold systems of 2 star rarity or lower.",stars=2),
    LegsItem("shieldcaptain:duelists_dualie_axle","Duelists Dualie-axle","Comedically large and over spec-ed roller skates. Be nimble and funny as you dance circles around your opponent.",stars=3),
    LegsItem("shieldcaptain:fishnets_presumably","Fishnets, Presumably","When foreman Dan lost his legs, he made do with these massive bars of rolled steel. The knurling was later added for *aesthetics*.",stars=1),
    LegsItem("shieldcaptain:fleet_feet","Fleet-Feet","Mass produced and eternally reliable gas piston springs make great passive stabilizers for cable tendon actuated limbs. A streamlined system for lithe builds.",stars=2),
    PowerItem("shieldcaptain:neutrino_of_dubious_mass","Neutrino of Dubious Mass","This... Violates the laws of physics right? It's the size of a beach ball! And it weighs a ton! How does this even work?!",stars=4),
    PowerItem("shieldcaptain:daybreak_maw","Daybreak Maw","Midriff mounted gaping maw of fire, burns bright with your hunger for battle! (Fire extinguisher not included)",stars=4),
    PowerItem("shieldcaptain:ludicrous_lumpstick","Ludicrous-Lumpstick","Who needs *proper* valve timing anyway? Increases top speed, might explode. Flooring it compels you to roll 1d6, on a 6 *something* breaks.",stars=1),
    PowerItem("shieldcaptain:purpose_built_pompadour","Purpose-built Pompadour","Monolith of hair that defies gravity, channel its strength to lift yourself higher. Needs to be maintained with an equally large pocket comb.",["kit"],stars=3),
    WeaponItem("shieldcaptain:delvers_dredge","Delvers Dredge","A hefty anchor of dubious origin, recovered from the depths of the Core. Use this weapon to halt yourself or an opponent in their tracks.",stars=3),
    WeaponItem("shieldcaptain:four_meter_monkeywrench","Four-Meter-Monkeywrench","A common overscale pipe wrench made to service the infinite shrimp pipelines. Makes a fine bludgeon for mecha gacha combat.",stars=2),
    WeaponItem("shieldcaptain:tachyon_lance","Tachyon Lance","Mechs can have a little time travel, as a treat. Fires a beam of time, great for rusting out your opponents armour or getting 28 hours of sleep in about 4 seconds.",["kit"],stars=3),
])

n217 = Mech("n217",
[
    WeaponItem("n217:ace_of_swords","ARC110//Ace of Swords","Mass-produced mech cannon, spec'd for penetrative capability over destructive power.",stars=1),
    BodyItem("n217:ace_of_cups","ARC120//Ace of Cups","Basic, mass-produced mech frame. Has barely enough space inside for a single pilot.",stars=1),
    ArmsItem("n217:ace_of_pentacles","ARC130//Ace of Pentacles","Mass-produced mech arms, with nimble, articulated digits capable of delicate work—at the cost of actual material strength.",stars=1),
    LegsItem("n217:ace_of_wands","ARC140//Ace of Wands","Mass-produced mech legs, which comes with an autonomous movement scheme, allowing—at the flip of a switch—for a mech to run towards a destination, without pilot input, and without any heed to obstacles or hazards in the way.",stars=1),
    CosmeticItem("n217:the_fool","ARC000//The Fool","A mechanical bird, styled after A.R.C.’s logo, perched on top of the mech. ARC000 uses a negligible amount of fuel to chirp and flap its wings, as well as to stabilize against impact or wind—to always remain standing, always looking ahead.",stars=2),
    PowerItem("n217:the_magician","ARC001//The Magician","A miniature portable recycling plant. ARC001 consumes various types of raw material—scavenged mid-battle from the remains of mech combat, through a network of tubes attached to a mech's legs and arms—and rapidly converts them into usable fuel.",stars=2),
    WeaponItem("n217:the_high_priestess","ARC002//The High Priestess","A phantasmal armament. ARC002 is a durable straight sword, perpetually surrounded by some dozen near-identical holograms of itself, designed to confound the opposition and obscure trajectories of attack.",stars=2),
    CockpitItem("n217:the_empress","ARC003//The Empress","A.R.C.’s general purpose Mech AI, which communicates via a mechanical sunflower. Through a network of “roots” which runs through the mech, ARC003 possesses the ability to detect most preliminary signs of damage, as well as perform basic maintenance and repair on the field.",stars=3),
    BodyItem("n217:the_emperor","ARC004//The Emperor","A sleek, pure black mech frame. Being A.R.C.'s first—and to date, only—military contract, ARC004 is designed to withstand damage, absorb impact, and muffle electromagnetic interference to a degree that far exceeds the average duelist mech.",stars=3),
    CockpitItem("n217:the_hierophant","ARC005//The Hierophant","A.R.C.'s environmental analysis Mech AI, which communicates via a hologram of a stylized eye. Built directly into ARC005 is a complex physics engine, allowing the AI to near-perfectly predict the location and movements of enemy mechs—regardless of any effects interfering or restricting visibility.",stars=3),
    KitItem("n217:the_lovers","ARC006//The Lovers","A liquid which gathers near any exposed 'wounds' on a mech. Acting as a universal binding agent, ARC006 can attach to *any* mech parts—such as the mech's own severed limbs, or the arms and legs “borrowed” from enemy mechs—and anchor them to any damaged sections, allowing quick on-field repair.",stars=4),
    LegsItem("n217:the_chariot","ARC007//The Chariot","ARC007 is composed of two interrelated parts: a series of thin legs on the outside, trading resilience for high speed; and some dozen copies inside, that will be released and attached to the mech whenever any outer legs are damaged beyond use. Designed for constant motion, heedless of harm.",stars=3),
    KitItem("n217:strength","ARC008//Strength","A team of between 4 and 6 skilled rodent technicians, machinists, and necromancers for hire. They tend to drive a hard bargain, but they are frighteningly effective in return—willing to work themselves to death (and back out of it) to keep all systems online. Just make sure your mech is fireproof.",stars=3),
    PowerItem("n217:the_hermit","ARC009//The Hermit","A power cell of improbable energy density—just one the size of a fist is enough to last days. However, ARC009 is also highly unstable, needing to be placed in a sealed chamber and constantly supervised for any potential signs of disaster. At least the warm iridescent glow around it looks nice.",stars=4),
    ArmsItem("n217:wheel_of_fortune","ARC010//Wheel of Fortune","Drones in the shape of hands. These can be used as normal arms and range extenders, or they can be set to operate autonomously—seeking out, interfering with, and countering any enemy offenses without pilot input…as long as you trust the highly unpredictable, two-decade-out-of-date AI to do its job.",["weapon"],stars=2),
    BackItem("n217:justice","ARC011//Justice","A massive fish tank, attached to a mech's back. The water within ARC011 is perpetually murky, only allowing the briefest of glimpses at its inside—at the shadow of a cetacean eye, whose gaze seems to tear at one's guilt and regret down to the bone. A protection against backstabs and sneak attacks.",stars=4),
    ArmsItem("n217:the_hanged_man","ARC012//The Hanged Man","Lightly-rusted mechanical arms, made from interlocking copper plates and gears. A technology inherited from A.R.C.’s predecessor grants ARC012 the ability to “steal time” with every direct melee attack—slowing down an opponent a few seconds at a time, whilst speeding the mech in return.",["weapon"],stars=3),
    BodyPlanItem("n217:death","ARC013//Death","Any mech part can draw blood, or feed an engine. Any hollow space can house a pilot. Torn off limbs can be replaced with those still intact, and plating around thrusters can fill gaps in armour. ARC013 is a shapeless blueprint, made to accommodate adaptation—even in the midst of combat",{"legs":2,"arms":2},stars=4),
    KitItem("n217:temperance","ARC014//Temperance","A network of tunnels within a mech, which seems to magnify the cacophony of battle and attract Unbirds. ARC014 grants a mech the ability to submerge into the ground, much like the unvians within it—with the maximum duration spent underground increasing with greater quantities of Unbirds.",stars=3),
    BodyPlanItem("n217:the_devil","ARC015//The Devil","Blades in the back, shots in the dark. ARC015 can muffle sound, hide heat signatures, and is capable of carrying upwards of 2 extra weapons—at the cost of automatically retracting and disabling all weapons when directly illuminated and observed. Keep out of sight, and keep the lights shut.",{"legs":2,"arms":2,"weapon":4},stars=3),
    WeaponItem("n217:the_tower","ARC016//The Tower","A simple throwing spear that can be remotely detonated. Within is a microscopic mote of misfortune, which on contact with air creates a rapidly-growing improbability field—boosting the chances of unlikely events (catastrophic errors, heart attacks, etc), while dropping the chances of likely ones.",stars=4),
    CosmeticItem("n217:the_star","ARC017//The Star","A purely decorative constellation of lamps, too weak to properly illuminate beyond a mere few steps forward. Yet, something in your heart tells you that if you are ever lost, ever stranded, ever too far from your mech, those lights will guide you back to the cockpit—to where you belong.",stars=2),
    CosmeticItem("n217:the_moon","ARC018//The Moon","A coat of glimmering, ashy paint. ARC017 can, in theory, work as a genuine source of illumination—releasing a light which intensifies the closer the mech is to the nearest moon, to potentially blinding luminosity. However, due to the location of most mech arenas, it often only manages a dim glow.",stars=3),
    CosmeticItem("n217:the_sun","ARC019//The Sun","Days before the historic 27-day A.R.C. strike, an engineer saved a defunct Mech AI from being scrapped. It ended up playing such a key role in broadcasting the strike that, after the strike's victory, it was preserved and spread across A.R.C.—eventually becoming ARC019, your cheerful, sunny friend.",stars=3),
    CockpitItem("n217:judgement","ARC020//Judgement","A copper bird with gemstone eyes, a gift from A.R.C., whistles. Outside, traps open early, and the killzone timer beeps late, and opponent mechs are swallowed in quicksand. Your opponent is struggling against these sudden obstacles, but it’s futile. The results—the bird whispers—are already fixed.",stars=5),
    LegsItem("n217:the_world","ARC021//The World","Once, an ARC140 was inscribed with strange runes found on a pair of abnormally sturdy trekking boots. ARC021 is the result: mech legs which cannot break, fail, or kneel, and which can teleport to “anywhere graced by ingenuity, curiosity, or exploration”—carrying the will to chart the world onwards.",stars=5),
])

nevephoenix=Mech("nevephoenix",
[
    ArmsItem("nevephoenix:dragon_knight_arms","Dragon Knight Armor","Beautiful polished armor, built to last against dragon fire without scorching the knight inside.",stars=3),
    ArmsItem("nevephoenix:bear_arms","Bear Arms","Strong hairy bear arms. Build to catch salmon quickly.",stars=2),
    LegsItem("nevephoenix:cursed_red_shoes","Cursed Red Shoes","These legs come with red shoes cursed to dance until you drop. You do dance fantastic though.",stars=1),
    LegsItem("nevephoenix:glass_slippers","Glass Slippers","Beautiful strong dragon-glass slippers on very pretty legs. Perfectly sized for your mech, and excellent to run in.",stars=4),
    BodyItem("nevephoenix:princess_dress","Princess Dress","Beautiful and sparkly, it flows in a ballgown fashion.",stars=1),
    BodyItem("nevephoenix:swan_princess","Swan Princess","A ballgown made of magical feathers, each glowing and fluttering in the wind.",stars=2),
    BodyPlanItem("nevephoenix:tower","Tower","Your mech is tall. Real tall. Kicking is your strong suit", {"legs":2}, stars=1),
    BodyPlanItem("nevephoenix:fairy","Fairy","Your mech is lightweight with an extra back slot to accomodate wings", {"back":2}, stars=1),
    BackItem("nevephoenix:pixie_wings","Pixie Wings","Small and flight enabling,  these green dragonfly wings will help you move quickly.",stars=1),
    BackItem("nevephoenix:dragon_wings","Dragon Wings","Large draconian Wings, allowing powerful flight causing gusts of wind when you land",stars=3),
    WeaponItem("nevephoenix:magic_wand","Magic Wand","Use your imagination to transform one thing into another thing temporarily",stars=4),
    WeaponItem("nevephoenix:pheonix_fire","Pheonix Fire","White-hot flame that shoots out of your mech's hands",stars=3),
    CosmeticItem("nevephoenix:frog_prince","Frog Prince","Your mech has powerful amphibian legs, or webbed fingers and a very nice doublet or a feathered hat",stars=3),
    PowerItem("nevephoenix:true_loves_kisses","True Love's Kisses","Feelings describe the power contained in a kiss. Words do not.",stars=5),
])

zapterra=Mech("zapterra",
[
    KitItem("zapterra:standard_shoes","Standard Shoes","Shiny, black. One inch heels, thin suede soles, and laces. Driving steps, quick rotation, movement with a partner.",stars=1),
    KitItem("zapterra:latin_shoes","Latin Shoes","Matte, black. Four inch heels, thin suede soles, and laces. Hip action, quick redirections, push and pull connection with a partner.",stars=1),
    PowerItem("zapterra:paso_doble","Style: Paso Doble","Your eyes never leave your opponent. Confidence, showmanship, strength, domination. Complete control of the battle's pace. Flamenco styling in the arms.",stars=2),
    PowerItem("zapterra:foxtrot","Style: Foxtrot","Beautiful, streamlined motion with powerful posture that never wavers. Getting in the way of your path of motion is a bad idea.",stars=2),
    PowerItem("zapterra:waltz","Style: Waltz","Beautiful, streamlined motion and rotation. Aggressive possession and control of space with strong, extended, mobile posture.",stars=2),
    PowerItem("zapterra:quickstep","Style: Quickstep","Impossibly fast, to the detriment of technique. Breakneck steps, hops, kicks and redirection. Impossible to predict, with distances closed in a fraction of an instant.",stars=2),
    PowerItem("zapterra:jive","Style: Jive","Your every energy and optimization is placed into the strength, speed and length of blazing fast kicks, leg movement, and footwork. Flashy, without the need for a partner.",stars=4),
    PowerItem("zapterra:rumba","Style: Rumba","Slow and intentional movement with extensive hip action, legwork, and tension between partners. Spot rotations so fast you can't see them happen.",stars=2),
    BodyPlanItem("zapterra:standard_frame","Standard Frame","Two sets of facing bipedal legs that shift in and out of line. Upper body locks in place, redistributing impacts to the system. Forgoes weapons, favoring momentum and rotation with occasional kicks. 4 legs, 2 bodies, 2 power sources, 2 cockpits, 1 back.",{"legs":4,"weapon":0,"body":2,"cockpit":2,"power":2},stars=4),
    CosmeticItem("zapterra:competition_number","Competition Number","How else will the judges call you back?",stars=1),
    CosmeticItem("zapterra:spray_tan","Spray Tan","Helps you look more natural when you're under bright lighting. Helps you look more scary when you're not.",stars=1),
    CosmeticItem("zapterra:competition_dress","Competition Dress","A flowing dress in beautiful colors. Decorated with two bajillion rhinestones.",stars=2),
    CosmeticItem("zapterra:tailsuit","Tailsuit","Handsome. Stylish. Classy. Sweaty.",stars=2),
    PowerItem("zapterra:ten_dance_champion","Ten-Dance Champion","Relentless endurance. Unmatched aggression and intentionality. You know exactly where you are, how you're about to move, and where your opponent's balance could use some improvement.",stars=5),
    KitItem("zapterra:kinetic_anchorage","Kinetic Anchorage","A nanite field that allows you to to push, pull, and redirect momentum from points in midair. Almost as good as a partner.",stars=3),             
])

jcterran=Mech("jcterran",
[
    WeaponItem("jcterran:km1_autocannon","KM-1 Autocannon","A sturdy, high-caliber autocannon, belt-fed and suited for a variety of ammunition types.",stars=1),
    BackItem("jcterran:ammunition_pack","Ammunition Pack","A series of boxes, pouches, and mag-locks hold all the ammunition your mech could need. Could store magazines, shells, capacitors, or more exotic ordnance...",stars=1),
    WeaponItem("jcterran:deca1_burst_laser","DECA-1 Burst Laser","This bulky energy weapon fires a high-powered laser over short ranges. Because of its significant power draw, it is usually run off a set of manually reloaded capacitor banks, though it can be reconfigured to draw directly from exceptionally powerful reactors.",stars=1),
    CosmeticItem("jcterran:stylish_graffiti","Stylish Graffiti","A colorful selection of personal icons, fantastical images, and barely readable text applied to your mech via spray paint. Ideal for self-expression and chaotic flair.",stars=1),
    BodyItem("jcterran:boxy_frame","Boxy Frame","A bulky, hard-edged frame for your mech, making it loom over the battlefield. Presents a large target profile, but bristles with hardpoints. A body fit for the dispassionate, the utilitarian, or those who want to make an impression.",stars=1),
    ArmsItem("jcterran:branched_arms","Branched Arms","These dull metal arms split at the elbow joint. One branch ends in a heavy claw, fit for wielding weaponry, while the other ends in a set of light manipulator tendrils.",stars=2),
    ArmsItem("jcterran:plated_arms","Plated Arms","These up-armored arms have been covered in heavy, overlapping metal plates. The armor may impede flexibility, but it will make the arms harder to destroy.",stars=1),
    LegsItem("jcterran:plated_legs","Plated Legs","These up-armored legs feature powerful hydraulic joints covered in layered metal plates. They might not the fastest legs around, but they will be difficult to destroy with weaker weaponry.",stars=1),
    WeaponItem("jcterran:kca1_defense_rockets","KCA-1 Defense Rockets","A cluster of four dumbfire rockets, mounted on an external rack. Their HEAT payloads can do serious damage, but they lack accuracy, and the system comes with no spares. Don't spend them all in one place...",stars=2),
    WeaponItem("jcterran:kl2_antimaterial_rifle","KL-2 Anti-Material Rifle","A heavy rifle, loaded with hyperdense metal slugs that can punch straight through armor. The weapon's onboard optics are synced directly with your mech. According to TPGA superstition, models with serial numbers ending in 13 are considered lucky. This one isn't, though.",stars=3),
    CockpitItem("jcterran:sensor_cockpit","Sensor Cockpit","This sloped cockpit is set into your mech's body, covered in sensor arrays, radar dishes, and cameras. The sensors' vision is projected onto a wraparound display in the cockpit. Good for finding your enemy's weaknesses but could be blinded if the sensors were disabled. ",stars=3),
    KitItem("jcterran:cryocoolant_system","Cryo-Coolant System","This extensive cooling system cycles hypercooled liquids through your mech's systems. Curiously, it appears to have been assembled from long-haul cryopod components. This could keep your mech stable when using high-energy systems.",stars=3),
    WeaponItem("jcterran:km3_grenade_launcher","KM-3 Grenade Launcher","A heavy rotary grenade launcher, capable of being mounted both internally and externally. This design has the unusual ability to fire adhesive-coated \"sticky\" rounds, which can be detonated by remote, in addition to standard payloads.",stars=2),
    KitItem("jcterran:capacitor_banks","Capacitor Banks","A set of externally-mounted supercapacitors, arranged in vertical banks. They can be charged by your mech's reactor from spare power, then expended for extraordinary bursts of energy. However, they take a long time to recharge after each use.",stars=2),
    WeaponItem("jcterran:kl2_antimaterial_rifle_lucky","KL-2 Anti-Material Rifle (Lucky)","A heavy rifle, loaded with hyperdense metal slugs that can punch straight through armor. The weapon's onboard optics are synced directly with your mech. According to TPGA superstition, models with serial numbers ending in 13 are considered lucky, and this one is!",stars=4),
    WeaponItem("jcterran:fusion_glaive","Fusion Glaive","Channels power down a maglocked, variable-length haft into a jet of pure energy. Linked directly to your mech's reactor, the blade's theoretical output is near limitless: given sufficient power, it can kill anything.",stars=5),
    WeaponItem("jcterran:aurora_point_defense_system","AURORA Point Defense System","A networked array of lasers built into the frame of your mech. Can intercept physical projectiles, blind enemy sensors, and attack soft targets at close range. On low power, they can also project a spectacular lightshow.",["cosmetic"],stars=4),
])



urirles=Mech("urirles",
[
	PowerItem("urirles:fusion_cell","Fusion Cell","Stable, efficient, small, boring. Slotted in a standard power mount, it will power a mecha under a normal load and a bit beyond. Just don't expect anything fancy as it was designed with reliability in mind. And cost-cutting, admittedly.",stars=1),
	KitItem("urirles:last_century_embedded_electronics","Last Century Embedded Electronics","Listen, if it was good enough for working on the Lantern III Scrapyards fifty years ago, it's still good enough now. Old and clunky, yet also hardened and missing some of the wireless stuff that make modern mechs remotely hackable.",stars=1),
	BodyItem("urirles:scrapyard_field_upgrade","Scrapyard Field Upgrade","A bunch of steel plates haphazardly welded around the body of your mech, adding quite a bit of improvised spaced armor.",stars=1),
	LegsItem("urirles:heavy_duty_pneumatic_legs","Heavy Duty Pneumatic Legs","Two big steel legs, powered by massive pistons. Rugged and reliable, those won't get you anywhere fast, but they will get you there eventually. And noisily.",stars=1),
	WeaponItem("urirles:foam_cannon","Foam Cannon","Used to put out fire and seal hull breach, the rapid hardening foam can be retasked to impair your opponent's movements.",stars=1),
	CockpitItem("urirles:extreme_environment_cockpit","Extreme Environment Cockpit","This cockpit will keep you safe in the most hostile of work environment, from temperature control to radiation shielding. It will also give you an accurate reading of all that fun stuff it's working hard to keep outside.",stars=2),
	CosmeticItem("urirles:days_since_last_incident","_ Days Since Last Incident","A whiteboard that allows you to keep track of the last time you ripped another mech in half.",stars=2),
	PowerItem("urirles:fusion_cell_hotwired","Fusion Cell (Hotwired)","You went and did it. This cell had most of its safeties shunted to allow for a much higher and spiker power profile. This also made it sensitive to direct impact, overheating and runaway reaction. And worst of all, it voided the warranty.",stars=2),
	ArmsItem("urirles:hydraulic_clamps","Hydraulic Clamps","Heavy arms that ends in massive clamps. Can grab and lift some hefty weights, but do not expect to pick up eggs.",stars=2),
	CosmeticItem("urirles:white_noise_backing_signal","White Noise Backing Signal (Loud)","Normally used for workplace safety, this speaker has been hot-wired to announce your approach with a wave of white noise.",stars=3),
	WeaponItem("urirles:steel_cutting_beam","Steel Cutting Beam","Short-ranged, but able to punch through most conventional armour. Can't help you against shield or reflective material. Most often put on a shoulder mount, leaving the hands free to hold the target.",stars=3),
	BackItem("urirles:onboard_forge","Onboard Forge","This portable (if cumbersome) factory allows you to build spare parts or field fortifications. It churns a good amount of smoke while in use.",stars=3),
	KitItem("urirles:structural_analyser","Structural Analyser","Initially used in demolition work, this sensor suit gives you an internal 3D representation of whatever you scan, helping to pinpoint weak spots.",stars=4),
	BodyPlanItem("urirles:modular_fittings_points","Modular Fitting Points","By optimising space usage and adding universal internal and external mounting points, you can plug another Kit and another Back item. It also makes repairing easier by just switching damaged parts.",{"back":2,"kit":2},stars=4),
	BackItem("urirles:onboard_nanoforge","Onboard Nanoforge","Cutting edge nanomachine powered forge in a sleek design, it can produce most small parts almost instantly, or build structure remotely by dropping nano-goo. And no smoke!",stars=5),
])


nullified = Mech("nullified",
[
    Item("nullified:null_pointer", "Null Pointer", "A jagged shard of unreality that, by all definitions, does not exist. Sensors and computer systems go haywire when nearby. Was something else here, before?", ["power","weapon","kit"], stars=5),
    CosmeticItem("nullified:null_device", "Null Device", "A mysterious bucket that devours all inputted information. Useful for waste disposal.", stars=1),
])




event_formal = Mech("48th Annual Mech Formal",
[
    WeaponItem("event_formal:intergalacticsky", "F.L.P. Rippers", "Excessively long and ornately detailed nails ready to Slay your Enemies, in true industry fashion", stars=3, tags=("event",)),
    CosmeticItem("event_formal:hillexed", "Smoochable Lips", "A large pair of realistic lips adorn the outside of the cockpit. They have limited articulation, just in case you need to pucker up.", stars=3, tags=("event",)),
    KitItem("event_formal:loading", "Gyroscopic Stabilizer", "a bleeding edge internal part that prevents the mech from losing their balance and falling over. ideal for elaborate dances or striking truly insane poses", stars=3, tags=("event",)),
    BackItem("event_formal:hal_2000", "Cloak and Dagger", "A large, fancy cloak paired with a small needle hidden somewhere in the hand/wrist of the mech. The needle is primarily a data collection tool that sends information about whatever is stabbed to the cloak, which is actually made of optical camouflage!", stars=3, tags=("event",)),
    KitItem("event_formal:st_yietus", "LAST DANCE - ASTRAL WING", "A mysterious system lies sleeping within your mech. Only when your will is in perfect concert with your mech's will it awake, projecting the pure energy of your soul outward in a beautiful-and destructive-display. It is said to have the power to reshape the cosmos to your will... use it wisely.", stars=3, tags=("event",)),
    CosmeticItem("event_formal:chillychilichelle", "Cognitive Bloom", "A small, 2-inch-wide metal disc mounted onto the top of the cockpit. Emitting a high pitch, the device projects a fuzzy model of an enormous flower into viewers' minds. Observers disagree on what species it is but all claim to have seen their favourite.", stars=3, tags=("event",)),
    KitItem("event_formal:deric", "Strapless And Backless", "Through complex technology, every component of the mecha floats independently of each other, allowing ultimate control and dodging. However, the Back slot cannot be used.", stars=3, tags=("event",)),
    PowerItem("event_formal:shork", "Yureactor", "A generator that runs off of the pilot's positive feelings towards a significant other. Romantic, platonic, any kind of love that drives you forwards.", stars=3, tags=("event",)),
    WeaponItem("event_formal:oneirocartographer", "Razorsilk Skirt", "Your mech wears a long, flowing skirt made of an ultrafine biometallic alloy. Twirl right and you can slice an opponent in half – just be careful with it on the dance floor...", stars=3, tags=("event",)),
    CosmeticItem("event_formal:thecowofeternalflame", "Aetherial Ball Gown", "A stunning long flowing black gown made of aetheric energy and swirling constellations. The gown has short poofy off-shoulder sleeves and the bottom trails on the ground a bit after your mech. The pattern continuously shifts and the stars glitter from every angle.", stars=3, tags=("event",)),
    CockpitItem("event_formal:triangle", "Table for Two", "Your cockpit is a secluded table, set for two. The carpet is red. The decor is Art Deco. A system of ceiling tracks suspend two chairs and a butlerprobe with bespoke arms for every need and a snazzy bowtie. Now all it needs is your date 😳👉👈", stars=3, tags=("event",)),
    WeaponItem("event_formal:theoddman", "Oversized tin cans", "Oversized tin cans attached to string from a mech marriage ceremony. A part of romantic(?) tradition for some reason. Can be used either as a weapon or a cosmetic.", stars=3, tags=("event",)),
    CosmeticItem("event_formal:ditto", "Fancy Top-Hat", "The most formal of formal attire.", stars=3, tags=("event",)),
    CosmeticItem("event_formal:p_rker", "Collar", "Indicates a mech's name and point of origin, and makes a decisive fashion statement.", stars=3, tags=("event",)),
    PowerItem("event_formal:loftyinclination", "Wedding Band", "A band of precious metal, otherwise inert. Somehow, your mech is far more resiliant when wearing it, though there has been a notable decrease in your attack damage when facing off against your rival.", stars=3, tags=("event",)),
    CosmeticItem("event_formal:neve", "Fascinator", "A beautifully elaborate hat, slightly small for the head.", stars=3, tags=("event",)),
    CosmeticItem("event_formal:n217", "ARC138//Nine of Pentacles", "Originally created to celebrate the new millennium, ARC138 is an endless stream of golden radiance, flowing unimpeded from the hands of the mech. This obscene wealth is not real, and leaves nothing behind—merely a masterful (and highly over-indulgent) trick of the light.", stars=3, tags=("event",)),
    WeaponItem("event_formal:cheesesnack", "Literal Chocolate Bomb", "Coat your target in sticky, searing-hot chocolate that hardens as it cools. A product of the Iron Chef Wars.", stars=3, tags=("event",)),
    BodyItem("event_formal:colabot", "Ghostly Garments", "An ethereal, semi-transparent body dressed in fancy cocktail attire. Despite its intangible nature, it seems to be able to attach to the other components of your mech just fine. Impervious to physical damage - attacks just phase through. Can’t kill what’s already (drop) dead (gorgeous)!", stars=3, tags=("event",)),
    WeaponItem("event_formal:cheshire", "Girl's Best Friend", "Usually worn as a tiara, broach, or cufflink, the beam fired from this enchanted jewel grows more powerful for each reflective or crystalline surface on your mech.", stars=3, tags=("event",)),
    PowerItem("event_formal:bytes", "Kaiju Blood", "This mech is powered by the ancient spirit within the blood of a kaiju.", stars=3, tags=("event",)),
    CosmeticItem("event_formal:intoamutecrypt", "Symphony In C", "It's warm and golden like an oven that's wide open.", stars=3, tags=("event",)),
])

event_fauna = Mech("FRONT's FAUNA Invitational",
[
    LegsItem("event_fauna:bytes","NewtTech Legs","Lose a limb? Regrow it!",stars=3,tags=("event",)),
    BodyPlanItem("event_fauna:triangle","Metamorphosis","Your mech is still developing. It begins an encounter as a highly armored low mobility crawler: 2 weapons, 0 limbs. Upon maturity the carapace cracks, allowing what has developed to burst forth, a new shape rapidly hardening as it exits: 3 sets legs, 0 arms, can fly. No item is shared between forms.",{"weapon":4,"arms":0,"legs":3,"kit":2,"back":2,"power":2,"body":2},stars=3,tags=("event",)),
    WeaponItem("event_fauna:ditto","Volt Beetle Horn","This horn seems to be inspired by the Volt Beetles that live in the Core, slowly generating a static charge that can be released to stun opponents.",stars=3,tags=("cockpit", "event",)),
    BackItem("event_fauna:shork","Mucus Barrier","A free-floating mucus cocoon surrounds your mech. This shield disrupts sensors attempting to identify or locate your mech, and destroys parasitic attachments. Although the shield can tank attacks relatively well, doing so will cause it to lose integrity.",stars=3,tags=("event",)),
    WeaponItem("event_fauna:hal_2000","Mach Bullet Punchers","Adds another pair of arms to your mech. These arms are mounted with a pair of hanging spring-loaded metal clubs that can launch at a speed exceeding the speed of sound. Enemies in melee range not hit may suffer deafness or be stunned by the firing of a club. Stronger underwater.",stars=3,tags=("event",)),
    BackItem("event_fauna:syl","Horse Back","It’s a horse, tied to your back. It whinnies occasionally and you can feed it oats.",stars=3,tags=("event",)),
    BackItem("event_fauna:loading","Photaxis Phlare","A back mounted phase drive that plunges you into the immateria. While submerged in this way you may only move towards sources of strong UV radiation. Luckily this system is also equipped with a strong UV flare gun to provide valid lights, but other lights are also valid.",stars=3,tags=("weapon", "event",)),
    PowerItem("event_fauna:moonbug","Electric Eel Tank","A large aquarium holding a happy group of electric eels that help power your mech.",stars=3,tags=("event",)),
    KitItem("event_fauna:thecowofeternalflame","Blood Vents","These vents are connected to whatever fluid the mech uses to keep itself functioning. Like the Horned lizard this is designed after, this allows the mech to fire a short-range blast of it's own \"blood\" as a defense mechanism.",stars=3,tags=("event",)),
    KitItem("event_fauna:bee","Adaptive Skin","The skin of this mech can change colour and texture in order to communicate, look cool, and camouflage itself. It does not perfectly replicate what is behind it, but instead it can achieve the general vibes of the surface the mech is on.",stars=3,tags=("event",)),
    BodyPlanItem("event_fauna:hill","Planarian Power","This flatworm bodyplan has zero legs and must wriggle on the ground. However, the first time your mecha is cleanly cut in half, each half can regenerate into a full mecha!",{"legs":0},stars=3,tags=("event",)),
    KitItem("event_fauna:st_yietus","HAGSKIN DISSUASION SYSTEM","Inspired by the humble hagfish, this system emits voluminous slime from your mech's skin to engulf your foes. The slime expands exponentially in liquid, clogs up enemy intakes, and thanks to a special blend of exotic polymers it also weakens incoming attacks of all kinds! It's the perfect defense.",stars=3,tags=("event",)),
    KitItem("event_fauna:intergalacticsky ","Vibrissae","Sensory arrays are placed on key parts of the mech, allowing for increased detection of movement, wind, and other disturbances. Extremely sensitive and easy to max out.",stars=3,tags=("event",)),
    ArmsItem("event_fauna:chimera","Featherful","Fluffy and colorful feathered wings that enable flight.",stars=3,tags=("event",)),
    KitItem("event_fauna:cheshire","Exuvian Mimic","Shed your skin. This fragile simulacra is already dead, but your doomed twin will do as you ask. Without power, it cannot sustain itself or it's weapons for long, and without you, its poor carapace will not endure the wounds of the world. Do not begrudge your past self for its limitations.",stars=3,tags=("event",)),
    BackItem("event_fauna:ava_shinedrake","Starbreak Anemone","Your mech has formed a symbiotic relationship with a minor eldritch entity, now anchored to its back. Midnight tendrils flow eerily around your mech, inflicting anything they touch with data hallucinogens that corrupt computers and mesmerize AI. Luckily, repeated exposure has made your mech immune.",stars=3,tags=("weapon", "event",)),
    BackItem("event_fauna:chillychilichelle","Suriname Birthing Pods","A perforated metal husk inspired by the common Suriname toad. On the surface are a dozen honeycomb-like depressions, each overflowing with a viscous, translucent slime - each housing a miniature biomechanical replica of your mech, ready to burst out on command as drones.",stars=3,tags=("event",)),
    CosmeticItem("event_fauna:colabot","Deer Dappling","Delicate spotting is painted on your mech’s hindquarters (or… thorax? Your mech’s caboose, alright?). It’s pretty, like the pattern of sunshine through leaves. In a very specific environment, it might help you camouflage yourself, but it most looks nice.",stars=3,tags=("event",)),
    LegsItem("event_fauna:renne","Snikt Kickers","Spindly metal legs with a lining of waterproof padding. In combat, the endoskeleton's toe parts can be severed on inbuilt faultlines to pierce this padding and provide an additional weapon at a cost to durability.",stars=3,tags=("event",)),
    BackItem("event_fauna:deric","Arctic-Blast Scales","Your mech's back is covered with massive metal scales. When activated, the edges glow ice blue, they lift up, and a frozen wind gushes out. With condensation, you can release a hail of ice shards. You can also curl up in a spiny frostball.",stars=3,tags=("event",)),
    LegsItem("event_fauna:blueberry","Poisonous Barbs","While poison may not be much use on an opponent's mech, they still are a very fashionable accessory for everyone who likes platypi.",stars=3,tags=("event",)),
    BackItem("event_fauna:bogle","Rickety Roost","A rickety tower anchored to the back of your mech ripe with antennae and caked in guano. Once an array of scientific instruments, it's now home to your pigeons.",stars=3,tags=("event",)),
    BodyItem("event_fauna:zapterra","Extremophile","Extreme resistance to temperature (.05K-150C), pressure (40,000 kPa), sudden impacts (1.14 GPa), and radiation. Capable of making automatic repairs to wiring with access to water, able to survive in a dehydrated state for 30+ years. Can copy opponent resistances if it gets a taste.",stars=3,tags=("event",)),
])




starting_inventory = ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body"]




body_plans = [
BodyPlanItem("ratoon:bipedal","Standard Bipedal","",{"legs": 2, "arms": 2, "power": 1}),
]




# all_mechs = (syl, intoamutecrypt, metanite64, bee, oneirocartographer, triangle, cadence, vel, hillexed, cheshire, loading, styietus, deric)


ratoon_pullable_mechs = (bee, oneirocartographer, hillexed, styietus, triangle, cheshire, loading, metanite64, deric, syl, vel, amutecrypt, intergalacticsky, renne, moonbug, cheesesnack, spellweaver, bytes, thecowofeternalflame, p_rker, shork, ditto, hal2000, turtlelover2244, zweihawke, colabot, loftyinclination, shade, babaloga, theoddman, only, chillychilichelle, chimera, homeslice, shieldcaptain, n217, nevephoenix, zapterra, urirles, jcterran)

event_mechs = (event_formal, event_fauna, )
event_gift_mech = event_fauna
all_mechs = ratoon_pullable_mechs + (alto, nullified, ) + event_mechs




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

def merge_gatcha_tables(mech_names):
    loot = []

    for mech in all_mechs:
        if mech.username.lower() in mech_names:
            loot.extend(mech.loot)

    return Mech("random", loot)

def check_gacha_table():
    for mech in all_mechs:
        #print(mech.loot)
        pass

if __name__ == "__main__":
    check_gacha_table()
