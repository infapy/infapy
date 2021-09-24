import requests as re
import infapy

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
    
    def getActivityMonitor(self):
        """This function returns an object of getActivityMonitor
        which has sub method to fetch the activity log for running jobs

        Returns:
            class object: v2.getActivityMonitor.GetActivityMonitor
        """
        from infapy.v2.getActivityMonitor import GetActivityMonitor
        return GetActivityMonitor(self._v2,self._v2BaseURL,self._v2icSessionID)
    
    def getAgent(self):
        """This function returns an object of getAgent
        which has multiple sub methods to fetch details for agents in the org

        Returns:
            class object: v2.getAgent.GetAgent
        """
        from infapy.v2.getAgent import GetAgent
        return GetAgent(self._v2,self._v2BaseURL,self._v2icSessionID)

    def getAuditLog(self):
        """This function returns an object of getAuditLog
        which has sub method to fetch audit logs for the org

        Returns:
            class object: v2.getAgent.GetAuditLog
        """
        from infapy.v2.getAuditLog import GetAuditLog
        return GetAuditLog(self._v2,self._v2BaseURL,self._v2icSessionID)

    def jobControl(self):
        """This function returns an object of jobControl
        which has sub method to start/stop Jobs

        Returns:
            class object: v2.getAgent.JobControl
        """
        from infapy.v2.jobControl import JobControl
        return JobControl(self._v2,self._v2BaseURL,self._v2icSessionID)

    def taskList(self):
        """This function returns an object of taskList
        which has sub method to list tasks by type

        Returns:
            class object: v2.getAgent.TaskList
        """
        from infapy.v2.taskList import TaskList
        return TaskList(self._v2,self._v2BaseURL,self._v2icSessionID)