import infapy

infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaHandler = infapy.connect(profile="spani")
v3=infaHandler.v3()

Schedule=v3.schedule()
# print(Schedule.getAllSchedules())
# print(Schedule.getScheduleById("9dMjYg78QCpewd7iS939IzD0000000000002"))
print(Schedule.getSchedulesWithQuery("status=='enabled' and createdBy=='admin021651'"))