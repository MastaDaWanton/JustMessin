import requests
import logging
import pandas as pd
#Logging Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('api_scraping.log'), logging.StreamHandler()])
# Create a logger object/instance of logger class
logger=logging.getLogger(__name__)

def Get_pokemon(poke_name):
    url=f'https://pokeapi.co/api/v2/pokemon/{poke_name.lower()}'
    logger.info(f"fetching Data for Pokemon: {poke_name}")
    try:
        response=requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data=response.json()
        logger.info(f"Data fetched successfully for Pokemon: {poke_name}")

        Pokemon_Info= {
            'Name': data['name'],
            'ID': data['id'],
            'Height': data['height'],
            'Weight': data['weight'],
            'Types': [t['type']['name'] for t in data['types']],
            'Abilities': [a['ability']['name'] for a in data['abilities']]
        }
        return pd.DataFrame([Pokemon_Info])
      
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        logger.info(f"Finished processing request for Pokemon: {poke_name}") 
    return None

poke_name=input("Enter the name of the Pokemon: ")
pokemon_data=Get_pokemon(poke_name)
if pokemon_data is not None:
    print(pokemon_data)
    print("Data fetched successfully and displayed above.")