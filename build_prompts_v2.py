#!/usr/bin/env python3
"""V2 prompts with strict OEM accuracy + negative phrasing.

Strategy: focus on the 3 priority angles (front, side, interior) for any car
that's missing them; then back-fill rear/wheels if budget allows.
"""
import json
from pathlib import Path

TARGET_DIR = Path("/home/user/workspace/gita-v2/images")

# Tightly-worded model specs that lock to the OEM. Critical: each entry calls
# out distinguishing details + negative cues to keep the renderer honest.
CARS = {
    "mercedes-g63-amg": {
        "spec": "2025 Mercedes-AMG G63 W463 facelift, twin-turbo V8, AMG Panamericana vertical-slat chrome grille (NOT regular G-Wagen grille), round LED headlights with integrated DRL ring, squared-off boxy SUV body with widened AMG flared fender arches, side-exit quad chrome exhaust tips, AMG body kit",
        "color": "obsidian black matte exterior, 22-inch AMG cross-spoke gloss-black forged alloy wheels",
        "interior": "AMG-specific Nappa leather diamond-quilted seats, AMG steering wheel with red 12 o'clock marker, dual 12.3-inch widescreen displays, AMG performance pedals, carbon-fiber trim",
        "negative": "NOT a Mercedes G500, NOT a regular G-Class, must show AMG Panamericana vertical-slat grille",
    },
    "mercedes-gls-450d": {
        "spec": "2025 Mercedes-Benz GLS 450d 4MATIC X167 facelift, full-size three-row luxury SUV (NOT the smaller GLE, NOT G-Class), AMG Line exterior, massive upright chrome grille with vertical Mercedes star pattern, multibeam LED headlights, smooth flowing SUV silhouette, chrome window surrounds",
        "color": "obsidian black metallic, 21-inch AMG twin five-spoke alloy wheels",
        "interior": "Nappa leather captain seats, two 12.3-inch MBUX widescreens, open-pore wood trim, ambient lighting strips",
        "negative": "NOT a G-Class boxy SUV, NOT a GLE coupe, must be the long three-row full-size GLS",
    },
    "mercedes-g580-eq": {
        "spec": "2025 Mercedes-Benz G580 with EQ Technology W465 electric G-Class, fully electric (NO exhaust pipe anywhere), CLOSED solid front grille panel with illuminated star pattern (NOT slatted AMG grille), boxy square G-Wagen silhouette, horizontal battery-pack strip along lower body sills, rear-mounted spare-wheel cover with EQ-specific aero disc",
        "color": "alpine grey magno matte finish, 20-inch EV-specific aero five-spoke alloy wheels",
        "interior": "G-Class square dashboard with off-road grab handle, dual digital screens, EQ-specific blue ambient lighting, Nappa leather seats",
        "negative": "NOT a G63 AMG, NOT an internal-combustion G-Wagen, NO exhaust pipes, must show closed EV grille and battery sill",
    },
    "lucid-air-pure": {
        "spec": "2025 Lucid Air Pure all-electric luxury sedan, low-slung four-door fastback silhouette, distinctive Lucid full-width micro-LED light bar spanning entire front fascia (NO nose-cone), short hood, glass-canopy roof, frameless flush door handles, slim aerodynamic mirrors",
        "color": "stellar white pearlescent paint, 19-inch Aero Range turbine alloy wheels",
        "interior": "minimalist Lucid cockpit with curved 34-inch glass cockpit display, lower secondary touchscreen, Mojave PurLuxe vegan leather seats, blonde wood trim",
        "negative": "NOT a Tesla Model S (no Tesla nose-cone), NOT a Mercedes EQS, must show Lucid's signature full-width LED light bar",
    },
    "mercedes-g500": {
        "spec": "2024 Mercedes-Benz G500 W463 standard non-AMG G-Class, classic three-vertical-slat chrome grille (NOT AMG Panamericana grille), round LED headlights, boxy square SUV silhouette, narrower fender flares than AMG, side-mounted single chrome exhaust",
        "color": "designo manufaktur olive green metallic, 19-inch five-spoke alloy wheels",
        "interior": "Nappa leather seats, dual 12.3-inch widescreen displays, square G-specific dashboard, off-road grab handle on passenger side",
        "negative": "NOT a G63 AMG, NO Panamericana vertical-slat grille, NO widened AMG flares, must be the cleaner standard G500",
    },
    "chevy-tahoe-high-country": {
        "spec": "2025 Chevrolet Tahoe High Country full-size three-row body-on-frame SUV, bold horizontal chrome bar across grille, Chevrolet bowtie center emblem, large LED dual headlamps with vertical C-shape DRL signature, chrome window surrounds, body-color rocker panels, High Country exclusive chrome trim",
        "color": "black metallic, 22-inch polished chrome multi-spoke alloy wheels",
        "interior": "premium leather captain chairs with perforation, 17.7-inch infotainment touchscreen, 11-inch driver display, real wood trim, head-up display",
        "negative": "NOT a Suburban (Tahoe is the shorter wheelbase), NOT a Silverado pickup truck",
    },
    "bmw-x7-xdrive40i": {
        "spec": "2025 BMW X7 xDrive40i G07 LCI facelift, full-size three-row luxury SUV, BMW's split-headlight design (slim upper DRL strip + lower main beam unit), tall vertical illuminated dual-kidney grille with Iconic Glow chrome surround, M Sport exterior package",
        "color": "carbon black metallic, 22-inch M Aerodynamic Y-spoke alloy wheels",
        "interior": "BMW Curved Display (12.3-inch driver + 14.9-inch infotainment as one panel), Merino leather captain chairs, crystal glass iDrive controller, ambient lighting",
        "negative": "NOT a BMW X5 (X7 is bigger with three rows), NOT an iX EV, must show split-headlight + tall illuminated kidney grille",
    },
    "tesla-model-x-lr": {
        "spec": "2024 Tesla Model X Long Range, mid-size luxury SUV with signature falcon-wing rear doors (must be visible, ideally one open or hinged position), smooth aerodynamic silhouette, NO traditional grille at all (smooth body-color front), full-width slim LED light bar across nose, flush door handles",
        "color": "midnight silver metallic, 22-inch turbine alloy wheels",
        "interior": "minimalist Tesla cabin with yoke steering control, 17-inch landscape center touchscreen, second 8-inch rear display, white vegan leather, panoramic glass roof",
        "negative": "NOT a Model Y (Model X has falcon-wing rear doors), NOT a Model S sedan, must show falcon-wing doors and smooth grille-less front",
    },
    "mercedes-s580e": {
        "spec": "2025 Mercedes-Benz S580e plug-in hybrid W223 flagship sedan, long elegant four-door luxury sedan silhouette (NOT an SUV), Mercedes Digital Light LED headlamps with star-pattern projection, tall upright chrome grille with three-pointed star emblem center, chrome window surrounds, smooth flowing body lines",
        "color": "selenite grey magno metallic, 20-inch AMG multi-spoke alloy wheels",
        "interior": "executive rear seats with reclining business-class layout, Burmester 4D speakers, 12.8-inch portrait OLED center screen, Nappa leather, open-pore wood",
        "negative": "NOT a GLS SUV, NOT a C-Class, must be the long full-size S-Class flagship sedan",
    },
    "ford-bronco-raptor": {
        "spec": "2025 Ford Bronco Raptor 4-door boxy SUV (NOT a pickup truck), wide-body fender flares with exposed bolts, blacked-out FORD lettering across grille with amber LED marker lights, off-road bumper with integrated LED light pods, raised suspension stance, removable hard-top roof, retro-modern boxy SUV silhouette",
        "color": "code orange exterior, 37-inch BFGoodrich KO2 all-terrain tires on matte-black beadlock-style off-road wheels",
        "interior": "marine-grade vinyl seats with orange contrast stitching, off-road grab handles, 12-inch SYNC 4 touchscreen, rubberized floor",
        "negative": "NOT an F-150 pickup truck (Bronco is an SUV with no truck bed), NOT a Bronco Sport (smaller crossover)",
    },
    "ford-f150-raptor": {
        "spec": "2025 Ford F-150 Raptor R full-size four-door pickup truck (HAS a visible truck bed at rear), massive blacked-out grille with amber LED marker lights and bold FORD lettering, aggressive vented hood scoop, widened fender flares, dual exhaust outlets, raised off-road suspension",
        "color": "agate black metallic, 37-inch BFGoodrich KO2 all-terrain tires on matte-black off-road alloy wheels",
        "interior": "Recaro sport bucket seats with orange accents, 12-inch SYNC 4 touchscreen, carbon-fiber trim, off-road dial selector",
        "negative": "NOT a Bronco SUV (F-150 must have a truck bed), NOT a regular F-150, must show widened Raptor fender flares and amber marker lights",
    },
    "mercedes-gle-450d": {
        "spec": "2025 Mercedes-Benz GLE 450d 4MATIC W167 mid-size SUV, AMG Line exterior, large diamond-pattern chrome grille, multibeam LED headlights, smooth two-row mid-size SUV silhouette (NOT the larger three-row GLS, NOT the boxy G-Class)",
        "color": "polar white, 21-inch AMG five-twin-spoke alloy wheels",
        "interior": "Nappa leather seats, dual 12.3-inch MBUX widescreens, open-pore wood trim, panoramic sunroof",
        "negative": "NOT a GLS (smaller, two rows), NOT a G-Class boxy SUV, NOT a GLC (GLE is bigger)",
    },
    "tesla-cybertruck-awd": {
        "spec": "2024 Tesla Cybertruck AWD, brushed stainless-steel exoskeleton body (NO paint), angular faceted pentagon-shaped silhouette, NO curves anywhere, single full-width LED light bar across front, single full-width LED bar across rear, NO traditional door handles, NO chrome trim, integrated tonneau cover over rear bed, sharp triangular A-pillar",
        "color": "raw brushed stainless steel finish, 20-inch dark cyber wheels with all-terrain tires",
        "interior": "minimalist square steering yoke, 18.5-inch center landscape touchscreen, 9.4-inch rear screen, vegan leather bench seats, white interior accents, exposed metal door panels",
        "negative": "NOT a concept truck, NOT a Rivian, NOT an F-150, MUST show stainless steel angular pentagon body with full-width LED bars and no door handles",
    },
    "bmw-x5-xdrive40i": {
        "spec": "2025 BMW X5 xDrive40i G05 LCI facelift, mid-size five-seat SUV (NOT the larger three-row X7), M Sport exterior package, traditional dual-kidney grille (NOT the oversized iX grille, NOT the X7's tall illuminated grille), slim adaptive laser-LED headlights with hexagonal DRL signature, sloping rear roofline",
        "color": "phytonic blue metallic, 21-inch M Y-spoke alloy wheels",
        "interior": "BMW Curved Display 12.3+14.9 inch panel, vernasca leather sport seats, crystal-glass iDrive controller, ambient lighting",
        "negative": "NOT an X7 (X5 has only two rows), NOT an iX EV, must show traditional dual-kidney grille not the illuminated tall one",
    },
    "ford-bronco-big-bend": {
        "spec": "2024 Ford Bronco Big Bend 4-door SUV sixth generation, standard-width (NOT wide-body Raptor), boxy retro-modern SUV silhouette, round LED headlights flanking large white FORD lettering across the grille (NOT blacked-out), narrower standard fender flares, removable doors and roof visible",
        "color": "area 51 light blue exterior, 17-inch grey-painted aluminum wheels with standard all-terrain tires",
        "interior": "cloth seats with marine-grade vinyl, 8-inch SYNC 4 touchscreen, rubberized floor, off-road grab handles",
        "negative": "NOT a Bronco Raptor (Big Bend has standard-width flares), NOT a Bronco Sport (smaller crossover), NOT an F-150",
    },
    "mustang-gt-v8": {
        "spec": "2025 Ford Mustang GT V8 coupe S650 seventh generation, long hood and short rear deck (classic American muscle proportions), tri-bar LED headlamps, twin hood scoop bulges, GT-specific lower front splitter, dual rear exhaust outlets, fastback coupe silhouette",
        "color": "race red exterior, 19-inch dark-painted machined-face Y-spoke alloy wheels",
        "interior": "Recaro bucket seats, dual digital displays (12.4-inch driver + 13.2-inch infotainment) angled toward driver, flat-bottom steering wheel, aluminum pedals",
        "negative": "NOT a Camaro, NOT a Challenger, must be the long-hood Mustang coupe with tri-bar LED headlamps",
    },
    "kia-ev9-rwd": {
        "spec": "2025 Kia EV9 RWD all-electric three-row SUV, upright boxy boxy EV-specific silhouette, distinctive vertical Star Map LED daytime running lights at front and rear corners (Kia's pixel-LED signature), closed EV-specific front fascia (NOT tiger-nose grille), flush door handles",
        "color": "ocean matte blue exterior, 20-inch aero alloy wheels",
        "interior": "two 12.3-inch curved displays as one panel, vegan leather seats with relaxation mode, sustainable recycled materials, ambient lighting",
        "negative": "NOT a Kia Telluride (Telluride has tiger-nose grille and ICE engine), NOT a Sportage, must show closed EV fascia and vertical pixel LED signature",
    },
    "rivian-r1s-dual": {
        "spec": "2025 Rivian R1S Dual Motor all-electric three-row SUV (NOT a pickup truck), signature oval stadium-light vertical LED headlamps connected by full-width horizontal LED light bar across the front, clean smooth body panels with no chrome, boxy upright SUV silhouette",
        "color": "limestone green metallic, 21-inch Sport dark machined-face alloy wheels",
        "interior": "Rivian-specific minimalist cabin, 15.6-inch landscape touchscreen, 12.3-inch driver display, vegan leather seats, sustainable wood trim",
        "negative": "NOT a Rivian R1T pickup (R1S is an SUV with no truck bed), NOT a Ford Bronco, must show signature oval stadium-light headlamps and full-width LED bar",
    },
    "jeep-wrangler-sport": {
        "spec": "2024 Jeep Wrangler Sport 4-door Unlimited JL generation, classic Jeep seven-vertical-slot grille (NOT a Bronco-style grille), round LED headlights, flat squared fender flares with exposed wheel arches, removable hard-top roof, exposed door hinges, foldable windshield, body-on-frame boxy SUV silhouette",
        "color": "firecracker red exterior, 17-inch black-painted steel wheels with off-road all-terrain tires",
        "interior": "rugged cloth seats with washable surfaces, vertical 7-inch touchscreen, exposed Allen screws on dashboard, manual transmission shifter, grab handles",
        "negative": "NOT a Ford Bronco (Wrangler has seven-slot grille), NOT a Gladiator pickup, must show seven-slot grille and exposed door hinges",
    },
    "chevy-traverse-z71": {
        "spec": "2025 Chevrolet Traverse Z71 three-row mid-size SUV third generation, rugged off-road-styled SUV (NOT a Tahoe full-size, NOT a Suburban), squared-off front fascia with Z71 dark-finish grille and red Z71 badging, integrated skid plates, dark machined alloy wheels, slim LED headlights with Chevy bowtie emblem",
        "color": "harvest bronze metallic, 18-inch dark machined-finish alloy wheels with all-terrain tires",
        "interior": "Z71-specific cloth and leatherette seats with red contrast stitching, 17.7-inch infotainment touchscreen, 11-inch driver display, rugged rubber floor mats",
        "negative": "NOT a Tahoe (Traverse is unibody crossover not body-on-frame full-size), NOT a Suburban, must show Z71 dark trim and skid plates",
    },
}

