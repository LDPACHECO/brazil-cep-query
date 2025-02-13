# main.py

import argparse
from services.cep_service import CepService

def main():
    parser = argparse.ArgumentParser(description='Query Brazilian postal codes (CEPs).')
    parser.add_argument('cep', type=str, help='The postal code (CEP) to query.')
    args = parser.parse_args()

    cep_service = CepService()
    
    if cep_service.validate_cep(args.cep):
        cep_data = cep_service.fetch_cep_data(args.cep)
        if cep_data:
            print(f"CEP: {cep_data.cep}")
            print(f"Street: {cep_data.street}")
            print(f"Neighborhood: {cep_data.neighborhood}")
            print(f"City: {cep_data.city}")
            print(f"State: {cep_data.state}")
        else:
            print("No data found for the provided CEP.")
    else:
        print("Invalid CEP format.")

if __name__ == '__main__':
    main()