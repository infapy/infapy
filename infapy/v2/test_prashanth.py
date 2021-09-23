import infapy

infapy.setFileLogger(name="test",level="DEBUG")
infaHandler = infapy.connect()
#v2=infaHandler.v2()
#getActivityDetails = v2.getActivityLog().getAllActivityLog()

v3=infaHandler.v3()
response = v3.lookup(path="Prashanth/TEST/MTT_MappingTask6",objectType="MTT")
print(response)

response = v3.lookup(id="6OZL5GLp1wckJzwhTG30kD")
print(response)

response = v3.lookup(path="Prashanth/TEST/MTT_MappingTask6")
print(response)