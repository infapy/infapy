import infapy

infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaHandler = infapy.connect(profile="spani")
v3=infaHandler.v3()

Schedule=v3.schedule()
print(Schedule.getAllSchedules())