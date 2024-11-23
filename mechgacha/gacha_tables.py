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
    PowerItem("bee:supernova_drive","Supernova Drive","A core of swirling energy, the captured explosion of a star, held together with the force of dark matter. Iridescent and an unstoppable force.", stars=5)
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
    Item("oneirocartographer:diffractive_heliograpb","Diffractive Heliograph","A reflective lattice of metal used for long-range visual signaling."),
    CockpitItem("oneirocartographer:dendritic_interface","Dendritic Interface","The cockpit has been overgrown with roots and branches, shaping themselves around the pilot's movements.", stars=3),
    WeaponItem("oneirocartographer:manipulator_assembly_tier_2","Manipulator Assembly","A pair of mismatched claw-grippers; one large and sturdy, the other small and meant for delicate work. Each arm now unfolds into several grippers in an array of sizes and materials. A practiced pilot can use these to pick up nearly anything without damaging it.", stars=5)
]
)


hillexed = Mech("hillexed", 
[
    PowerItem("hillexed:antimatter_tea","Antimatter tea","A transparent container of hot antibeverage! A steel handle attached to glass lets you see the powerful magnets within. Drink it to unlock the vast wellspring of energy inside your mouth!"),
    LegsItem("hillexed:teeny_mechanized_legs","Teeny mechanized legs","Someone wasn't clear about millimeters versus meters. It looks like someone turned a robotic arm upside-down, full of joints and motors. That can't possibly be a baby shoe on the end, can it?", stars=2),
    ArmsItem("hillexed:neutron_star_on_a_stick","Neutron Star on a Stick","The ultimate fishing rod. Cast the line to throw the white-hot neutron star towards something you want to grab, and once gravity sticks the two together, reel it in. If you're really good, you can set up an orbit!"),
    BodyItem("hillexed:parabolic_block","Parabolic Block","A pancake-shaped glass cylinder set on edge with attachment points for other mecha parts spaced across the outer rim. The mecha's internals are visible through the sides; made of glass, it is more window than not. Built into one side is a concave depression, a ginormous curved parabolic dish with a smooth mirror finish. Three thin trusses reach forwards from the dish to hold something steady at its focal point. The focal point concentrates light and energy recieved from the dish, so it's the perfect place for a cockpit with advanced sensors... or a weapon that can reflect energy off the dish into a giant beam!"),
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
    Item("hillexed:cassegrain_style_parabolic_block","Cassegrain-Style Parabolic Block"," A drum-shaped colorful hollow tube on its side, with attachment points for other mecha parts spaced across the outer rim. The front circular surface is mostly open, with three thin truss struts reaching out from the edge to support a small platform in its center. The back circular surface is sealed off, except for a small hole in the center. Almost everything in the tube's inside is reflective, bouncing light that enters back and forth until it enters the back small hole, which is the focal point. The focal point concentrates light and energy recieved from the tube, so it's the perfect place for a cockpit with advanced sensors... or a weapon that can reflect energy through the tube into a giant beam!      This parabolic block bounces light multiple times, packing a longer focal length into a smaller mecha form.  Perfect for spreading out energy weapons into incredibly zoomed-in beams of mass destruction.", stars=5),

])

