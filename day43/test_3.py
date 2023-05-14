class KgToPounds:

    def __init__(self, kg):
        self.kg = kg

    def to_pounds(self):
        return self.kg * 2.205

 
k = KgToPounds('a')

k.to_pounds()
