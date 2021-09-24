import logging
import requests as re
import infapy
import json

# infapy.log = logging.getinfapy.log(__name__)
# print(infapy.log)
class Schedule:
    """This class is a handler for fetching
    the Schedule Details from IICS and executing other V3 Schedule APIs
    """
    def __init__(self,v3,v3BaseURL,v3SessionID):
        self._v3 = v3
        self._v3BaseURL = v3BaseURL
        self._v3SessionID = v3SessionID


    def getAllSchedules(self):
        """getAllSchedules returns details for all Schedules in the Org.

        Returns:
            List of dict: <Schedule Details in dict Format>
        """
        url=self._v3BaseURL + "/public/core/v3/schedule"
        headers = {'Content-Type': "application/json", 'Accept': "application/json","INFA-SESSION-ID":self._v3SessionID}
        infapy.log.info("getAllSchedules URL - " + url)
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
        infapy.log.info("Fetched Details for All Schedules in the Org")
        data = response.json()
        return data

    def getScheduleById(self,id):
        """getScheduleById returns details for the schedule as specified by the Id.

        Args:
            id (string): Schedule Id.

        Returns:
            dict: <Schedule Details in dict Format>
        """

        url=self._v3BaseURL + "/public/core/v3/schedule/" + id
        headers = {'Content-Type': "application/json", 'Accept': "application/json","INFA-SESSION-ID":self._v3SessionID}
        infapy.log.info("getScheduleById URL - " + url)
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
        infapy.log.info("Fetched Details for Schedule " + id )
        data = response.json()
        return data

    def getSchedulesWithQuery(self,query):
        """getScheduleWithQuery returns details for the schedules as specified by the filter query provided.

        Args:
            query (string): Filter Query to filter out Schedules.

        Returns:
            list of dict: <Schedule Details in dict Format>
        """

        url=self._v3BaseURL + "/public/core/v3/schedule?q=" + query
        headers = {'Content-Type': "application/json", 'Accept': "application/json","INFA-SESSION-ID":self._v3SessionID}
        infapy.log.info("getScheduleWithQuery URL - " + url)
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
        infapy.log.info("Fetched Details for Schedules using the Query: " + query )
        data = response.json()
        return data