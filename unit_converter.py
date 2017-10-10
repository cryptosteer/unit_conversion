
conversion_factor_to_inch = {
    "m": 39.3701,
    "yd": 36.0,
    "in": 1.0,
}


class UnitOfLength():
    """This class defines the supported measuring units registered at
    conversion_factor_to_inch dictionary."""
    def __init__(self, value, unit):
        self.check_unit_supported(unit)
        self.unit = unit
        self.value = value

    def convert(self, unit_to_convert):
        self.check_unit_supported(unit_to_convert)
        new_value = (self.value * conversion_factor_to_inch[self.unit])\
            / conversion_factor_to_inch[unit_to_convert]
        self.unit = unit_to_convert
        new_unit_of_length = UnitOfLength(new_value, unit_to_convert)
        return new_unit_of_length

    def check_unit_supported(self, unit):
        if unit not in conversion_factor_to_inch.keys():
            raise Exception("Length unit '" + unit + "' is not supported")

    def __repr__(self):
        value = str(self.value).rstrip('0').rstrip('.')
        return str(value + " " + self.unit)
