import logging
import requests as re
import infapy
import json

# infapy.log = logging.getinfapy.log(__name__)
# print(infapy.log)
class GetOrg:
    """
    This class is a handler for fetching the Org and Sub-org Details from IICS
    """
    def __init__(self,v2,v2BaseURL,v2icSessionID):
        self._v2 = v2
        self._v2BaseURL = v2BaseURL
        self._v2icSessionID = v2icSessionID
        
    def getOrgDetails(self):
        """getOrgDetails returns the details of the IICS Organization

        Returns:
            List of dict: <Organization Details in dict Format>
        """
        url=self._v2BaseURL + "/api/v2/org"
        headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionID":self._v2icSessionID}
        infapy.log.info("GetOrgDetails URL - " + url)
        infapy.log.info("API Headers: " + str(headers))
        infapy.log.info("Body: " + "This API requires no body")
        try:
            response = re.get(url=url, headers=headers)
            infapy.log.debug(str(response.json()))
        except Exception as e:
            infapy.log.exception(e)
            raise
        infapy.log.info("Fetched the Organization Details from IICS")
        data = response.json()
        return data

    def getSubOrgDetailsById(self, subId):
        """getSubOrgDetailsById returns the details of the Sub Organization with the Id passed as 'subId'

        Args:
            subId (string): Sub Organization Id

        Returns:
            List of dict: <Sub Organization Details in dict Format>
        """
        url=self._v2BaseURL + "/api/v2/org/" + subId
        headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionID":self._v2icSessionID}
        infapy.log.info("GetSubOrgDetailsById URL - " + url)
        infapy.log.info("API Headers: " + str(headers))
        infapy.log.info("Body: " + "This API requires no body")
        try:
            response = re.get(url=url, headers=headers)
            infapy.log.debug(str(response.json()))
        except Exception as e:
            infapy.log.exception(e)
            raise
        infapy.log.info("Fetched the Sub Organization Details from IICS")
        data = response.json()
        return data

    def getSubOrgDetailsByName(self, subName):
        """getSubOrgDetailsByName returns the details of the Sub Organization with the name passed as 'subName'

        Args:
            subName (string): Sub Organization Name

        Returns:
            List of dict: <Sub Organization Details in dict Format>
        """
        subNameSpaceReplaced = subName.replace(" ","%20")
        url=self._v2BaseURL + "/api/v2/org/name/" + subNameSpaceReplaced
        headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionID":self._v2icSessionID}
        infapy.log.info("GetSubOrgDetailsByName URL - " + url)
        infapy.log.info("API Headers: " + str(headers))
        infapy.log.info("Body: " + "This API requires no body")
        try:
            response = re.get(url=url, headers=headers)
            infapy.log.debug(str(response.json()))
        except Exception as e:
            infapy.log.exception(e)
            raise
        infapy.log.info("Fetched the Sub Organization Details from IICS")
        data = response.json()
        return data