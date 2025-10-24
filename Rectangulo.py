class rectángulo:
    def __init__ (self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def base(self):
        return abs(self.punto2.x - self.punto1.x)
    
    def altura(self):
        return abs(self.punto2.y - self.punto1.x)
    
    def área(self):
        return self.base() * self.altura()
    
    def __str__ (self):
        f"El rectángulo tiene como base : {self.base()}; Como altura {self.altura()}; y su área es la siguiente : {self.área()}"