styietus = Mech("St. Yietus",
[
    PowerItem("st_yietus:curseheart_engine","CURSEHEART ENGINE","A grinding mass of twisted machinery, alight with horror and hope. Within its bowels, misfortune and cruelty are catalyzed into fiercest resolve. Generates additional energy for each unique debuff affecting your mech."),
    LegsItem("st_yietus:rotborn_stomper","ROTBORN STOMPER","A sturdy weatherproofed leg. Slow, but capable of brief bursts of agility. Gains charges over time which can each be spent to perform a short leap. Leaps are faster than walking and clear low obstacles and small gaps. Slightly reduces the effects of debuffs."),
    ArmsItem("st_yietus:rotborn_fist","ROTBORN FIST","A simple arm, covered in pitted armor and tipped with a large, gauntlet-like hand. Paired with a small remote manipulator for more delicate work. Whenever it is not equipped with a melee weapon, even if it is equipped with a ranged weapon, its fist counts as an equipped melee weapon. Slightly reduces the effects of debuffs."),
    BodyItem("st_yietus:melancholic_visage","MELANCHOLIC VISAGE","A bulky armored torso with a masked head. Despite its battered condition it still looks ever ahead, towards a brighter future. It's tough, has good heat capacity, and reduces the effects of debuffs."),
    CockpitItem("st_yietus:psychlink_mpi","PSYCHLINK MPI","A mysterious mask that draws closer the wills of a mech and its pilot, allowing them both to be pushed past their normal limits. Activated abilities can be used before their cooldowns end, at the cost of a large amount of heat and a longer, unskippable cooldown."),
    Item("st_yietus:external_utility_pack","EXTERNAL UTILITY PACK","An armored backpack for storing extra-bulky equipment. Improves cooling and speeds up ability cooldowns. Slightly reduces the effects of debuffs.", ["back"]),
    Item("st_yietus:slaghewn_warpick","SLAGHEWN WARPICK","A warpick crafted from industrial waste, resplendent with signs of use and repair. Not the most elegant of weapons, but its effectiveness is undeniable. Good base stats, effective against armor.", ["weapon"]),
    Item("st_yietus:titanweave_cloak","TITANWEAVE CLOAK","A massive, well-worn cloak designed to shield a mech's mechanisms from severe weather. Comes in a variety of styles and patterns.", ["cosmetic"]),
    BodyPlanItem("st_yietus:tech_terror_body_plan","TECH TERROR BODY PLAN","An intricate, skeletal body plan that allows up to four arms or up to two weapons to be equipped instead of a body. Use at your own risk.", {"arms": 4}),
    BodyPlanItem("st_yietus:kitbash_kit_adaptor","KITBASH KIT ADAPTER","A set of tools and materials used to combine parts in all sorts of unintended ways. Adds one additional slot of any type other than a body to your mech.", {}), # todo: make work
    Item("st_yietus:novelty_mug","NOVELTY MUG", "A plastic novelty mug, obtained through great personal effort. The sense of pride one gets from owning this object gives you a minor all-around stat boost. Nifty!"),
    Item("st_yietus:crescent_companion","CRESCENT COMPANION", "The moon-headed ghost of a fictional being has made its home in either your mind or the systems of your mech. It grants you the ability to create a temporary aura of disruption around you that severely slows enemies' cooldowns and cooling and mildly slows yours. Just make sure to remember it so it doesn't fade away."),
    Item("st_yietus:weird_lil_guy","WEIRD LIL' GUY","A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.", ["cosmetic"]),
    PowerItem("st_yietus:divinity_tap","DIVINITY TAP","A bony, eerily pristine variant of the CURSEHEART ENGINE. Generates additional energy for each unique debuff affecting your mech. In addition, it has a toggled ability that massively improves all stats, but creates heat at an exponentially increasing rate and marks your mech with a halo that is visible to everyone while active. You feel tired after using it, but can't explain why.", stars=5),
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
    ArmsItem("triangle:arm_03","Arm: Prefix: Arm 03","Two seemingly straight-forward arms with quick-release couplers. There are pop-out handles in both the forearms and the biceps: the arms can detach/transform into weapons. The five-star versions are bulkier and feature specialized couplers at both shoulder and elbow that can clamp anywhere onto the mech's body or onto other limbs, instead of requiring a quick release housing. These arms have their own power supplies and can be operated independently of the body.", stars=5),
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
    CockpitItem("cheshire:stowaway_cheshire","Stowaway Cheshire","Yeah, you can pretend I'm a copilot or if you've got a Pacific Rim thing going on we can do that, but you need to know I'm just gonna sneak onto your mecha when you aren't looking"),  
    BodyPlanItem("cheshire:centaur","Centaur","Four legs, two arms, a power source body and a back slot.", {"legs": 4, "arms": 2}),
    BodyItem("cheshire:sigil_crusted_body","Sigil Crusted Body","What appears to be an old wooden ship or other reclaimed wood, covered in burned sigils that animate it", stars=3),
    Item("cheshire:framed_picture_of_rival","A Framed Picture of your Rival","Its just a normal, totally platonic rival relationship. This picture is just framed to make you fight them better and not because you're repressed", stars=2),
    Item("cheshire:a_bunch_of_floating_spheres","A bunch of floating spheres","Some of them glow!", ["cosmetic"], stars=3),
    ArmsItem("cheshire:crystal_arms","Crystal Arms","what look like standard mech arms have been absolutely shredded by some sort of magical crystal growing out of the inside. they don't seem to have impeded the arms functions at all", stars=4),
    PowerItem("cheshire:the_wheel","Core: The Wheel","A series of gear structures that appear to be powered by some sort of forest animal running very quickly on the center one.", stars=4),
    PowerItem("cheshire:amber_heart_tier_2","Amber Heart", "This strange, semi-translucent object is crafted in the rough approximation of an animal heart. despite being made from yellow resin and metal, it beats. The five Star version seems to be pumping black blood? ichor? sap? Mecha can use this too convert different kinds of ammo, mana, or energy between each other (Or maybe into health if that's a thing)", stars=5),
]
)

