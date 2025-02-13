class CepService:
    def __init__(self):
        self.api_url = "https://viacep.com.br/ws/{}/json/"

    def fetch_cep_data(self, cep):
        import requests
        
        if not self.validate_cep(cep):
            raise ValueError("Invalid CEP format.")
        
        response = requests.get(self.api_url.format(cep))
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def validate_cep(self, cep):
        return isinstance(cep, str) and len(cep) == 8 and cep.isdigit()