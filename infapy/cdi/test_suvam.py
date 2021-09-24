import infapy


infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaHandler = infapy.connect(profile="spani")
cdi=infaHandler.cdi()

MTTask=cdi.mttask()
# print(MTTask.getAllMTTasks())
# print(MTTask.getMTTaskById("0119Y40Z00000000000O"))
print(MTTask.getMTTaskByName("MT_IU 2"))