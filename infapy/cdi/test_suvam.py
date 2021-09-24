import infapy


infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaHandler = infapy.connect(profile="spani")
cdi=infaHandler.cdi()

MTTask=cdi.mttask()
print(MTTask.getAllMTTasks())