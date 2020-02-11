# first pip install python-bittrex
# How to install in Pycharm?
# File -> Settings -> Project interpreter -> Install -> python-bittrex

from bittrex.bittrex import Bittrex

my_bittrex = Bittrex('my_api_key', 'my_api_secret')

bsv_price = my_bittrex.get_market_history('USDT-BSV')
print(bsv_price['result'][0]['Price'])