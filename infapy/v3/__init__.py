import requests as re
import infapy
from infapy.exceptions import InvalidArgumentsError

# infapy.log = logging.getinfapy.log(__name__)

class V3():
    """V3 class is a wrapper class for all the IICS rest v2 APIs
    """
    def __init__(self,v3,v3BaseURL,v3SessionID):
        """This class is used to leverage the IICS V2 APIs

        Args:
            v3 (json): login response of v23 login API
            v3BaseURL (string): The base url which we get from the v3 login API
            v3SessionID (string): The SessionID from the v3 Login API
        """
        infapy.log.info("created a v2 handler object successfully")
        infapy.log.info("v3BaseURL: " + v3BaseURL)
        self._v3=v3
        self._v3SessionID = v3SessionID
        self._v3BaseURL = v3BaseURL
        
    def objects(self):
        """objects method returns a class objects used to fetch the object details
        like object ids, object dependency etc
        You can fetch the mapping task object dependecies, runtime env used etc
        Returns:
            Class Object of type objects  
        """
        from infapy.v3.objects import Objects
        return Objects(v3=self._v3,v3BaseURL=self._v3BaseURL,v3SessionID=self._v3SessionID)
    
    def lookup(self,id=None,path=None,objectType=None):
        """lookup api is used to fetch the object ID.

        Args:
            id ([str], required if path and object not provided): [description]. object id.
            path ([str], required if id not provided): [description]. ProjectFolder/SubFolder/mt_test
            objectType ([str], required if id not provided): [description]. Type of object, ex: MTT

        Raises:
            InvalidArgumentsError: if required arguments are not passed

        Returns:
            json: lookup of object
        """
        infapy.log.info("Performing lookup operation")
        idProvidedFlag=True
        try:
            if id is None:
                idProvidedFlag=False
                if (path is None) or (objectType is None):
                    infapy.log.error("You have not provided valid arguments for performing lookup")
                    infapy.log.error("Either provide id from v3.objects or provide the path and type")
                    infapy.log.info("Usage: v3.lookup(id=ID)")
                    infapy.log.info("Usage: v3.lookup(path=/path/to/object,type=ObjectType)")
                    raise InvalidArgumentsError
        except Exception as e:
            infapy.log.exception(e)
            raise
        
        url=self._v3BaseURL + "/public/core/v3/lookup"
        headers = {'Content-Type': "application/json", 'Accept': "application/json","INFA-SESSION-ID":self._v3SessionID}
        
        if idProvidedFlag:
            infapy.log.info("Using object id: " + id + " to perform lookup")
            body = {"objects": [{"id" : id}]}
        else:
            infapy.log.info("Using Path and type for object fetch")
            infapy.log.info("Path Provided: " + path)
            infapy.log.info("Object Type Provided: " + objectType)
            body = {"objects": [{"path": path,"type": objectType}]}
            infapy.log.info("Please note that if you are using path, you have to provide \nProjectFolder/SubFolder/MT_taskName")
        infapy.log.info("get lookup url - " + url)
        infapy.log.info("API Headers: " + str(headers))
        infapy.log.info("Body: " + str(body))
        
        # The below format is for post
        # bodyV3={"username": userName,"password": password}
        # r3 = re.post(url=urlV3, json=bodyV3, headers=headers)
        try:
            response = re.post(url=url, json=body, headers=headers)
            data = response.json()
            infapy.log.debug(data)
        except Exception as e:
            log.exception(e)
            raise

        infapy.log.info("Lookup completed")
        return data

    def users(self):
        from infapy.v3.users import Users
        return Users(V3=self._v3,v3BaseURL=self._v3BaseURL,v3SessionID=self._v3SessionID)