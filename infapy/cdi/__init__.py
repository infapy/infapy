import infapy


class CDI():
    """CDI class is a wrapper class for all the IICS rest CDI APIs
    """

    def __init__(self,v3,v2,v2BaseURL,v3BaseURL,v3SessionID,v2icSessionID):
        """This class is used to leverage the IICS CDI APIs

        Args:
            v3 (json): login response of v3 login API
            v2 (json): login response of v2 login API
            v2BaseURL (string): The base url which we get from the v3 login API
            v3BaseURL (string): The base url which we get from the v2 login API
            v3SessionID (string): The SessionID from the v3 Login API
            v2icSessionID (string): The SessionID from the v2 Login API
        """

        infapy.log.info("created a v2 handler object successfully")
        infapy.log.info("v2BaseURL: " + v2BaseURL)
        self._v2=v2
        self._v2icSessionID = v2icSessionID
        self._v2BaseURL = v2BaseURL
        infapy.log.info("created a v3 handler object successfully")
        infapy.log.info("v3BaseURL: " + v3BaseURL)
        self._v3=v3
        self._v3SessionID = v3SessionID
        self._v3BaseURL = v3BaseURL

    def mttask(self):
        """This function returns an object of mttask
        which has multiple sub methods to fetch, create, update and delete mapping tasks in IICS

        Returns:
            class object: v3.mttask.MTTask
        """
        from infapy.cdi.mttask import MTTask
        return MTTask(self._v2,self._v2BaseURL,self._v2icSessionID)   