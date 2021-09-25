import logging
import requests as re
import infapy
import json

# # infapy.log = logging.getinfapy.log(__name__)
# # print(infapy.log)
# class UpdateOrg:

#     def __init__(self,v2,v2BaseURL,v2icSessionID):
#         self._v2 = v2
#         self._v2BaseURL = v2BaseURL
#         self._v2icSessionID = v2icSessionID
        
#     def updateOrgDetails(self):
#         url=self._v2BaseURL + "/api/v2/org"
#         headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionID":self._v2icSessionID}
#         infapy.log.info("GetOrgDetails URL - " + url)
#         infapy.log.info("API Headers: " + str(headers))
#         infapy.log.info("Body: " + "This API requires no body")
#         try:
#             response = re.get(url=url, headers=headers)
#             infapy.log.debug(str(response.json()))
#         except Exception as e:
#             infapy.log.exception(e)
#             raise
#         infapy.log.info("Fetched the Organization Details from IICS")
#         data = response.json()
#         return data
def updateSubOrgDetails(self, subId):
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