loading = Mech("loading", 
[
    PowerItem("loading:kinetic_recycler","Kinetic Recycler","A kinetic generator powered by the grounded movement of the mech"),
    LegsItem("loading:xr2","Loading's XR2","Long double jointed legs that give the mech a low crouching position while stationary, but a long stride"),
    ArmsItem("loading:knuckle_draggers","Knuckle Draggers","Long and delicate arms twice as long as the torso it is attached to"),
    BodyItem("loading:elongated_segment_frame","Elongated Segment Frame","Thin segmented spine that allows for maximum flexibility and aerodynamics"),
    CockpitItem("loading:gyrobomber","Gyrobomber","A gyroscopic cockpit with 300 degrees of visibility to allow for the stabilization of the cockpit even as the body contorts."),
    Item("loading:big_jacket","Big Jacket","A jacket that is two sizes too large. It flows in the wind, increasing evasion the more the mech moves.", ["back", "cosmetic"]),
    Item("loading:hook_lash","Hook Lash","A lash that looks not unlike the skyhook from Bioshock. it applies a random debuff on hit", ["weapon"]),
    Item("loading:big_mechs_jacket","Big Mechs Jacket","A long flowing jacket based on the Mechs bomber jacket that flows behind the mech as it moves obscuring the body. It increases evasion the more the mech moves.", ["back", "cosmetic"], stars=5),
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
    BodyItem("vel:bipedal_frame", "Bipedal Frame","a human-like core (proportions may vary) with advanced sensors near the head or on it."),
    CockpitItem("vel:external_cockpit", "External Cockpit","outside cockpit? it has some periscopes/small windows as a backup."),
    Item("vel:booster_backpack", "Booster Backpack","A backpack with one or two massive boosters with added drop tanks and some light equipment to like change the fuel cell, and ammo/technical equipment/jamming equipment.", ["back"]),
    Item("vel:retractible_swords", "Retractible Swords", "a long carbine (think SVD or FRF-1), knife(ves)/retractible swords with the handle tucked in the forearms, plus countermeasures/stun launchers in the limbs.", ["weapon"]),
    Item("vel:pilot_emblem", "Pilot Emblem", "A big pilot emblem on a shoulder/skirt/side of the bust with a 2-3 colored paint scheme.", ["cosmetic"]),
    BodyItem("vel:durability_frame", "Durability Frame","This form is all about utility and durability on the ground and is therefore equipped with additionnal protection plates (from a different color), bigger fatter limbs and a backpack that takes a lot of drilling and mining and machining equipment (or mounts artillery). It still retains the sensor-heavy head/upper torso (though now with a helmet) and general equipment, just with thrusters replaced with like added hardpoints, protection and ground mobility (threads, crampons, hovercraft, etc)."),
    Item("vel:ace_custom_frame", "Ace Custom Frame","This mech is a special personal unit of a famous ace/freedom fighter that's fighting for the betterment of humanity, it's based from a standard military/industrial unit, but was heavily modified and customized to fit a more exploration, reconaissance, sharpshooting role.", stars=5),
]
)

amutecrypt = Mech("amutecrypt", 
[
    PowerItem("amutecrypt:new_killer_star","New Killer Star","A caged sun, kept behind some thick shielding."),
    LegsItem("amutecrypt:the_awesome_foursome","The Awesome Foursome","4 heavy, industrial legs, designed for defence and redundancy."),
    ArmsItem("amutecrypt:i_thought_about_the_army","I Thought About The Arm-y","Two industrial robotic arms."),
    BodyItem("amutecrypt:the_part_formerly_known_as","! (The Part Formerly Known As)","A stout core with the arms mounted high up, like Atlas from Portal."),
    CockpitItem("amutecrypt:okayish_computer","Okayish Computer","An AMD CPU hanging like a pair of fluffy dice would."),
    Item("amutecrypt:thrill_the_dj","Thrill The DJ","a big set of speakers", ["back"]),
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
    LegsItem("alto:unremarkable_legs","Unremarkable Legs","These hydraulic mecha legs are well maintained but otherwise unremarkable. They are ready for painting, aftermarket tinkering, or full replacement. "),
    ArmsItem("alto:unremarkable_arms","Unremarkable Arms","These hydraulic mecha arms are well maintained but otherwise unremarkable. They are ready for painting, aftermarket tinkering, or full replacement."),
    BodyItem("alto:unremarkable_body","Unremarkable Body","This hydraulic mecha body is well maintained but otherwise unremarkable. It is ready for painting, aftermarket tinkering, or full replacement. "),
    BodyPlanItem("alto:light_mecha","Light Mecha","This Blueprint was given to Alto from the original Polkadot. It seems to be plans for an ultralight mobile suit consisting of only a powersource, a weapon, and a back mounted accessory. It's almost more honest to call it power armor than a proper mecha", {"weapon": 1, "power":1, "back":1}, stars=5),
]
)

