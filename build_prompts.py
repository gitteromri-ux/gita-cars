#!/usr/bin/env python3
"""Build the prompt manifest for all 20 cars x 5 angles = 100 images."""
import json

# Descriptive spec per car: (slug, exact_model_description, color_phrase)
CARS = [
    ("mercedes-g63-amg",          "2025 Mercedes-AMG G63 (W463 generation), AMG body kit, AMG Performance flared fenders, side-exit quad exhaust", "matte black exterior, AMG black 22-inch cross-spoke wheels"),
    ("mercedes-gls-450d",         "2025 Mercedes-Benz GLS 450d 4MATIC (X167), AMG Line exterior package, large chrome grille with vertical Mercedes star pattern", "obsidian black metallic paint, 21-inch AMG multi-spoke alloy wheels"),
    ("mercedes-g580-eq",          "2025 Mercedes-Benz G580 with EQ Technology (electric G-Class, W465), square boxy silhouette, signature flat LED headlamps, exposed rear-mounted spare-wheel cover", "alpine grey magno matte finish, 20-inch aero alloy wheels"),
    ("lucid-air-pure",            "2025 Lucid Air Pure sedan, low aerodynamic four-door silhouette, sleek micro-LED headlight bar across full front fascia, frameless flush door handles", "stellar white pearl paint, 19-inch aero turbine wheels"),
    ("mercedes-g500",             "2024 Mercedes-Benz G500 (W463 generation, standard non-AMG G-Wagon), boxy SUV shape, round LED headlamps, classic chrome grille slats", "designo manufaktur olive green metallic, 19-inch five-spoke alloy wheels"),
    ("chevy-tahoe-high-country",  "2025 Chevrolet Tahoe High Country full-size SUV, bold chrome grille bar, large LED dual headlamps with C-shape DRL, body-color rocker panels", "black metallic paint, 22-inch polished chrome multi-spoke wheels"),
    ("bmw-x7-xdrive40i",          "2025 BMW X7 xDrive40i (G07 facelift), split-headlight design with tall illuminated kidney grille, M Sport package body kit", "carbon black metallic exterior, 22-inch M aerodynamic alloy wheels"),
    ("tesla-model-x-lr",          "2024 Tesla Model X Long Range, falcon-wing rear doors visible, smooth aerodynamic SUV silhouette, full-width front lightbar, no traditional grille", "midnight silver metallic paint, 22-inch turbine wheels"),
    ("mercedes-s580e",            "2025 Mercedes-Benz S580e plug-in hybrid sedan (W223), long elegant flagship sedan silhouette, full-LED Digital Light headlamps, large chrome upright grille with three-pointed star", "selenite grey magno metallic, 20-inch AMG multi-spoke wheels"),
    ("ford-bronco-raptor",        "2025 Ford Bronco Raptor 4-door, wide fender flares, FORD lettering across grille, off-road bumper with integrated LED light pods, raised suspension stance", "code orange paint, 37-inch BFGoodrich KO2 mud-terrain tires on beadlock-style black wheels"),
    ("ford-f150-raptor",          "2025 Ford F-150 Raptor R full-size pickup truck, massive blacked-out FORD grille with amber marker lights, aggressive vented hood, wide track stance", "agate black metallic paint, 37-inch BFGoodrich KO2 tires on matte-black off-road wheels"),
    ("mercedes-gle-450d",         "2025 Mercedes-Benz GLE 450d 4MATIC SUV (W167), AMG Line exterior, sloping coupe-like roofline, large diamond-pattern chrome grille", "polar white paint, 21-inch AMG five-twin-spoke alloy wheels"),
    ("tesla-cybertruck-awd",      "2024 Tesla Cybertruck AWD, angular faceted stainless-steel pickup-truck body, sharp triangular silhouette, full-width LED light bar front and rear, no traditional grille", "raw brushed stainless-steel exterior, 20-inch dark cyber wheels"),
    ("bmw-x5-xdrive40i",          "2025 BMW X5 xDrive40i SUV (G05 facelift), M Sport exterior package, tall vertical kidney grille, adaptive LED headlights with hexagonal DRLs", "phytonic blue metallic paint, 21-inch M Y-spoke alloy wheels"),
    ("ford-bronco-big-bend",      "2024 Ford Bronco Big Bend 4-door SUV (sixth-generation), boxy retro-modern silhouette, round LED headlights flanking large white FORD lettering grille, removable doors and roof visible", "area 51 light blue paint, 17-inch grey-painted aluminum wheels with all-terrain tires"),
    ("mustang-gt-v8",             "2025 Ford Mustang GT V8 coupe (S650 generation), long hood and short rear deck, tri-bar LED headlamps, hood scoop bulges, GT badging", "race red paint, 19-inch dark-painted machined-face Y-spoke wheels"),
    ("kia-ev9-rwd",               "2025 Kia EV9 RWD all-electric three-row SUV, upright boxy SUV silhouette, vertical Star Map LED daytime running lights at front and rear, flush door handles", "ocean matte blue exterior, 20-inch aero alloy wheels"),
    ("rivian-r1s-dual",           "2025 Rivian R1S Dual Motor electric SUV, signature oval stadium-light headlamps connected by full-width LED bar, clean smooth body panels", "limestone green metallic paint, 21-inch sport dark alloy wheels"),
    ("jeep-wrangler-sport",       "2024 Jeep Wrangler Sport 4-door (JL generation), classic seven-slot grille, round headlamps, flat fender flares, removable hard top", "firecracker red paint, 17-inch black-painted steel wheels with off-road tires"),
    ("chevy-traverse-z71",        "2025 Chevrolet Traverse Z71 three-row SUV (third generation), squared-off rugged grille, dark-finish trim, integrated skid plates", "harvest bronze metallic paint, 18-inch dark machined alloy wheels with all-terrain tires"),
]

