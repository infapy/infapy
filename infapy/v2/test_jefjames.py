from requests.models import Response, codes
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

# serverTime = v2.getServerTime()
# print(serverTime)

##########################################################################

# allUsersDetails = v2.getUser().getAllUsers()
# print("All Users Details:")
# print(allUsersDetails)

# userId = "000QML0300000000000P"
# userDetails = v2.getUser().getUserById(userId)
# print("User Details:")
# print(userDetails)

# userName = "Jeffline"
# userDetails = v2.getUser().getUserByName(userName)
# print("User Jeffline:")
# print(userDetails)

##########################################################################

# id = "0106LX";
# data = {
#     '@type': 'org',
#     'id': '0106LX',
#     'orgId': '0106LX',
#     'name': 'Infa-IIDIQ-POD2-suborg-1',
#     'description': '',
#     'createTime': '2018-07-05T00:13:10.000Z',
#     'updateTime': '2020-10-14T05:25:43.000Z',
#     'createdBy': 'idiq_prod_pod2',
#     'updatedBy': 'mosharma@informatica.com',
#     'address1': 'update',
#     'address2': '',
#     'address3': '',
#     'employees': '0_10',
#     'city': 'city',
#     'country': 'US',
#     'state': 'MD',
#     'zipcode': '90001',
#     'successEmails': '',
#     'warningEmails': '',
#     'errorEmails': '',
#     'spiUrl': 'https://paku.rt.informaticacloud.com/activevos',
#     'devOrg': 'false',
#     'timezone': 'America/Los_Angeles',
#     'maxLogRows': 100,
#     'minPasswordLength': 9,
#     'minPasswordCharMix': 3,
#     'passwordReuseInDays': 90,
#     'passwordExpirationInDays': 180,
#     'subOrgLimit': 0,
#     'restApiSessionLimit': 0,
#     'parentOrgId': '80bTjaasFejbEkQynNFnyT',
#     'subOrgs': [],
#     'twoFactorAuthentication': 'false',
#     'orgUUID': "6Q0z2tCamb1bfBWxQYCam9",
#     'ipAddressRanges': []
# }

# response = v2.org().updateSubOrgDetails(id,data)
# print(response)

# ##########################################################################

# userid = "000QML0300000000000V"
# data = {
#     '@type': 'user',
#     'id': '000QML0300000000000V',
#     'orgId': '000QML',
#     'name': 'CAI_Anonymous_80bTjaasFejbEkQynNFnyT',
#     'createTime': '2019-11-17T03:57:50.000Z',
#     'updateTime': '2021-09-24T10:23:19.004Z',
#     'createdBy': 'icrt',
#     'updatedBy': 'Jeffline',
#     'firstName': 'CAI',
#     'lastName': 'Anonymous',
#     'password': '********',
#     'emails': 'caianonymous@email.com',
#     'timezone': 'America/Los_Angeles',
#     'serverUrl': 'https://na2.dm-us.informaticacloud.com/saas',
#     'spiUrl': 'https://paku.rt.informaticacloud.com/activevos',
#     'forceChangePassword': 'false',
#     'uuid': '1HXerKm4R64hnJPCnrqZws',
#     'optOutOfEmails': 'false',
#     'usergroups': [],
#     'roles': [
#         {
#             '@type': 'role',
#             'name': 'Service Consumer',
#             'description': 'Role for running tasks, taskflows, and processes.'
#         }
#     ]
# }

# response1 = v2.user().updateUserDetails(userid, data)
# print(response1)

##########################################################################

# data = {
#     '@type' : 'registration',
#     'user' : {
#         '@type' : 'user',
#         'name' : 'jjtest',
#         'emails' : 'jefjames@informatica.com',
#         'firstName' : 'firstName',
#         'lastName' : 'lastName',
#         'title' : 'jobTitle',
#         'phone' : '(0)1234 567 890',
#         'timezone' : 'null',
#         'forceChangePassword' : 'false'
#     },
#     'org' : {
#         '@type' : 'org',
#         'offerCode' : 'PPC30daytrial', 
#         'campaignCode' : 'PPC',
#         'name' : 'testorg',
#         'address1' : '1 Main St',
#         'city' : 'Mycity',
#         'state' : 'CA',
#         'zipcode' : '90210',
#         'country' : 'US',
#         'employees' : '5001_'
#     },
#     'registrationCode' : 'ics-standard', 
#     'sendEmail' : 'true'
# }

# response = v2.org().registerSubOrg(data)
# print(response)

##########################################################################

# id = "000QML0300000000001K"

# userDetails = v2.user().getUserById(id)
# print(userDetails)

# respCode = v2.user().deleteUser(id)
# print(respCode)

# userDetails = v2.user().getUserById(id)
# print(userDetails)

##########################################################################
v3=infaHandler.v3()
sName = "OI Data Collector"
sAction = "stop"
agentId = "jGbv2pNa8qukzzKDNZsCI6"
response=v3.AgentService().updateAgentService(sName,sAction,agentId)
print(response)