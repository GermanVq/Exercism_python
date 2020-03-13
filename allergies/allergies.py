class Allergies:

    def __init__(self, score):
        self.score = score
        self.table = dict(eggs=(1), 
                          peanuts=(2), 
                          shellfish=(4), 
                          strawberries=(8), 
                          tomatoes=(16),
                          chocolate=(32), 
                          pollen=(64), 
                          cats=(128)
                          )

    def allergic_to(self, item):
         return self.score & self.table[item] > 0
     
    @property
    def lst(self):
        return [s for s, i in self.table.items() 
                if i & self.score > 0]