# Angle prompts
ANGLE_DESC = {
    "front":    "front three-quarter view showing the full front fascia, grille, headlamps, hood, and front bumper details, camera at eye level slightly off-center",
    "rear":     "rear three-quarter view showing taillight signature, tailgate or trunk, rear bumper and exhaust outlets, camera slightly low and offset to one side",
    "interior": "interior cockpit photography from the driver-door perspective, showing leather seats, steering wheel, full digital instrument cluster, center infotainment touchscreen, dashboard stitching detail, soft cabin lighting",
    "wheels":   "extreme close-up macro shot of one front wheel and tire, showing the alloy wheel design, brake caliper behind spokes, tire sidewall detail, shallow depth of field",
    "side":     "pure side profile shot from 90 degrees, showing the complete silhouette and proportions, doors, greenhouse, wheel arches, body length",
}

BACKDROP = "premium cobalt-blue gradient backdrop, deep navy floor with soft reflection, photorealistic 8K editorial automotive photography, cinematic studio lighting with rim light on body panels, no people, no text, no watermark, no logo overlays"

manifest = []
for slug, model_desc, color_desc in CARS:
    for angle, angle_desc in ANGLE_DESC.items():
        if angle == "interior":
            prompt = f"{model_desc}, {color_desc}. Photoreal {angle_desc}. Interior trim color matched to a premium dark leather and brushed-metal cabin. {BACKDROP}"
        elif angle == "wheels":
            prompt = f"{model_desc}, {color_desc}. {angle_desc}. {BACKDROP}"
        else:
            prompt = f"{model_desc}, {color_desc}. {angle_desc}. {BACKDROP}"
        manifest.append({
            "slug": slug,
            "angle": angle,
            "filename": f"{slug}-{angle}",
            "prompt": prompt,
        })

with open("/home/user/workspace/gita-v2/prompts_manifest.json", "w") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Built {len(manifest)} prompts ({len(CARS)} cars × {len(ANGLE_DESC)} angles)")
