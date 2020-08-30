"""

Universidad del Valle de Guatemala
Graficas por computadora
Obj
Jorge Suchite Carnet 15293
07/07/2020
SR3 . Obj Model


"""
class ModelObJ(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines = file.read().splitlines()

        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.modobj()



#### muchos objs vienen con diferentes signos de puntuacion para separar varias cosas
### en este caso se arreglaron los que a mi me aparecieron
    def modobj(self):
        for line in self.lines:
            if line:
                try:
                    prefix, value = line.split(' ', 1)
                except:
                    continue

                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                    # normales
                elif prefix == 'vn':
                    self.normals.append(list(map(float,value.split(' '))))
                    #coordens
                elif prefix == 'vt':
                    self.texcoords.append(list(map(float,value.split(' '))))
                    #caras
                elif prefix == 'f':
                    caras = value.split(' ')
                    lista = []
                    for cara in caras:
                        if cara != '':
                            c = cara.split('/')
                            vector = []
                            for x in c:
                                try:
                                    vector.append(int(x))
                                except:
                                    print(str(x))

                            lista.append(vector)
                    self.faces.append(lista)
        print("Si se pudo cargar")