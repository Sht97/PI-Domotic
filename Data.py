class Data:

    def __init__(self, data: tuple):
        self.x = int(data[2])
        self.y = int(data[3])
        self.z = int(data[4])
        self.a = int(data[5])
        self.b = int(data[6])
        self.c = int(data[7])

    def get_all_atr(self):
        return [self.x, self.y, self.z, self.a, self.b, self.c]
