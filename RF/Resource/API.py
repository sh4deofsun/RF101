"""Sends ... API requests to preprod and test endpoints."""
import json
from robot.api import logger
from robot.api.deco import keyword, library
import requests
 
 
@library(scope="TEST", version="0.1", auto_keywords=False)
class API:
    """API for sending ... requests."""
    endpoints = {
    }
    @keyword
    def call_api(self, environment: str, req_body: dict, service_name: str, method="POST", expected_status_code="200") -> str:
        """
        Calls API with specified environment and headers.
        Environment: Endpoint name or URL
        Req_body: Request body
        Service name: Endpoint service name
        Method: Request method. default POST
        Expected status code: Default 200
        """
        header = {}
        environment = environment.lower()
        if environment in self.endpoints.keys():
            config = self.endpoints[environment]
        elif environment.startswith("http"):
            config = environment
            logger.info(f"CUSTOM ENVIRONMENT: {environment}")
        else:
            logger.warn(f"INCORRECT ENVIRONMENT: {environment}")
            raise Exception(-99)
 
        match environment:
            case "local":
               config = "http://127.0.0.1:8000"
 
 
        if method == "POST":
            r = requests.post(url=config + '/' + service_name, json=req_body, headers=header)
            logger.info(r.request.headers)
            logger.info(f"POST request sent to {config}, request body={req_body}, headers={header}")
        elif method == "GET":
            r = requests.get(url=config + '/' + service_name, json=req_body, headers=header)
            logger.info(f"GET request sent to {config}/{service_name}, request body={req_body}, headers={header}")
        else:
            raise Exception(-99)
 
        if r.status_code == int(expected_status_code):
            logger.info(f"RESPONSE: {r.text}")
            return r.text
        else:
            logger.warn(f"UNEXPECTED STATUS CODE: {r.status_code}.")
            raise Exception(-99)
 