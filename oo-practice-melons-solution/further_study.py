from harvest import (
    make_melon_type_lookup,
    make_melon_types,
    Melon,
    get_sellability_report,
)

melon_types = make_melon_types()
melons_by_id = make_melon_type_lookup(melon_types)

melons_from_harvest = []
with open("harvest_log.txt") as file:
    for line in file:
        # Shape 1 Color 2 Type yw Harvested By Sheila Field # 37
        shape_rating = line[(line.find("Shape") + 6) : line.find("Shape") + 7]
        color_rating = line[(line.find("Color") + 6) : line.find("Color") + 7]
        melon_code = line[(line.find("Type") + 5) : (line.find("Harvested") - 1)]
        harvested_by = line[(line.find("By") + 3) : (line.find("Field") - 1)]
        field = line[(line.find("Field") + 8) :]
        melons_from_harvest.append(
            Melon(
                shape_rating=int(shape_rating),
                color_rating=int(color_rating),
                field=field,
                harvester=harvested_by,
                melon_type=melons_by_id.get(melon_code),
            )
        )
get_sellability_report(melons_from_harvest)
