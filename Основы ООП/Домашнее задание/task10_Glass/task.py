# TODO написать класс Glass согласно условию
class Glass:
    def __init__(self, material: str):
        """
        Создаем стакан
        :param material: материал, из которого изготавливается стакан
        """
        self.material = None
        self.get_material(material)

    def get_material(self, material: str):
        if not isinstance(material, str):
            raise TypeError("К производству предложен не материал")
        # if material != "стекло" or "песок":
        #     raise ValueError("Предложен неподходящий материал")
        self.material = material
        return self.material


if __name__ == "__main__":
    glass_1 = Glass("песок")
    print(glass_1)
