import os, requests, uuid, json
import pandas as pd


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

# prepare body from articles
csv_file = "../../tests/data/articles_test_10.csv"
df = pd.read_csv(csv_file, sep=',')

records = []
for idx, row in df.iterrows():
    id   = row['id']
    lang = row['lang']
    text = row['content']
    lang_id = lang + ':' + str(id);
    record = {"id":lang_id, "text":text}
    records.append(record)

body = {"documents":records}

# request
request = requests.post(url, headers=headers, json=body)
response = request.json()

# grab results
results = response["documents"]
for result in results:
    lang_id = result["id"]
    prediction = result["detectedLanguages"][0]['iso6391Name']
    probability = result["detectedLanguages"][0]['score']
    print(lang_id, prediction, probability, result)
