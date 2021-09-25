import requests as re
import infapy
from infapy.exceptions import InvalidDetailsProvided

# infapy.log = logging.getinfapy.log(__name__)

class V2():
    """V2 class is a wrapper class for all the IICS rest v2 APIs
    """
    def __init__(self,v2,v2BaseURL,v2icSessionID):
        """This class is used to leverage the IICS V2 APIs

        Args:
            v2 (json): login response of v2 login API
            v2BaseURL (string): The base url which we get from the v2 login API
            v2icSessionID (string): The icSessionID from the v2 Login API
        """
        infapy.log.info("created a v2 class object successfully")
        infapy.log.info("v2BaseURL: " + v2BaseURL)
        self._v2=v2
        self._v2BaseURL = v2BaseURL
        self._v2icSessionID = v2icSessionID
        
    def getActivityLog(self):
        """This function returns an object of getActivityLog
        which has multiple sub methods to fetch the activity log

        Returns:
            class object: v2.getActivityLog.GetActivityLog
        """
        from infapy.v2.getActivityLog import GetActivityLog
        return GetActivityLog(self._v2,self._v2BaseURL,self._v2icSessionID)

    def org(self):
        """This function returns an object of getOrg
        which has multiple sub methods to fetch the Org and Sub-org Details

        Returns:
            class object: v2.getOrg.GetOrg
        """
        from infapy.v2.org import Org
        return Org(self._v2,self._v2BaseURL,self._v2icSessionID)

    

    def getRuntimeEnvironment(self):
        """This function returns an object of getRuntimeEnvironment
        which has multiple sub methods to fetch the Details of Runtime Environments

        Returns:
            class object: v2.getRuntimeEnvironment.GetRuntimeEnvironment
        """
        from infapy.v2.getRuntimeEnvironment import GetRuntimeEnvironment
        return GetRuntimeEnvironment(self._v2,self._v2BaseURL,self._v2icSessionID)
    
    def getSchedule(self):
        """This function returns an object of getSchedule
        which has multiple sub methods to fetch the Details of Runtime Environments

        Returns:
            class object: v2.getSchedule.GetSchedule
        """
        from infapy.v2.getSchedule import GetSchedule
        return GetSchedule(self._v2,self._v2BaseURL,self._v2icSessionID)

    def getServerTime(self):
        """getServerTime returns all the activity logs from IICS in dict format

        Returns:
            List of dict: <Local Time of the IICS Server>
        """
        url=self._v2BaseURL + "/api/v2/server/serverTime"
        headers = {'Content-Type': "application/json", 'Accept': "application/json","icSessionID":self._v2icSessionID}
        infapy.log.info("getServerTime URL - " + url)
        infapy.log.info("API Headers: " + str(headers))
        infapy.log.info("Body: " + "This API requires no body")
        try:
            response = re.get(url=url, headers=headers)
            infapy.log.debug(str(response.json()))
        except Exception as e:
            infapy.log.exception(e)
            raise
        infapy.log.info("Fetched the Local Time of the IICS Server")
        data = response.json()
        return data

    def user(self):
        """This function returns an object of getUser
        which has multiple sub methods to fetch the details of IICS Users

        Returns:
            class object: v2.getUser.GetUser
        """
        from infapy.v2.user import User
        return User(self._v2,self._v2BaseURL,self._v2icSessionID)

    