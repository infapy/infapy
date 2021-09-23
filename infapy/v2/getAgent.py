import logging
import requests as re
import infapy
import json

# infapy.log = logging.getinfapy.log(__name__)
# print(infapy.log)
class GetAgent:
    """This class is a handler for fetching
    the Activity Monitor from IICS
    """
    def __init__(self,v2,v2BaseURL,v2icSessionID):
        self._v2 = v2
        self._v2BaseURL = v2BaseURL
        self._v2icSessionID = v2icSessionID
    

    def getAllAgentDetails(self):
        """getAllAgentDetails returns details for all Agents in the Org.

        Returns:
            List of dict: <Agent Details in dict Format>
        """
        url=self._v2BaseURL + "/api/v2/agent"
        headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionID":self._v2icSessionID}
        infapy.log.info("getAllAgentDetails URL - " + url)
        infapy.log.info("API Headers: " + str(headers))
        infapy.log.info("Body: " + "This API requires no body")
        # The below format is for post
        # bodyV3={"username": userName,"password": password}
        # r3 = re.post(url=urlV3, json=bodyV3, headers=headers)
        try:
            response = re.get(url=url, headers=headers)
            infapy.log.debug(str(response.json()))
        except Exception as e:
            infapy.log.exception(e)
            raise
        infapy.log.info("Fetched Agent Details for All Agents in the Org")
        data = response.json()
        return data
    
    def getInstallerToken(self,platform):
        """getInstallerToken returns installer link depending on platform, and installer token for registering the secure agent.

        Args:
            platform (string): Operating system type. Valid values: win64 OR linux64

        Returns:
            List of dict: <Installer link and registration token in dict Format>
        """
        url=self._v2BaseURL + "/api/v2/agent/installerInfo/" + platform
        headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionID":self._v2icSessionID}
        infapy.log.info("getInstallerToken URL - " + url)
        infapy.log.info("API Headers: " + str(headers))
        infapy.log.info("Body: " + "This API requires no body")
        # The below format is for post
        # bodyV3={"username": userName,"password": password}
        # r3 = re.post(url=urlV3, json=bodyV3, headers=headers)
        try:
            response = re.get(url=url, headers=headers)
            infapy.log.debug(str(response.json()))
        except Exception as e:
            infapy.log.exception(e)
            raise
        infapy.log.info("Fetched Agent Details for All Agents in the Org")
        data = response.json()
        return data