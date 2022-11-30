from classes.trader import Trader
from lib.function_tools import get_config

CONFIG_FILE = "config.json"
config = get_config(CONFIG_FILE)
trader_client = Trader(config=config)
historicParam = {
    "exchange": "NSE",
    "symboltoken": "3045",
    "interval": "ONE_MINUTE",
    "fromdate": "2021-02-08 09:00",
    "todate": "2021-02-08 09:16",
}
print(trader_client.get_candle_data(historicParam))
