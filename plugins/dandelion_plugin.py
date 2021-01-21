import requests
from plugins.api_plugin import ApiPlugin

try:
    import json
except ImportError:
    import simplejson as json


class DandelionPlugin(ApiPlugin):
    """
        A plugin to access Dandelion API, for semantic text analytics
        Visit the website to subscribe and get an api key:
        https://dandelion.eu/accounts/register/?next=/docs/api/datatxt/nex/getting-started/

        Attributes:
            _api_key: the api key obtained on the website by the user to access the services
            _endpoint_entities: endpoint for Entity Extraction API
    """
    _api_key = None
    _endpoint_entities = "https://api.dandelion.eu/datatxt/nex/v1/?text={}&top_entities=10&social." \
                         "hashtag=true&social.mention=true&include=types%2Ccategories&token={}"

    def configure(self, api_key):
        """
            Configure the plugin with a key to the API. This method must be called before any other method.

            :param api_key: the api key obtained on the website by the user to access the services
                visit the website to subscribe and get an api key: https://dandelion.eu/
            :type api_key: string
        """
        self._api_key = api_key

    def authenticate(self):
        """ This api doesnt need authentication """
        pass

    def get_entities(self, text):
        """
            Extracts the main entities from the text provided.

            From the website:  this API you will be able to automatically tag your texts,
            extracting Wikipedia entities and enriching your data.
            Free plan alows 1.000/day requests per day (~30.000/month).

            :param text: text that will be analyzed. mandatory.
            :type text: string

            :return the entities extracted from the text
            :rtype list of strings
        """
        if not self._api_key:
            raise RuntimeError("There isn't api key for this plugin. Please, call configure before usage.")
        if not type(text) is str:
            raise TypeError(
                f"Parameter 'text' is of type {type(text)}. This attribute must be an instance of string.")
        entities = []
        request_uri = self._endpoint_entities.format(text, self._api_key)
        response = requests.get(request_uri)
        dictResponse = json.loads(response.text)
        if 'annotations' in dictResponse:
            for annotation in dictResponse['annotations']:
                if annotation['spot'] not in entities:
                    entities.append(annotation['spot'])

        return entities
