class Reindeer:
    # -----------------------------------------------------
    # Configuration
    # -----------------------------------------------------

    def __init__(self, name, speed, endurance, pause):
        self.name      = name
        self.speed     = speed
        self.endurance = endurance
        self.pause     = pause
        self.state     = "moving"
        self.ticks     = endurance
        self.distance  = 0
        self.points    = 0

    # -----------------------------------------------------
    # Public Methods
    # -----------------------------------------------------

    def increment_points(self):
        self.points += 1
        
    def tick(self):
        self.ticks += -1
        if self.state == "moving":
            self.distance += self.speed

        if self.ticks == 0:
            if self.state == "moving":
                self.ticks = self.pause
                self.state = "resting"
            else:
                self.ticks = self.endurance
                self.state = "moving"
