import os

class Environment():

    def getAzureCognitiveServiceKey(self):
        return self._get_environ('AZURE_CS_KEY')

    def getAzureCognitiveServiceEndpoint(self):
        return self._get_environ('AZURE_CS_ENDPOINT')

    def getAzureTextAnalyticsServiceUrl(self, showStats=False):
        endpoint = self.getAzureCognitiveServiceEndpoint()
        if endpoint == None:
            return None
        path     = '/text/analytics/v2.1/languages'
        params   = '?showStats=' + ('true' if showStats else 'false')
        return endpoint + path + params;

    def _get_environ(self, name):
        """To be able to run the project without the Azure Service, i.e. without the environment settings,
        the key error is catched and None is returned instead.
        """
        try:
            return os.environ[name]
        except KeyError:
            return None


env = Environment();
print(env.getAzureTextAnalyticsServiceUrl())

