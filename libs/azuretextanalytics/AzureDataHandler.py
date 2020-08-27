import uuid


class AzureDataHandler:
    """Handle azure data formats for of the service request and response."""

    #
    # Prepare Azure service request
    #

    def __init__(self, debug=False):
        self.debug = debug


    def create_document(self, text, id=None):
        text_id = id if (id != None) else str(uuid.uuid4())
        record = {"id":text_id, "text":text}
        return {"documents":[record] }


    def create_documents(self, df):
        records = []
        for idx, row in df.iterrows():
            id   = row['id']
            lang = row['lang']
            text = row['content']
            lang_id = lang + ":" + str(id)
            record = {"id":lang_id, "text":text}
            records.append(record)
        return {"documents":records }

    #
    # Handle Azure service response
    #

    def extract_result(self, response):
        results = self.extract_results(response)
        if len(results) == 0:
            return None
        return results[0]


    def extract_results(self, response):
        results = []
        documents = response["documents"]
        for document in documents:
            result = self._extract_document(document)
            results.append(result)
        return results


    def _extract_document(self, document):
        """Extract the first detected language entry with the prediction and probability (score).
         Sample structure:
            {
                "detectedLanguages": [
                    {
                        "iso6391Name": "de",
                        "name": "German",
                        "score": 0.882352888584137
                    }
                ],
                "id": "de:1"
            },
        """
        lang = document["detectedLanguages"][0]['iso6391Name']
        prob = document["detectedLanguages"][0]['score']
        return {'language': lang, 'probability': prob}
