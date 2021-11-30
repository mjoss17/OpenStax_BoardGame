class Purse:

    def __init__(self):
        self.coins = 0

    def add(self, coin_difference):
        self.coins += coin_difference
        return self.coins

    
    