>>> from FaucetPy import Api
>>> myApi = Api("fc50c1915d45b2729b965d535a00a813ef4451b4")
>>> myApi.get_balance()
{'status': 200, 'message': 'OK', 'currency': 'BTC', 'balance': '0', 'balance_bitcoin': '0.00000000'}
>>> myApi.listFaucets()
{'status': 404, 'message': 'Invalid API method accessed.'}
>>> myApi.payouts()
{'status': 200, 'message': 'OK', 'rewards': []}
>>> myApi.my_payouts()
{'status': 200, 'message': 'OK', 'rewards': []}