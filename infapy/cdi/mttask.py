import logging
import requests as re
import infapy
import json

# infapy.log = logging.getinfapy.log(__name__)
# print(infapy.log)
class MTTask:
    """This class is a handler for running IICS mttask APIs
    """
    def __init__(self,cdi,cdiBaseURL,cdiSessionID):
        self._cdi=cdi
        self._cdiSessionID = cdiSessionID
        self._cdiBaseURL = cdiBaseURL

    def getAllMTTasks(self):
        """getAllSchedules returns details for all Schedules in the Org.

        Returns:
            List of dict: <Schedule Details in dict Format>
        """
        url=self._cdiBaseURL + "/api/v2/mttask"
        headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionId":self._cdiSessionID}
        infapy.log.info("getAllMTTasks URL - " + url)
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
        infapy.log.info("Fetched List of All Mapping Tasks in the Org")
        data = response.json()
        return data