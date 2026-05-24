#!/usr/bin/env python3
"""V3 prompts: same OEM accuracy but PHRASED POSITIVELY only.

The safety filter seems triggered by chains of negative phrases like
"NO chrome, NO door handles, NOT a Bronco". Use positive descriptions
instead.
"""
import json
from pathlib import Path

CARS = {
    "mercedes-g63-amg": {
        "spec":  "2025 Mercedes-AMG G63 W463 generation, AMG Panamericana vertical-slat chrome grille, round LED headlights with integrated DRL ring, square boxy SUV body, AMG widened fender flares, side-exit quad chrome exhaust tips",
        "color": "obsidian black matte exterior, 22-inch AMG cross-spoke gloss-black forged alloy wheels",
        "interior": "AMG-specific diamond-quilted Nappa leather seats, AMG steering wheel with red 12 o'clock marker, dual 12.3-inch widescreen displays, AMG performance pedals, carbon-fiber trim",
    },
    "mercedes-gls-450d": {
        "spec":  "2025 Mercedes-Benz GLS 450d 4MATIC X167 facelift, full-size three-row luxury SUV, AMG Line exterior, large upright chrome grille with vertical Mercedes star pattern, multibeam LED headlights, smooth flowing SUV silhouette, chrome window surrounds",
        "color": "obsidian black metallic paint, 21-inch AMG twin five-spoke alloy wheels",
        "interior": "Nappa leather captain seats, two 12.3-inch MBUX widescreen displays, open-pore wood trim, ambient LED lighting strips",
    },
    "mercedes-g580-eq": {
        "spec":  "2025 Mercedes-Benz G580 electric G-Class W465, closed solid front grille panel with illuminated three-pointed star pattern, square boxy G-Wagen silhouette, horizontal battery-pack styling strip along lower body sills, rear-mounted spare-wheel cover with aero disc",
        "color": "alpine grey magno matte finish, 20-inch EV-specific aero five-spoke alloy wheels",
        "interior": "G-Class square dashboard with grab handle on passenger side, dual digital screens, blue ambient lighting, Nappa leather seats",
    },
    "lucid-air-pure": {
        "spec":  "2025 Lucid Air Pure electric luxury sedan, low four-door fastback silhouette, full-width micro-LED light bar spanning entire front fascia, short hood, glass-canopy roof, frameless flush door handles, slim aerodynamic mirrors",
        "color": "stellar white pearlescent paint, 19-inch Aero Range turbine alloy wheels",
        "interior": "minimalist cockpit with curved 34-inch glass cockpit display, lower secondary touchscreen, Mojave PurLuxe vegan leather seats, blonde wood trim",
    },
    "mercedes-g500": {
        "spec":  "2024 Mercedes-Benz G500 W463 standard G-Class, classic three-vertical-slat chrome grille, round LED headlights, square boxy SUV silhouette, side-mounted single chrome exhaust",
        "color": "designo manufaktur olive green metallic, 19-inch five-spoke alloy wheels",
        "interior": "Nappa leather seats, dual 12.3-inch widescreen displays, square G-specific dashboard, grab handle on passenger side",
    },
    "chevy-tahoe-high-country": {
        "spec":  "2025 Chevrolet Tahoe High Country full-size three-row body-on-frame SUV, bold horizontal chrome bar across grille with Chevrolet bowtie center emblem, large LED dual headlamps with vertical C-shape DRL signature, chrome window surrounds",
        "color": "black metallic paint, 22-inch polished chrome multi-spoke alloy wheels",
        "interior": "premium leather captain chairs with perforation, 17.7-inch infotainment touchscreen, 11-inch driver display, real wood trim",
    },
    "bmw-x7-xdrive40i": {
        "spec":  "2025 BMW X7 xDrive40i G07 LCI facelift, full-size three-row luxury SUV, BMW split-headlight design (slim upper DRL strip above lower main beam unit), tall vertical illuminated dual-kidney grille with chrome Iconic Glow surround, M Sport package",
        "color": "carbon black metallic exterior, 22-inch M Aerodynamic Y-spoke alloy wheels",
        "interior": "BMW Curved Display 12.3-inch driver plus 14.9-inch infotainment as one panel, Merino leather captain chairs, crystal-glass iDrive controller, ambient lighting",
    },
    "tesla-model-x-lr": {
        "spec":  "2024 Tesla Model X Long Range mid-size luxury SUV, signature falcon-wing rear doors clearly visible, smooth aerodynamic silhouette, smooth body-color front nose with full-width slim LED light bar, flush door handles",
        "color": "midnight silver metallic paint, 22-inch turbine alloy wheels",
        "interior": "minimalist Tesla cabin with yoke steering control, 17-inch landscape center touchscreen, second 8-inch rear display, white vegan leather, panoramic glass roof",
    },
    "mercedes-s580e": {
        "spec":  "2025 Mercedes-Benz S580e plug-in hybrid W223 flagship sedan, long elegant four-door luxury sedan silhouette, Mercedes Digital Light LED headlamps with star-pattern projection, tall upright chrome grille with three-pointed star center emblem",
        "color": "selenite grey magno metallic paint, 20-inch AMG multi-spoke alloy wheels",
        "interior": "executive rear seats with reclining business-class layout, Burmester 4D speakers, 12.8-inch portrait OLED center screen, Nappa leather, open-pore wood",
    },
    "ford-bronco-raptor": {
        "spec":  "2025 Ford Bronco Raptor 4-door boxy off-road SUV, wide-body fender flares with exposed bolts, blacked-out FORD lettering across grille with amber LED marker lights, off-road bumper with integrated LED light pods, raised suspension, removable hard-top roof",
        "color": "code orange exterior paint, 37-inch BFGoodrich KO2 all-terrain tires on matte-black beadlock-style off-road wheels",
        "interior": "marine-grade vinyl seats with orange contrast stitching, off-road grab handles, 12-inch SYNC 4 touchscreen, rubberized floor",
    },
    "ford-f150-raptor": {
        "spec":  "2025 Ford F-150 Raptor R full-size four-door pickup truck with visible truck bed at rear, massive blacked-out grille with amber LED marker lights and bold FORD lettering, aggressive vented hood scoop, widened Raptor fender flares, dual exhaust outlets, raised off-road suspension",
        "color": "agate black metallic paint, 37-inch BFGoodrich KO2 all-terrain tires on matte-black off-road alloy wheels",
        "interior": "Recaro sport bucket seats with orange accents, 12-inch SYNC 4 touchscreen, carbon-fiber trim, off-road dial selector",
    },
    "mercedes-gle-450d": {
        "spec":  "2025 Mercedes-Benz GLE 450d 4MATIC W167 mid-size two-row SUV, AMG Line exterior package, large diamond-pattern chrome grille, multibeam LED headlights, smooth SUV silhouette",
        "color": "polar white paint, 21-inch AMG five-twin-spoke alloy wheels",
        "interior": "Nappa leather seats, dual 12.3-inch MBUX widescreen displays, open-pore wood trim, panoramic sunroof",
    },
    "tesla-cybertruck-awd": {
        "spec":  "2024 Tesla Cybertruck AWD, brushed stainless-steel exoskeleton body, angular faceted pentagon-shaped silhouette, single full-width LED light bar across front, single full-width LED bar across rear, integrated tonneau cover over rear bed, sharp triangular A-pillar",
        "color": "raw brushed stainless steel finish, 20-inch dark cyber wheels with all-terrain tires",
        "interior": "minimalist square steering yoke, 18.5-inch center landscape touchscreen, 9.4-inch rear screen, vegan leather bench seats, white interior accents",
    },
    "bmw-x5-xdrive40i": {
        "spec":  "2025 BMW X5 xDrive40i G05 LCI facelift mid-size five-seat SUV, M Sport exterior package, traditional dual-kidney grille at modest size, slim adaptive laser-LED headlights with hexagonal DRL signature, sloping rear roofline",
        "color": "phytonic blue metallic paint, 21-inch M Y-spoke alloy wheels",
        "interior": "BMW Curved Display 12.3-inch driver plus 14.9-inch infotainment panel, Vernasca leather sport seats, crystal-glass iDrive controller, ambient lighting",
    },
    "ford-bronco-big-bend": {
        "spec":  "2024 Ford Bronco Big Bend 4-door SUV sixth generation, standard-width boxy retro-modern SUV silhouette, round LED headlights flanking large white FORD lettering across the grille, narrow standard fender flares, removable doors and roof",
        "color": "area 51 light blue exterior paint, 17-inch grey-painted aluminum wheels with all-terrain tires",
        "interior": "cloth seats with marine-grade vinyl, 8-inch SYNC 4 touchscreen, rubberized floor, off-road grab handles",
    },
    "mustang-gt-v8": {
        "spec":  "2025 Ford Mustang GT V8 coupe S650 seventh generation, long hood and short rear deck classic American muscle proportions, tri-bar LED headlamps, twin hood scoop bulges, GT lower front splitter, dual rear exhaust outlets, fastback coupe silhouette",
        "color": "race red exterior paint, 19-inch dark-painted machined-face Y-spoke alloy wheels",
        "interior": "Recaro bucket seats, dual digital displays 12.4-inch driver plus 13.2-inch infotainment angled toward driver, flat-bottom steering wheel, aluminum pedals",
    },
    "kia-ev9-rwd": {
        "spec":  "2025 Kia EV9 RWD electric three-row SUV, upright boxy EV silhouette, vertical Star Map LED daytime running lights at front and rear corners (pixel-LED signature), closed EV-specific front fascia, flush door handles",
        "color": "ocean matte blue exterior, 20-inch aero alloy wheels",
        "interior": "two 12.3-inch curved displays as one panel, vegan leather seats with relaxation mode, sustainable recycled materials, ambient lighting",
    },
    "rivian-r1s-dual": {
        "spec":  "2025 Rivian R1S Dual Motor electric three-row SUV, signature oval stadium-light vertical LED headlamps connected by full-width horizontal LED light bar, clean smooth body panels, boxy upright SUV silhouette",
        "color": "limestone green metallic paint, 21-inch Sport dark machined-face alloy wheels",
        "interior": "Rivian minimalist cabin, 15.6-inch landscape touchscreen, 12.3-inch driver display, vegan leather seats, sustainable wood trim",
    },
    "jeep-wrangler-sport": {
        "spec":  "2024 Jeep Wrangler Sport 4-door Unlimited JL generation, classic Jeep seven-vertical-slot grille, round LED headlights, flat squared fender flares with exposed wheel arches, removable hard-top roof, exposed door hinges, foldable windshield",
        "color": "firecracker red exterior paint, 17-inch black-painted steel wheels with off-road all-terrain tires",
        "interior": "rugged cloth seats with washable surfaces, vertical 7-inch touchscreen, exposed Allen screws on dashboard, grab handles",
    },
    "chevy-traverse-z71": {
        "spec":  "2025 Chevrolet Traverse Z71 three-row mid-size SUV third generation, rugged off-road-styled crossover, squared-off front fascia with Z71 dark-finish grille and red Z71 badging, integrated skid plates, slim LED headlights with Chevy bowtie emblem",
        "color": "harvest bronze metallic paint, 18-inch dark machined-finish alloy wheels with all-terrain tires",
        "interior": "Z71-specific cloth and leatherette seats with red contrast stitching, 17.7-inch infotainment touchscreen, 11-inch driver display, rugged rubber floor mats",
    },
}

