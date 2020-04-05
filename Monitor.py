class Monitor:
    def __init__(self):
        self.cards = []
        self.quan = -1
        self.playerID = -1

    def analyze_request(self, request):
        commands = request.split(' ')
        type_num = commands[0]
        result = None

        if type_num == 0:
            result, debug = self.init_id_and_quan(commands)
        elif type_num == 1:
            result, debug = self.get_cards(commands)

        return result, commands

    def init_id_and_quan(self, commands):
        self.playerID = commands[1]
        self.quan = commands[2]
        return "PASS", ""

    def get_cards(self, commands):
        self.cards = commands[5:]
        return "PASS", self.cards