ANGLE_DESC = {
    "front":    "front three-quarter view at eye level, camera offset 30 degrees, full front fascia visible including grille, headlamps, hood and bumper",
    "rear":     "rear three-quarter view at eye level, camera offset 30 degrees, taillights, tailgate or trunk, rear bumper and any exhaust outlets clearly visible",
    "interior": "interior cockpit photograph from the driver-door perspective, dashboard and steering wheel filling frame, instrument cluster and infotainment screen clearly visible, soft cabin lighting",
    "wheels":   "extreme close-up macro photograph of one front wheel and tire only, factory wheel design centered, brake caliper behind spokes, tire sidewall lettering visible, shallow depth of field, body of vehicle blurred in background",
    "side":     "pure side profile shot from exactly 90 degrees, complete vehicle silhouette filling frame, all doors and proportions visible, no perspective distortion",
}

BACKDROP = "premium cobalt-blue gradient studio backdrop, deep navy floor with soft reflection, photorealistic 8K editorial automotive photography, cinematic studio lighting with rim light on body panels"

NEGATIVE_GLOBAL = "no people, no text on the image, no watermarks, no logos overlays from any third party, no other car models in frame, OEM-correct details mandatory, no concept-car interpretations, no designer liberties, photographic accuracy mandatory"

# Priority angles
PRIORITY = ["front", "side", "interior"]
SECONDARY = ["rear", "wheels"]

