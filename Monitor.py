class Monitor:
    def __init__(self):
        self.cards = []
        self.quan = -1
        self.playedID = -1

    def analyze_request(self, request):
        commands = request.split(' ')

        return ("PASS",commands)

