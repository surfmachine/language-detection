import os, requests, uuid, json

# get environment settings (azure cognitive services key and endpoint)
from Environment import Environment
env = Environment()

# headers
subscription_key = env.getAzureCognitiveServiceKey()
xclient_trace_id = str(uuid.uuid4())

headers = {
    'Content-type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
    'X-ClientTraceId': xclient_trace_id
}

# text analytics service url
url = env.getAzureTextAnalyticsServiceUrl()

# body
body = {
    "documents": [
        {
            "id": "1",
            "text": "Hello world"
        },
        {
            "countryHint": "US",
            "id": "2",
            "text": "Bonjour tout le monde"
        },
        {
            "countryHint": "US",
            "id": "3",
            "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."
        },
        {
            "countryHint": "US",
            "id": "4",
            "text": ":) :( :D"
        }
    ]
}

# request
request = requests.post(url, headers=headers, json=body)

response = request.json()
print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
