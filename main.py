import pandas as pd
import matplotlib as mpl
from matplotlib import pyplot as plt
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='aud', days=300)
ethereum_data = cg.get_coin_market_chart_by_id(id='solana', vs_currency='aud', days=300)
pricess = ethereum_data['prices']
prices = bitcoin_data['prices']
data = pd.DataFrame(prices, columns=['TimeStamp', 'Prices'])

data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
datas = pd.DataFrame(pricess, columns=['TimeStamp', 'Prices'])

datas['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

del data['TimeStamp']
del datas['TimeStamp']
print(data)
cost = data["Prices"]
costs = datas["Prices"]
graph = cost.plot(kind='line')
graphs = costs.plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Prices')
plt.title('Cryptocurrency chart')
plt.show()