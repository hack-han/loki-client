from loki_client import LokiClient
from loki_client import SUPPORTED_DIRECTION


loki_url = 'http://localhost:3100'
loki_client = LokiClient(url=loki_url, disable_ssl=True)

# 1 test ready()
loki_ready = loki_client.ready()
if not loki_ready:
    print('Loki is not ready.')
    exit(1)

# 2 test query_range_with_context()
query = r'{host="ubuntu"}|~"error"'
result = loki_client.query_range_with_context(query=query, context_before=5, context_after=3)
if result[0]:
    print(result)

# 3 test post()
label_dic = {'host': 'windows', 'env': 'test'}
logs_lst = ['This is line 1', 'This is line 2', 'This is line 3', 'This is line 4']
result = loki_client.post(label_dic, logs_lst)
if not result[0]:
    print(result[1])

# 4 test labels()
result = loki_client.labels()
print(result)

# 5 test query_range()
query = r'{host="ubuntu"}|~"error"'
result = loki_client.query_range(query, direction=SUPPORTED_DIRECTION[1], limit=10)
print(result)

if result[0]:
    print(result[1]['status'])
    print(result[1]['data']['resultType'])

# 6 test query()
result = loki_client.query(query, direction=SUPPORTED_DIRECTION[1], limit=10)
print(result)
