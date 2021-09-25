import infapy

infapy.setFileLogger(name="test",level="DEBUG")
infaHandler = infapy.connect()
#v2=infaHandler.v2()
#getActivityDetails = v2.getActivityLog().getAllActivityLog()

v3=infaHandler.v3()
# response = v3.lookup(path="Prashanth/TEST/MTT_MappingTask6",objectType="MTT")
# print(response)

# response = v3.lookup(id="6OZL5GLp1wckJzwhTG30kD")
# print(response)

# response = v3.users().getAllUsers()
# #print(response)

# response = v3.userRoles().getAllUserRoles()
# print(response)

# response = v3.userRoles().createNewUserRole(name="myTestRole",description="my test roles",privileges=["9Yz7DzpQAKThluCEpbUqmX"])
# print(response)
# response = v3.userRoles().getUserRoleByName(userRoleName="myTestRole")
# print(response)

# response = v3.userRoles().deleteUserrole(userRoleID="dZC5LWzDiEOhCvpmm0sQoN")

# response = v3.userGroups().getUserGroupByName(userGroupName="INFA_ADMIN")
# print(response)

# newUserGroup = {
#     "name" : "user_group_2",
#     "roles" : ["9aTuLGRQgHyjpftpLFj7Qg"],
#     "users" : ["42szaouMf0bg0yycPME0Up"]
# }
# response = v3.userGroups().createNewUserGroup(newUserGroup)
# print(response)
# response = v3.userGroups().deleteUserGroup(userGroupID="lmU6VcL89KQeoesayPISgD")
# print(response)


# response = v3.users().getUserByID(id="9MxOtB2ml0ycSRywxsaMON")
# print(response)

# # userProfile={"email": "test"}
# # response = v3.users().createNewUser(userProfileInJson=userProfile)
# # print(response)

# response = v3.users().deleteUser(userID="2ZIIk0G34wIhYMCJn0pC6P")
# print(response)

# response = v3.getSecurityLogs().getSecurityLogsForLastOneDay()
# print(response)

# query="entryTime>=\"2021-09-22T08:00:00.000Z\";entryTime<=\"2021-09-23T17:00:00.000Z\""
# response = v3.getSecurityLogs().getSecurityLogsByCustomQuery(query=query)
# print(response)

# response = v3.export().startExport(name="MyTestJobFromPython",ObjectId="fbCKyij8Te2blUUMCDR5EE")
# print(response)

# response = v3.exportObject().getStatusOfExportByExportID(exportID="2pfGdKsxqWVhgWZ0NWONQ6")
# print(response)

# response = v3.exportObject().getExportLogsByExportID(exportID="2pfGdKsxqWVhgWZ0NWONQ6")
# print(response)

# response = v3.exportObject().getExportZipFileByExportID(exportID="2pfGdKsxqWVhgWZ0NWONQ6")

qaHandle = infapy.connect(profile="QA")
# v3 = qaHandle.v3()
# reponse = v3.importObject().uploadZipToGetJobID()
# print(reponse)

jsonObject = {
    "name" : "ImportNameFromScript",
    "importSpecification" : {
        "defaultConflictResolution" : "OVERWRITE",
        "objectSpecification" : [
        {
            "sourceObjectId" : "848Au1yuOzAcdxJMgPkdqy",
            "targetObjectId" : "9YGTW8zLVaAb6O15bcjbyk"
        }]
    }
}

v3 = qaHandle.v3()
# response = v3.importObject().startImportByJobID(jobID="aRepcFrGOXZefm5zjz76C6",importBody=jsonObject)
# print(response)

response = v3.importObject().getStatusOfImportByImportID(importID="aRepcFrGOXZefm5zjz76C6")
print(response)
response = v3.importObject().getImportLogsByImportID(importID="aRepcFrGOXZefm5zjz76C6")
print(response)
# response = v3.importObject().getImportLogsByExportID(importID="gH4t81yTaMnd7XKWpgV64C")
# print(response)