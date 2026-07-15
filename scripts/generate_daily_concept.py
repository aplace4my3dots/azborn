#!/usr/bin/env python3
"""
E-RUN Magazine — Automated Daily Concept & Caption Generator
Combines speculative physics, bio-mimicry, quantum materials, and avant-garde tailoring
to generate brand new, never-before-seen creative concepts every day.
"""

import os
import json
import random
from datetime import datetime

# Novel Biomaterials & Speculative Physics Matrix
AESTHETIC_THEMES = [
    {
        "title": "Acoustic Levitation & Liquid Mercury Couture",
        "header_color": "Pristine White (#FFFFFF)",
        "subject": "An avant-garde model wearing a tailored high-neck matte black silk evening gown with sharp architectural shoulders",
        "setting": "inside an ultra-clean charcoal anechoic sound chamber lined with acoustic foam wedges",
        "material_science": "orbiting gracefully around the gown are polished spheres of liquid silver mercury, suspended in mid-air by acoustic levitation sound waves that refract the studio strobe lights",
        "hook": "When sound waves sculpt liquid metal around the human silhouette. 🔊🫧",
        "story": "In E-RUN Issue 31, we eliminate the need for physical stitching. By modulating 40kHz acoustic levitation frequencies inside anechoic chambers, our styling team achieved what was previously thought impossible: suspending 84 discrete spheres of liquid silver mercury in mid-air orbits around our model's torso. When the frequency shifts, the liquid metal merges into a fluid metallic breastplate before dispersing back into orbital droplets.",
        "cta": "If you could wear a garment made of levitating liquid drops governed by sound waves, what song or frequency would you play to shape your dress? 🎶👇",
        "hashtags": "#ERUNMagazine #AcousticLevitation #LiquidMercury #FuturisticFashion #PhysicsFashion #AvantGardeTailoring #NextGenCouture #Midjourney6 #AIEditorial #HighTechHauteCouture #SoundDesign #SovereignStyle"
    },
    {
        "title": "Chitinous Aerogel & Bioluminescent Silk-Moth Dynasty",
        "header_color": "Classic White Serif (#FFFFFF)",
        "subject": "A majestic model wearing a full-length layered coat constructed from spun bioluminescent golden silk fibers and translucent aerogel fabric that glows softly like mist",
        "setting": "inside a misty botanical research conservatory at twilight with golden light filtering through high glass ceilings",
        "material_science": "featuring a sculptural high collar inspired by the natural chitin scales of giant silk-moths and delicate feathery moth antennae brow filigree",
        "hook": "Engineered from living golden silk and weightless aerogel: the Silk-Moth Dynasty. 🦋✨",
        "story": "For E-RUN Issue 32: Bio-Mimicry, we look to nature's most sophisticated architects: the Saturniidae silk-moth family. By harvesting genetically enhanced bioluminescent golden silk and fusing it with ultra-lightweight silica aerogel (a material 99.8% composed of air), our research atelier crafted an oversized coat that weighs under 40 grams yet provides absolute thermal insulation. To wear aerogel is to wear frozen fog.",
        "cta": "Would you wear an ultra-lightweight coat made of golden aerogel and glowing moth silk during winter? Drop a ✨ or 🦋 below!",
        "hashtags": "#ERUNMagazine #BioMimicry #AerogelFashion #SilkMothCouture #Bioluminescence #EcoLuxury #Xenobotany #SpeculativeDesign #FuturisticOuterwear #AIPrompting #HighFashionMagazine #Dreamscape"
    },
    {
        "title": "Electrostatic Ionization & Wearable Tesla Coils",
        "header_color": "Electric Cyan (#00FFCC)",
        "subject": "A model wearing a structured high-neck carbon-fiber trench coat embedded with vacuum glass tubes and polished copper conductive coils",
        "setting": "standing inside a dark industrial electrostatic observatory during a high-voltage thunderstorm",
        "material_science": "miniature purple and cyan electrical plasma tendrils and static lightning coils safely crackle across the copper tubes around the coat's silhouette",
        "hook": "Harnessing 50,000 volts of pure atmospheric static inside structured carbon fiber. ⚡🏙️",
        "story": "Welcome to E-RUN Issue 33: High Voltage. Why protect yourself from the storm when your outerwear can feed on its energy? Utilizing miniature localized Faraday shielding combined with copper-wound vacuum tubes, this modular trench coat channels atmospheric ionization into a glowing, crackling aura of violet plasma. The wearer doesn't just survive the elements—she commands the current.",
        "cta": "Tag someone whose creative energy is pure high-voltage electricity! ⚡💥",
        "hashtags": "#ERUNMagazine #TeslaCouture #HighVoltageFashion #TechwearLuxury #CyberpunkAesthetic #StaticElectricity #CarbonFiberFashion #FuturisticOuterwear #AIArtCommunity #NeoBrutalist #StormStyle #NextGenPower"
    },
    {
        "title": "Ferrofluid Magnetic Sculpture & Obsidian Velvet",
        "header_color": "Obsidian Grey (#1A1A1A)",
        "subject": "An avant-garde model wearing an elegant obsidian-black velvet column dress with magnetic induction copper thread embroidery",
        "setting": "inside a minimalist concrete laboratory with magnetic field generators reflecting off polished basalt floors",
        "material_science": "flowing around her neckline and wrists are dynamic, spiky geometric sculptures formed from living black ferrofluid that react instantaneously to hidden electromagnetic fields",
        "hook": "When magnetic fields turn liquid iron into razor-sharp geometric sculpture. 🧲⚫",
        "story": "In E-RUN Issue 34: Magnetic Alchemy, we explore ferrofluidics as the ultimate dynamic accessory. Composed of nanoscale ferromagnetic particles suspended in organic carrier oil, this liquid metal morphs from smooth ribbons into dramatic, spiky architectural crowns the exact second our hidden magnetic coils activate. Your neckline adapts from soft evening elegance to formidable spikes at the flick of a switch.",
        "cta": "If your jewelry morphed its shape based on magnetic fields around you, would you prefer **Fluid Ribbons** or **Sharp Spikes**? 🧲💬",
        "hashtags": "#ERUNMagazine #FerrofluidFashion #MagneticCouture #ObsidianVelvet #DarkLuxury #FuturisticJewelry #AvantGardeStyle #PhysicsInFashion #NextGenCouture #AIPhotography #HighSocietyGoth #DynamicApparel"
    },
    {
        "title": "Chronolithic Amber & Preserved Botanical Gowns",
        "header_color": "Saffron Yellow (#FFD700)",
        "subject": "A model wearing a breathtaking strapless gown constructed from flexible, crystal-clear resin and fossilized golden amber panels",
        "setting": "inside a sun-drenched architectural atrium where golden hour sunlight refracts through ancient geological rock formations",
        "material_science": "encased inside the translucent amber panels of the dress are perfectly preserved delicate alien orchids and glowing golden spores trapped in time",
        "hook": "Captured inside geological amber for 10,000 years: the Chronolithic Gown. ⏳🌼",
        "story": "Why let ephemeral beauty fade when it can be preserved across millennia? For E-RUN Issue 35: Deep Time, our botanical jewelers mastered flexible bio-resin synthesis to recreate the fossilizing properties of ancient tree amber. The rare xenobotanical orchids trapped inside the bodice of this gown will remain pristine for centuries—turning the wearer into a walking geological archive of beauty.",
        "cta": "What flower or memory would you want preserved inside a translucent amber gown for eternity? 🌼⌛",
        "hashtags": "#ERUNMagazine #ChronolithicFashion #AmberCouture #BotanicalPreservation #HighFashionArt #ResinDress #Xenobotany #LuxuryEditorial #GeologicalStyle #AIArt #VogueFuturism #EternalElegance"
    }
]