manifest = []
for slug, info in CARS.items():
    for angle in PRIORITY + SECONDARY:
        adesc = ANGLE_DESC[angle]
        if angle == "interior":
            body = f"{info['spec']}. {info['interior']}. {adesc}."
        elif angle == "wheels":
            body = f"{info['spec']}, {info['color']}. {adesc}."
        else:
            body = f"{info['spec']}, {info['color']}. {adesc}."
        prompt = f"{body} {BACKDROP}. {NEGATIVE_GLOBAL}. {info['negative']}."
        manifest.append({
            "slug": slug,
            "angle": angle,
            "priority": angle in PRIORITY,
            "filename": f"{slug}-{angle}",
            "prompt": prompt,
        })

# Mark which ones already exist with reasonable size
existing = {p.stem: p for p in TARGET_DIR.glob("*.png")}
for item in manifest:
    fn = item["filename"]
    item["exists"] = fn in existing and existing[fn].stat().st_size > 50000

with open("/home/user/workspace/gita-v2/prompts_manifest_v2.json", "w") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

todo_priority = [m for m in manifest if m["priority"] and not m["exists"]]
todo_secondary = [m for m in manifest if not m["priority"] and not m["exists"]]
done = [m for m in manifest if m["exists"]]
print(f"Total: {len(manifest)} | Done: {len(done)} | Priority TODO: {len(todo_priority)} | Secondary TODO: {len(todo_secondary)}")
