import infapy

infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaHandler = infapy.connect(profile="spani")
v3=infaHandler.v3()

Schedule=v3.schedule()
# print(Schedule.getAllSchedules())
# print(Schedule.getScheduleById("9dMjYg78QCpewd7iS939IzD0000000000002"))
# print(Schedule.getSchedulesWithQuery("status=='enabled' and createdBy=='admin021651'"))
bodyv3= {
    "name": "TEST_SCHEDULE_API",
    "status": "enabled",
    "frequency": 15,
    "dayOfMonth": 0,
    "scheduleFederatedId": "9GROQi3ZyIufwF9yzLtx0I",
    "startTime": "2021-04-05T15:00:20.000Z",
    "interval": "Minutely"
}
print(Schedule.createSchedule(bodyv3))