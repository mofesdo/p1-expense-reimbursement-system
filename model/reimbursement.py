class Reimbursement:
    def __init__(self, user, price, urgent, description):
        self.canceled = False
        self.approved = False
        self.user = user
        self.urgent = urgent
        self.price = price
        self.description = description

    def save(self):
        pass







