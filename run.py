import requests
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

CANARY_ADDR = os.environ.get("CANARY_ADDR")
CANARY_TX = os.environ.get("CANARY_TX")

url = "https://api.blockcypher.com/v1/btc/main/addrs/{addr}?unspentOnly=true"
response = requests.get(url.format(addr=CANARY_ADDR))
data = response.json()

txrefs = data["txrefs"]
print("balance: {}".format(data["balance"]))
txref = next(tx for tx in data["txrefs"] if tx["tx_hash"] == CANARY_TX)
print("txn spent? {}".format(txref["spent"]))
