class KgToPounds:

    def __init__(self, kg):
        self.__set_kg(kg)

    def to_pounds(self):
        return self.__kg * 2.205

    def __set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def __get_kg(self):
        return self.__kg

    kg = property(__get_kg,__set_kg) 
    
k = KgToPounds('a')
k.kg = 5
print(k.kg)