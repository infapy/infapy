import infapy

infapy.setFileLogger(name="test",level="DEBUG")
infaHandler = infapy.connect(profile="jefjames")
v2=infaHandler.v2()

# orgDetails = v2.getOrg().getOrgDetails()
# print("Org Details:")
# print(orgDetails)

# subOrgId = orgDetails[0]["subOrgs"][0]["id"]
# subOrgDetails = v2.getOrg().getSubOrgDetailsById(subOrgId)
# print("SubOrg Details:")
# print(subOrgDetails)

# subOrgName1 = orgDetails[0]["subOrgs"][0]["name"]
# subOrgName2 = orgDetails[0]["subOrgs"][1]["name"]
# subOrgDetails1 = v2.getOrg().getSubOrgDetailsByName(subOrgName1)
# print("SubOrg 1:")
# print(subOrgDetails1)
# subOrgDetails2 = v2.getOrg().getSubOrgDetailsByName(subOrgName2)
# print("SubOrg 2:")
# print(subOrgDetails2)

##########################################################################

# allrunEnvDetails = v2.getRuntimeEnvironment().getAllRuntimeEnvironments()
# print("All Runtime Environments Details:")
# print(allrunEnvDetails)

# runEnvId = "000QML2500000000002Z"
# runEnvDetails = v2.getRuntimeEnvironment().getRuntimeEnvironmentById(runEnvId)
# print("Runtime Environment Details:")
# print(runEnvDetails)

# runEnvName1 = "Kronos IICS Agent"
# runEnvName2 = "1_EM08"
# subOrgDetails1 = v2.getRuntimeEnvironment().getRuntimeEnvironmentByName(runEnvName1)
# print("Runtime Environment 1:")
# print(subOrgDetails1)
# subOrgDetails2 = v2.getRuntimeEnvironment().getRuntimeEnvironmentByName(runEnvName2)
# print("Runtime Environment 2:")
# print(subOrgDetails2)

##########################################################################

# allSchedulesDetails = v2.getSchedule().getAllSchedules()
# print("All Schedules Details:")
# print(allSchedulesDetails)

# scheduleId = "000QMLD0000000000002"
# scheduleDetails = v2.getSchedule().getScheduleById(scheduleId)
# print("Schedule Details:")
# print(scheduleDetails)

# scheduleName1 = "JJ_10min"
# scheduleName2 = "every 5 mins"
# scheduleDetails1 = v2.getSchedule().getScheduleByName(scheduleName1)
# print("Schedule 1:")
# print(scheduleDetails1)
# scheduleDetails2 = v2.getSchedule().getScheduleByName(scheduleName2)
# print("Schedule 2:")
# print(scheduleDetails2)

##########################################################################

serverTime = v2.getServerTime()
print(serverTime)

##########################################################################
# v3=infaHandler.v3()
# queryString="location=='Prashanth/infapy'"
# objectDetails=v3.objects().getObjectID(q=queryString)
# # print(objectDetails)
# myMTTObject = objectDetails["objects"][1]["id"]
# # print(myMTTObject)

# objectDependencies = v3.objects().getObjectDependency(objectID=myMTTObject)
# print(objectDependencies)

# for eachDependenecy in objectDependencies["references"]:
#     print()
#     print("*****************************************")
#     print(eachDependenecy)
#     print("*****************************************")
#     print()

