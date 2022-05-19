############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []
    
    Muskmelon = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )
    Muskmelon.add_pairing('mint')
    all_melon_types.append(Muskmelon)

    Casaba = MelonType(
        'cas',
        2003,
        'orange',
        True,
        False,
        'Casaba'
    )
    Casaba.add_pairing('strawberries')
    Casaba.add_pairing('mint')
    all_melon_types.append(Casaba)

    Crenshaw = MelonType(
        "cren",
        1996,
        "green",
        True,
        False,
        "Crenshaw"
    )
    Crenshaw.add_pairing("proscuitto")
    all_melon_types.append(Crenshaw)

    Yellow_Watermelon = MelonType(
        'yw',
        2013,
        'yellow',
        True,
        True,
        'Yellow Watermelon'
    )
    
    Yellow_Watermelon.add_pairing('ice cream')
    all_melon_types.append(Yellow_Watermelon)

    # all_melon_types.extend([Muskmelon, Casaba, Crenshaw, Yellow_Watermelon])
    print(all_melon_types)

    # Fill in the rest

    return all_melon_types

# melon_list = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with ")
        for pairing in melon.pairings:
            print(f"- {pairing}")

    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # loop over melon types, access each melon code by melon.code - make that a key with value of melon instance
    melon_dict = {}

    for melon in melon_types:
        key = melon.code
        melon_dict[key] = melon
    
    return melon_dict 

# make_melon_type_lookup(melon_list)
    # Fill in the rest



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self, type, shape_rating, color_rating, location, harvester):
        """Initialize a melon."""
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.location = location
        self.harvester = harvester

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5:
            return True
        else:
            return False

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
