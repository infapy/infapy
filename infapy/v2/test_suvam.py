from infapy.v2.jobControl import JobControl
import infapy

infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaHandler = infapy.connect(profile="spani")
v2=infaHandler.v2()
#getActivityDetails = v2.getActivityLog().getAllActivityLog()

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

# ActivityLog=v2.getActivityLog()
# print(ActivityLog.getAllActivityLog())
# print(ActivityLog.getActivityLogById("0119Y4C1000000000QEH"))
# print(ActivityLog.getActivityLogWithParams("2","2"))
# print(ActivityLog.getActivityLogWithParams())
# print(ActivityLog.getActivityLogWithParams(taskId="0119Y40Z00000000001S",runId="6"))
# open("C:\\Users\\spani\\Downloads/try.txt","w").write("hello")
# print(ActivityLog.getErrorLog("0119Y4C1000000000QPJ","C:\\Users\\spani\\Downloads"))
# print(ActivityLog.getErrorLog("0119Y4C1000000000QPJ","C:\\Users\\spani\\Downloads","try_Error.csv"))
# print(ActivityLog.getSessionLog("0119Y4C1000000000QPJ","C:\\Users\\spani\\Downloads"))
# print(ActivityLog.getSessionLog("0119Y4C1000000000QPJ","C:\\Users\\spani\\Downloads","s_mtt_0119Y40Z00000000001S"))
# print(ActivityLog.getSessionLog("0119Y4C1000000000QPK","C:\\Users\\spani\\Downloads",itemId="2752306096",childItemId="2752306099"))

# ActivityMonitor=v2.getActivityMonitor()
# print(ActivityMonitor.getActivityMonitorLog())
# print(ActivityMonitor.getActivityMonitorLog("true"))

# Agent=v2.getAgent()
# print(Agent.getAllAgentDetails())
# print(Agent.getInstallerToken("win64"))
# print(Agent.getAgentDetailsById("0119Y408000000000003"))
# print(Agent.getAgentDetailsByName("bolt informatica com"))
# print(Agent.getAllAgentServiceDetails())
# print(Agent.getAgentServiceDetailsById("0119Y408000000000003"))
# print(Agent.deleteAgent("0119Y408000000000008"))

# Agent=v2.getAuditLog()
# print(Agent.getAuditLogs("3","30"))

JobControl=v2.jobControl()
Job = {
    "@type": "job",
    "taskName": "MT_Warning",
    "taskType": "MTT"
}
# print(JobControl.startJob(Job))
print(JobControl.stopJob(Job))