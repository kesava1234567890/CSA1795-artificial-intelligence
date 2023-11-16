class VacuumCleaner:
    def __init__(self):
        self.location = [0, 0]
        self.cleaned = set()
    def move(self, direction):
        x, y = self.location
        if direction == 'up':
            self.location = [x, y + 1]
        elif direction == 'down':
            self.location = [x, y - 1]
        elif direction == 'left':
            self.location = [x - 1, y]
        elif direction == 'right':
            self.location = [x + 1, y]
    def clean(self):
        self.cleaned.add(tuple(self.location))
    def display_status(self):
        print(f"Current position: {self.location}")
        print(f"Cleaned locations: {self.cleaned}")
environment = {
    (0, 0): 'dirty',
    (1, 0): 'dirty',
    (2, 2): 'dirty',
    (1, 1): 'dirty'
}
vacuum = VacuumCleaner()
for loc, status in environment.items():
    if status == 'dirty':
        while vacuum.location != list(loc):
            x_diff = vacuum.location[0] - loc[0]
            y_diff = vacuum.location[1] - loc[1]
            if x_diff > 0:
                vacuum.move('left')
            elif x_diff < 0:
                vacuum.move('right')
            elif y_diff > 0:
                vacuum.move('down')
            elif y_diff < 0:
                vacuum.move('up')
        vacuum.clean()
vacuum.display_status()
