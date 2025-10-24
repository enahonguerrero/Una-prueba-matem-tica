import math
class punto:
    def __init__ (self, x, y):
        self.x = x
        self.y = y 
    
    def __str__(self):
        return f"{self.x}, {self.y}, este es el punto"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen de coordenadas"
        elif self.x == 0 and self.y != 0:
            return "El punto se encuentra en el eje y"
        elif self.x != 0 and self.y == 0:
            return "El punto se encuentra en el eje x"
        elif self.x > 0 and self.y > 0:
            return "El punto se encuentra en el cuadrante : I"
        elif self.x < 0 and self.y > 0:
            return "El punto se encuentra en el cuadrante : II"
        elif self.x < 0 and self.y < 0:
            return "El punto se encuentra en el cuadrante : III"
        elif self.x > 0 and self.y < 0:
            return "El punto se encuentra en el cuadrante : IV"

    def vector(self, otro_punto):
        x_resultante = otro_punto.x - self.x
        y_resultante = otro_punto.y - self.y
        return punto(x_resultante, y_resultante)
    
    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        distancia_redondeada = round(distancia, 2)
        return distancia_redondeada
    
