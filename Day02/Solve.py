class present:
    def __init__(self, dimensions : list):
        self.x = int(dimensions[0])
        self.y = int(dimensions[1])
        self.z = int(dimensions[2])

    def get_wrap_surface(self):
        self.s1 = self.x*self.y
        self.s2 = self.x*self.z
        self.s3 = self.y*self.z
        
        small_bit = min([self.s1, self.s2, self.s3])
        wrap = (self.s1 + self.s2 + self.s3)*2 + small_bit

        return wrap
    
    def get_ribbon_size(self):
        p1 = (self.x + self.y)*2
        p2 = (self.x + self.z)*2
        p3 = (self.z + self.y)*2

        main_ribbon = min(p1, p2, p3)
        bow = self.x*self.y*self.z

        return main_ribbon + bow

with open("Day02/Input.txt") as file:
    presents = [present(line.strip().split('x')) for line in file.readlines()]

wrap_amount = 0
for present in presents:
    wrap_amount += present.get_wrap_surface()

print(f'Part 1 : The total amount of wrap is {wrap_amount} square feet')

ribbon_amount = 0
for present in presents:
    ribbon_amount += present.get_ribbon_size()

print(f'Part 2 : The total amount of ribbon is {ribbon_amount} feet')