"""Keywords for utils"""
import json
 
from robot.api import logger
from robot.api.deco import keyword, library
 
 
@library(scope="SUITE", version="1.0", auto_keywords=False)
class Utils:
 
    @keyword
    def get_field_from_response(self, response: str | dict, field_name: str | list) -> str:
        """
        Returns specified field from API response.
        """
        if isinstance(response, str):
            response = json.loads(response)
        if isinstance(field_name, str):
            field_name = field_name.split(">")
        if len(field_name) > 1:
            return self.get_field_from_response(response[field_name[0]], field_name[1:])
        else:
            return response[field_name[0]]
    