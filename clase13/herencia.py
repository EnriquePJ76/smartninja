

class Player():

    def __init__(self, first_name, last_name, height_cm=1.8, weight_kg=75):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def fullname(self):
        #return "{0}, {1}".format(self.last_name, self.first_name)
        return "{1} {0}".format(self.last_name, self.first_name)

    def __str__(self):
        return self.fullname()




class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm=1.8, weight_kg=75, points=0, rebounds=0, assists=0):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def __str__(self):
        return "Basket player: {0}".format(super().__str__())


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name, last_name, height_cm, weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

    def __str__(self):
        return "Soccer player: {0}".format(super().__str__())

lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586, yellow_cards=95, red_cards=11)
messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

players = [lebron, kev_dur, ronaldo, messi]

for p in players:
    print ( p )
