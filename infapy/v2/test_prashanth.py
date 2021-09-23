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

response = v3.userGroups().getAllUserGroups()
# print(response)

response = v3.userGroups().getUserGroupByName(userGroupName="INFA_ADMIN")
print(response)

newUserGroup = {
    "name" : "user_group_2",
    "roles" : ["9aTuLGRQgHyjpftpLFj7Qg"],
    "users" : ["42szaouMf0bg0yycPME0Up"]
}
response = v3.userGroups().createNewUserGroup(newUserGroup)
print(response)


# response = v3.users().getUserByID(id="9MxOtB2ml0ycSRywxsaMON")
# print(response)

# # userProfile={"email": "test"}
# # response = v3.users().createNewUser(userProfileInJson=userProfile)
# # print(response)

# response = v3.users().deleteUser(userID="2ZIIk0G34wIhYMCJn0pC6P")
# print(response)