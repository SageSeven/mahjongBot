class Monitor:
    def __init__(self):
        self.cards = []
        self.quan = -1
        self.playerID = -1

    def analyze_request(self, request):
        request = request.strip('\"')
        commands = request.split(' ')
        type_num = int(commands[0])

        result = None
        debug = None

        if type_num == 0:
            result, debug = self.init_id_and_quan(commands)
        elif type_num == 1:
            result, debug = self.get_cards(commands)
        elif type_num == 2:
            result, debug = self.get_one_card(commands)
        elif type_num == 3:
            result, debug = self.handle_other_msg(commands)

        return result, debug

    def init_id_and_quan(self, commands):
        self.playerID = commands[1]
        self.quan = commands[2]
        return "PASS", ""

    def get_cards(self, commands):
        self.cards = commands[5:]
        return "PASS", self.cards

    def get_one_card(self, commands):

        return "PLAY "+commands[1], ""

    def handle_other_msg(self, commands):
        return "PASS", commands