def generate_concept(target_date_str=None):
    if not target_date_str:
        target_date_str = datetime.now().strftime("%Y-%m-%d")
        
    # Select or rotate concept based on day of year
    day_of_year = datetime.strptime(target_date_str, "%Y-%m-%d").timetuple().tm_yday
    theme = AESTHETIC_THEMES[day_of_year % len(AESTHETIC_THEMES)]
    
    prompt = f"Groundbreaking high-fashion magazine cover photography for E-RUN Magazine. {theme['subject']} standing {theme['setting']}. Surrounding her and her outfit, {theme['material_science']}. Crisp header masthead text 'E-RUN' across the top in {theme['header_color']}. Shot on Hasselblad H6D-100c medium format, hyper-detailed skin and fabric textures, speculative physics and luxury avant-garde fashion aesthetic --ar 4:5 --style raw --v 6.1"
    
    caption_text = f"""{theme['hook']}

{theme['story']}

{theme['cta']}

{theme['hashtags']}"""

    output = {
        "date": target_date_str,
        "title": theme["title"],
        "prompt": prompt,
        "caption": caption_text,
        "header_color": theme["header_color"]
    }
    
    # Save files for downstream automation
    os.makedirs("captions", exist_ok=True)
    json_path = f"captions/{target_date_str}.json"
    txt_path = f"captions/{target_date_str}.txt"
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
        
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(caption_text)
        
    print(f"✅ Generated Daily E-RUN Concept for {target_date_str}: {theme['title']}")
    print(f"📝 Prompt saved to {json_path}")
    print(f"💬 Caption saved to {txt_path}")
    return output

if __name__ == "__main__":
    generate_concept()
