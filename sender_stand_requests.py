import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOGS_MAIN_PATH)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USER_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers) #Recuerda al llamar función agregar ep parametro de data.User_Body.

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         headers=data.headers,
                         json=products_ids)
