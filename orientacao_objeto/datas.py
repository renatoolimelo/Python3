class Data:

    def __init__(self, day, mounth, year):
        self.day = day
        self.mounth = mounth
        self.year = year

    def formatada(self):
        print("{:02d}/{:02d}/{:02d}".format(self.day, self.mounth, self.year))

