from infapy.v3.license import License
import infapy

infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaLicenseHandler = infapy.connect(profile="spani_parent")
v3_License=infaLicenseHandler.v3()
# infaHandler = infapy.connect(profile="spani")
# v3=infaHandler.v3()

# Schedule=v3.schedule()
# print(Schedule.getAllSchedules())
# print(Schedule.getScheduleById("9dMjYg78QCpewd7iS939IzD0000000000002"))
# print(Schedule.getSchedulesWithQuery("status=='enabled' and createdBy=='admin021651'"))
# bodyv3= {
#     "name": "TEST_SCHEDULE_API",
#     "status": "enabled",
#     "frequency": 15,
#     "dayOfMonth": 0,
#     "scheduleFederatedId": "9GROQi3ZyIufwF9yzLtx0I",
#     "startTime": "2021-04-05T15:00:20.000Z",
#     "interval": "Minutely"
# }
# print(Schedule.createSchedule(bodyv3))
# updateBody={
#     "schedules":[
#         {
#     "id": "9dMjYg78QCpewd7iS939IzD0000000000009",
#     "name": "TEST_SCHEDULE_API_V2",
#     "status": "disabled",
#     "frequency": 15,
#     "description": "V2 API",
#     "scheduleFederatedId": "9GROQi3ZyIufwF9yzLtx0I"
# }
#     ]
# }
# print(Schedule.updateSchedule(updateBody,"9dMjYg78QCpewd7iS939IzD0000000000009"))
# print(Schedule.deleteSchedule("9dMjYg78QCpewd7iS939IzD0000000000009"))

License=v3_License.license()
# print(License.getLicenseDetails("9dMjYg78QCpewd7iS939Iz"))