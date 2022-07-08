class Source:
    def __init__(self, name, age, profession, language, years_of_experience):
        self.name = name
        self.age = age
        self.profession = profession
        self.language = language
        self.years_of_experience = years_of_experience

    @classmethod
    def _get_map(cls):
        return {
            "name": "full_name",
            "age": "years",
            "profession": "field",
            "language": "lang",
            "years_of_experience": "exp",
        }

    def map(self, _src_attr):  # return None or tuple with dst attr name and value
        dst_attr = self._get_map().get(_src_attr)
        if dst_attr:
            return dst_attr, getattr(self, _src_attr),


class Destination:
    full_name = None
    years = None
    field = None
    lang = None
    exp = None

    def __str__(self):
        return f'{self.full_name}, {self.years}, {self.field}, {self.lang}, {self.exp}'


if __name__ == '__main__':
    src = Source("John Doe", 35, "programmer", "golang", 2)
    dst = Destination()

    for attr in src.__dir__():
        mapped = src.map(attr)
        if mapped:
            dst_attr, value = mapped
            setattr(dst, dst_attr, value)

    print(dst) # dst now has all values from src in respective attrs