renne = Mech("renne", 
[
    PowerItem("renne:earthen_splinter","Earthen Splinter","A crystal brimming with earth-aspected arcane force. This energy regenerates gradually while the mech is dormant, but can be roused into uncontrollable bursts of magic if disturbed."),
    LegsItem("renne:tunneling_roots","Tunneling Roots","This mech has great tendrils that can support its weight as would legs, but also dig deep into the ground to provide anchoring when necessary."),
    ArmsItem("renne:plated_growth","Plated Growth","What looks like jointed arms of stone conceals a mass of large vines beneath the exterior armor. This stone exterior can be shed for greater flexibility, but at the cost of what protection it affords."),
    BodyItem("renne:the_tower","The Tower","An imposing cylindrical column upon which rests a stately head. Simple, but iconic in the oldest sense."),
    CockpitItem("renne:mystic_union","Mystic Union","Tendrils within the main cavity meld themselves to the pilot's extremities and the back of their neck, making it so they see and feel everything the mech can—and can control it as they would their body. This means they feel damage to the mech as pain, and for any mind, perception is reality..."),
    Item("renne:hanging_garden","Hanging Garden","This mech has a space on its back where life flourishes. Outside of battle, it may serve as a sanctuary, or a place to grow food.", ["back"]),
    Item("renne:hedge_clipper_turbo","Hedge Clipper Turbo","A massive pair of scissors; the individual blades can split off into dual swords, single-edged.", ["weapon"]),
    Item("renne:time_ravaged","Time-Ravaged","This mech is made of finely-chiseled stone covered in ancient artistic engravings, and much of it has been worn down by time and the elements. Parts of it are held together by plant growth that has overtaken it.", ["cosmetic"]),
    BodyPlanItem("renne:beastly_deva","Beastly Deva","This mech was built to be a master of both terrain and adaptability, meaning any relation to the human form is more coincidental than anything. Controlling it may be tricky.", {"legs":6,"arms":4}),
    CockpitItem("renne:spirit_of_the_earth","Spirit of the Earth","An embodiment of nature has taken residence inside this mech and communicates with the pilot. It does not speak human language, but long-term pilots claim to be able to understand it."),
    ArmsItem("renne:ancillary_vines","Ancillary Vines","Growing out of the mech's body, these prehensile growths may not have the greatest durability to slashing weapons, but excel at wrapping around things and tethering them."),
    Item("renne:razor_maw","Razor Maw","This mech's face bears a large snout with which it can bite enemies. Who needs weapons when you have the ideal predator body?", ["cosmetic"]),
    PowerItem("renne:caustic_engine","Caustic Engine","Some kind of bubbling acidic substance courses through this mech. How it doesn't eat through the thing is a small wonder."),
    PowerItem("renne:earthen_crystal","Earthen Crystal","A full crystal brimming with earth-aspected arcane force. This energy regenerates gradually while the mech is dormant, but can be roused into uncontrollable bursts of magic if disturbed. This crystal's size means its energy wellspring is far greater and can therefore be channeled into greater or longer-lasting effects, but the magic within **will** radiate into the pilot with continued operation due to its sheer concentration. This may have adverse or otherwise unusual effects on one's health, well-being, or biological taxonomy.", stars=5),
]
)



starting_inventory = ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body"]




body_plans = [
BodyPlanItem("ratoon:bipedal","Standard Bipedal","",{"leg": 2, "arm": 2, "power": 1}),
]




# all_mechs = (syl, intoamutecrypt, metanite64, bee, oneirocartographer, triangle, cadence, vel, hillexed, cheshire, loading, styietus, deric)

ratoon_pullable_mechs = (bee, oneirocartographer, hillexed, styietus, triangle, cheshire, loading, metanite64, deric, syl, vel, amutecrypt, intergalacticsky, renne)
all_mechs = ratoon_pullable_mechs + (alto, )


all_parts_list = {} # a dict of item id: item

# populate the parts list
for mech in all_mechs:
    for item in mech.loot:
        if item.id in all_parts_list:
            raise ValueError(f"Two items have the same ID {item.id}!")
        all_parts_list[item.id] = item

for item in body_plans:
    all_parts_list[item.id] = item

# done populating all_parts_list



# update playerdata set data='{"unlocked_mechs":["bee", "oneirocartographer", "hillexed", "styietus", "triangle", "cheshire", "loading", "metanite64", "deric", "syl", "vel", "amutecrypt", "intergalacticsky"], "ratoon_pulls": 0, "mech_pulls":1000}' where name='178116262390398976';
# update playerdata set data='{"unlocked_mechs":[], "ratoon_pulls": 1000, "mech_pulls":1000}' where name='178116262390398976';

def check_gacha_table():
    for mech in all_mechs:
        print(mech.loot)
        

if __name__ == "__main__":
    check_gacha_table()
