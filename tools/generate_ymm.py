import json

def slug(s) -> str:
    return (
        str(s)
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
        .replace(".", "")
    )

def make_entry(year, make, model, trim, engine_id, engine_file):
    return {
        "id": f"{slug(year)}_{slug(make)}_{slug(model)}_{slug(trim)}",
        "year": str(year),
        "make": make,
        "model": model,
        "trim": trim,
        "engineId": engine_id,
        "engineFile": engine_file,
    }

# --- EDIT THIS LIST ONLY ---
# Keep trims minimal for MVP; expand later via Admin Mode.
SPECS = [
    # SUBARU WRX
    ("Subaru", "WRX", "Base", 2002, 2005, "subaru_ej205", "lookups/engines/subaru/subaru_ej205.json"),
    ("Subaru", "WRX", "STI", 2004, 2008, "subaru_ej257", "lookups/engines/subaru/subaru_ej257.json"),
    ("Subaru", "WRX", "Base", 2006, 2008, "subaru_ej255", "lookups/engines/subaru/subaru_ej255.json"),

    # FORESTER (keep simple)
    ("Subaru", "Forester", "XT", 2004, 2008, "subaru_ej255", "lookups/engines/subaru/subaru_ej255.json"),

    # FORD (placeholder trims; refine later)
    ("Ford", "F-150", "5.4L 3V", 2004, 2010, "ford_modular_54_3v", "lookups/engines/ford/ford_modular_54_3v.json"),
    ("Ford", "Mustang", "GT Coyote Gen1", 2011, 2014, "ford_coyote_gen1", "lookups/engines/ford/ford_coyote_gen1.json"),
    ("Ford", "Mustang", "GT Coyote Gen2", 2015, 2017, "ford_coyote_gen2", "lookups/engines/ford/ford_coyote_gen2.json"),
    ("Ford", "Mustang", "GT Coyote Gen3", 2018, 2023, "ford_coyote_gen3", "lookups/engines/ford/ford_coyote_gen3.json"),
    ("Ford", "Mustang", "GT Coyote Gen4", 2024, 2026, "ford_coyote_gen4", "lookups/engines/ford/ford_coyote_gen4.json"),

    # GM (MVP coarse; we’ll refine engines per platform later)
    ("Chevrolet", "Silverado", "LS-based", 2002, 2007, "gm_ls", "lookups/engines/gm/gm_ls.json"),
    ("Chevrolet", "Suburban", "LS-based", 2002, 2007, "gm_ls", "lookups/engines/gm/gm_ls.json"),
    ("Chevrolet", "Corvette", "LS-based", 2002, 2013, "gm_ls", "lookups/engines/gm/gm_ls.json"),
    ("Chevrolet", "Camaro", "LS-based", 2010, 2015, "gm_ls", "lookups/engines/gm/gm_ls.json"),
]

out = []
for make, model, trim, y0, y1, engine_id, engine_file in SPECS:
    for year in range(y0, y1 + 1):
        out.append(make_entry(year, make, model, trim, engine_id, engine_file))

# Optional: sort for stable diffs
out.sort(key=lambda x: (x["year"], x["make"], x["model"], x["trim"]))

print(json.dumps(out, indent=2))
