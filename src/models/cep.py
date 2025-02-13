class Cep:
    def __init__(self, cep, street, neighborhood, city, state):
        self.cep = cep
        self.street = street
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    def display_info(self):
        return f"CEP: {self.cep}, Street: {self.street}, Neighborhood: {self.neighborhood}, City: {self.city}, State: {self.state}"