ANGLE_DESC = {
    "front":    "front three-quarter studio view at eye level, camera offset 30 degrees, full front fascia, grille, headlamps, hood and bumper",
    "rear":     "rear three-quarter studio view at eye level, camera offset 30 degrees, full taillight signature, tailgate or trunk, rear bumper",
    "interior": "interior cockpit studio photograph from the driver-door perspective, dashboard and steering wheel filling frame, instrument cluster and infotainment screen, soft cabin lighting",
    "wheels":   "extreme close-up macro studio photograph of one front wheel and tire, factory wheel design centered, brake caliper behind spokes, tire sidewall lettering, shallow depth of field",
    "side":     "pure side profile studio shot from exactly 90 degrees, complete vehicle silhouette filling frame, all doors and proportions visible",
}

BACKDROP = "Premium cobalt-blue gradient studio backdrop, deep navy floor with soft reflection, photorealistic 8K editorial automotive photography, cinematic studio lighting with rim light on body panels. Clean studio shot with no people, no text overlays, no watermarks."

PRIORITY = ["front", "side", "interior"]
SECONDARY = ["rear", "wheels"]

TARGET_DIR = Path("/home/user/workspace/gita-v2/images")

manifest = []
for slug, info in CARS.items():
    for angle in PRIORITY + SECONDARY:
        adesc = ANGLE_DESC[angle]
        if angle == "interior":
            body = f"{info['spec']}. {info['interior']}. {adesc}."
        else:
            body = f"{info['spec']}, {info['color']}. {adesc}."
        prompt = f"{body} {BACKDROP}"
        manifest.append({
            "slug": slug,
            "angle": angle,
            "priority": angle in PRIORITY,
            "filename": f"{slug}-{angle}",
            "prompt": prompt,
        })

# tag existing
existing = {p.stem: p for p in TARGET_DIR.glob("*.png")}
for item in manifest:
    fn = item["filename"]
    item["exists"] = fn in existing and existing[fn].stat().st_size > 50000

with open("/home/user/workspace/gita-v2/prompts_manifest_v3.json", "w") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

todo_priority = [m for m in manifest if m["priority"] and not m["exists"]]
todo_secondary = [m for m in manifest if not m["priority"] and not m["exists"]]
done = [m for m in manifest if m["exists"]]
print(f"Total: {len(manifest)} | Done: {len(done)} | Priority TODO: {len(todo_priority)} | Secondary TODO: {len(todo_secondary)}")
