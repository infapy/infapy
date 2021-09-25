import infapy


infapy.setFileLogger(name="test_Suvam",level="DEBUG")
infaHandler = infapy.connect(profile="spani")
cdi=infaHandler.cdi()

MTTask=cdi.mttask()
# print(MTTask.getAllMTTasks())
# print(MTTask.getMTTaskById("0119Y40Z00000000002P"))
# print(MTTask.getMTTaskByName("MT_IU 2"))
# createJSON={
#     "@type":"mtTask",
#     "name": "MT_IU_v2",
#     "containerId": "9wKUcCBrrb1kTpMB2G94UM",
#     "description": "IN DEFAULA FOLDER",
#     "runtimeEnvironmentId": "0119Y425000000000003",
#     "mappingId": "0119Y417000000000011",
#     "sessionProperties": {},
#     "enableCrossSchemaPushdown": True,
#     "enableParallelRun": False,
#     "autoTunedApplied": False,
#     "autoTunedAppliedType": "NONE",
#     "paramFileType": "PARAM_FILE_LOCAL",
#     "schemaMode": "async",
#     "parameterFileEncoding": "UTF-8",
#     "serverlessProperties": {},
#     "parameters": [
#         {
#             "@type": "mtTaskParameter",
#             "id": 362430283,
#             "name": "$Source$",
#             "type": "EXTENDED_SOURCE",
#             "label": "Source",
#             "uiProperties": {
#                 "connectionParameterized": "False",
#                 "isMsrcFilterParameterized": "False",
#                 "isMsrcSortParameterized": "False",
#                 "objectParameterized": "False",
#                 "visible": "False"
#             },
#             "sourceConnectionId": "0119Y40B000000000004",
#             "newFlatFile": False,
#             "newObject": False,
#             "showBusinessNames": False,
#             "naturalOrder": True,
#             "truncateTarget": False,
#             "bulkApiDBTarget": False,
#             "srcFFAttrs": {
#                 "@type": "flatFileAttrs",
#                 "id": 45053425,
#                 "delimiter": ",",
#                 "textQualifier": "\"",
#                 "escapeChar": "",
#                 "headerLineNo": 1,
#                 "firstDataRow": 2
#             },
#             "customFuncCfg": {
#                 "@type": "customFuncConfig",
#                 "id": -1,
#                 "connections": [],
#                 "inputMap": [],
#                 "outputFields": []
#             },
#             "tgtFieldRefs": {},
#             "targetUpdateColumns": [],
#             "extendedObject": {
#                 "@type": "extendedObject",
#                 "object": {
#                     "@type": "mObject",
#                     "name": "src_HS.csv",
#                     "label": "src_HS.csv",
#                     "metadataUpdated": False,
#                     "relations": [],
#                     "children": []
#                 },
#                 "objects": [
#                     {
#                         "@type": "mObject",
#                         "name": "src_HS.csv",
#                         "label": "src_HS.csv",
#                         "metadataUpdated": False,
#                         "relations": [],
#                         "children": []
#                     }
#                 ],
#                 "filters": [],
#                 "sortFields": []
#             },
#             "runtimeAttrs": {},
#             "isRESTModernSource": True,
#             "isFileList": False,
#             "handleSpecialChars": False,
#             "frsAsset": False,
#             "dynamicFileName": False,
#             "currentlyProcessedFileName": False,
#             "tgtObjectAttributes": {},
#             "runtimeParameterData": {
#                 "@type": "mtTaskRuntimeParameterData",
#                 "isConnectionRuntimeParameter": False,
#                 "isObjectRuntimeParameter": False
#             },
#             "overriddenFields": []
#         },
#         {
#             "@type": "mtTaskParameter",
#             "id": 362430286,
#             "name": "$Target$",
#             "type": "TARGET",
#             "label": "Target",
#             "uiProperties": {
#                 "connectionParameterized": "False",
#                 "objectParameterized": "False",
#                 "visible": "False",
#                 "defaultTargetUpdateColumns": "",
#                 "supportApplyDDLChanges": "True"
#             },
#             "targetConnectionId": "0119Y40B000000000004",
#             "targetObject": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "targetObjectLabel": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "newFlatFile": False,
#             "newObject": True,
#             "showBusinessNames": False,
#             "naturalOrder": True,
#             "newObjectName": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "truncateTarget": False,
#             "bulkApiDBTarget": False,
#             "operationType": "Insert",
#             "tgtFFAttrs": {
#                 "@type": "flatFileAttrs",
#                 "id": 45053428,
#                 "delimiter": ",",
#                 "textQualifier": "none",
#                 "escapeChar": "",
#                 "headerLineNo": 1
#             },
#             "customFuncCfg": {
#                 "@type": "customFuncConfig",
#                 "id": -1,
#                 "connections": [],
#                 "inputMap": [],
#                 "outputFields": []
#             },
#             "tgtFieldRefs": {},
#             "targetUpdateColumns": [],
#             "extendedObject": {
#                 "@type": "extendedObject",
#                 "filters": [],
#                 "sortFields": []
#             },
#             "runtimeAttrs": {},
#             "isRESTModernSource": True,
#             "isFileList": False,
#             "handleSpecialChars": False,
#             "frsAsset": False,
#             "dynamicFileName": False,
#             "currentlyProcessedFileName": False,
#             "objectName": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "objectLabel": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "tgtObjectAttributes": {},
#             "runtimeParameterData": {
#                 "@type": "mtTaskRuntimeParameterData",
#                 "isConnectionRuntimeParameter": False,
#                 "isObjectRuntimeParameter": False
#             },
#             "overriddenFields": []
#         },
#         {
#             "@type": "mtTaskParameter",
#             "id": 362430289,
#             "name": "$HierarchyBuilder$",
#             "type": "HSCHEMA",
#             "label": "HierarchyBuilder",
#             "uiProperties": {
#                 "visible": "False"
#             },
#             "newFlatFile": False,
#             "newObject": False,
#             "showBusinessNames": True,
#             "naturalOrder": True,
#             "truncateTarget": False,
#             "bulkApiDBTarget": False,
#             "customFuncCfg": {
#                 "@type": "customFuncConfig",
#                 "id": -1,
#                 "connections": [],
#                 "inputMap": [],
#                 "outputFields": []
#             },
#             "tgtFieldRefs": {},
#             "targetUpdateColumns": [],
#             "runtimeAttrs": {},
#             "isRESTModernSource": True,
#             "isFileList": False,
#             "handleSpecialChars": False,
#             "frsAsset": False,
#             "dynamicFileName": False,
#             "currentlyProcessedFileName": False,
#             "tgtObjectAttributes": {},
#             "runtimeParameterData": {
#                 "@type": "mtTaskRuntimeParameterData",
#                 "isConnectionRuntimeParameter": False,
#                 "isObjectRuntimeParameter": False
#             },
#             "overriddenFields": []
#         }
#     ],
#     "sequences": [],
#     "inOutParameters": [],
#     "connRuntimeAttrs": []
# }
# print(MTTask.createMTTask(createJSON))
# updateFullJSON={
#     "@type":"mtTask",
#     "name": "MT_IU_v3",
#     "containerId": "9wKUcCBrrb1kTpMB2G94UM",
#     "description": "NEW_DESCRIPTION",
#     "runtimeEnvironmentId": "0119Y425000000000003",
#     "mappingId": "0119Y417000000000011",
#     "sessionProperties": {},
#     "enableCrossSchemaPushdown": True,
#     "enableParallelRun": False,
#     "autoTunedApplied": False,
#     "autoTunedAppliedType": "NONE",
#     "paramFileType": "PARAM_FILE_LOCAL",
#     "schemaMode": "async",
#     "parameterFileEncoding": "UTF-8",
#     "serverlessProperties": {},
#     "parameters": [
#         {
#             "@type": "mtTaskParameter",
#             "id": 362430283,
#             "name": "$Source$",
#             "type": "EXTENDED_SOURCE",
#             "label": "Source",
#             "uiProperties": {
#                 "connectionParameterized": "False",
#                 "isMsrcFilterParameterized": "False",
#                 "isMsrcSortParameterized": "False",
#                 "objectParameterized": "False",
#                 "visible": "False"
#             },
#             "sourceConnectionId": "0119Y40B000000000004",
#             "newFlatFile": False,
#             "newObject": False,
#             "showBusinessNames": False,
#             "naturalOrder": True,
#             "truncateTarget": False,
#             "bulkApiDBTarget": False,
#             "srcFFAttrs": {
#                 "@type": "flatFileAttrs",
#                 "id": 45053425,
#                 "delimiter": ",",
#                 "textQualifier": "\"",
#                 "escapeChar": "",
#                 "headerLineNo": 1,
#                 "firstDataRow": 2
#             },
#             "customFuncCfg": {
#                 "@type": "customFuncConfig",
#                 "id": -1,
#                 "connections": [],
#                 "inputMap": [],
#                 "outputFields": []
#             },
#             "tgtFieldRefs": {},
#             "targetUpdateColumns": [],
#             "extendedObject": {
#                 "@type": "extendedObject",
#                 "object": {
#                     "@type": "mObject",
#                     "name": "src_HS.csv",
#                     "label": "src_HS.csv",
#                     "metadataUpdated": False,
#                     "relations": [],
#                     "children": []
#                 },
#                 "objects": [
#                     {
#                         "@type": "mObject",
#                         "name": "src_HS.csv",
#                         "label": "src_HS.csv",
#                         "metadataUpdated": False,
#                         "relations": [],
#                         "children": []
#                     }
#                 ],
#                 "filters": [],
#                 "sortFields": []
#             },
#             "runtimeAttrs": {},
#             "isRESTModernSource": True,
#             "isFileList": False,
#             "handleSpecialChars": False,
#             "frsAsset": False,
#             "dynamicFileName": False,
#             "currentlyProcessedFileName": False,
#             "tgtObjectAttributes": {},
#             "runtimeParameterData": {
#                 "@type": "mtTaskRuntimeParameterData",
#                 "isConnectionRuntimeParameter": False,
#                 "isObjectRuntimeParameter": False
#             },
#             "overriddenFields": []
#         },
#         {
#             "@type": "mtTaskParameter",
#             "id": 362430286,
#             "name": "$Target$",
#             "type": "TARGET",
#             "label": "Target",
#             "uiProperties": {
#                 "connectionParameterized": "False",
#                 "objectParameterized": "False",
#                 "visible": "False",
#                 "defaultTargetUpdateColumns": "",
#                 "supportApplyDDLChanges": "True"
#             },
#             "targetConnectionId": "0119Y40B000000000004",
#             "targetObject": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "targetObjectLabel": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "newFlatFile": False,
#             "newObject": True,
#             "showBusinessNames": False,
#             "naturalOrder": True,
#             "newObjectName": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "truncateTarget": False,
#             "bulkApiDBTarget": False,
#             "operationType": "Insert",
#             "tgtFFAttrs": {
#                 "@type": "flatFileAttrs",
#                 "id": 45053428,
#                 "delimiter": ",",
#                 "textQualifier": "none",
#                 "escapeChar": "",
#                 "headerLineNo": 1
#             },
#             "customFuncCfg": {
#                 "@type": "customFuncConfig",
#                 "id": -1,
#                 "connections": [],
#                 "inputMap": [],
#                 "outputFields": []
#             },
#             "tgtFieldRefs": {},
#             "targetUpdateColumns": [],
#             "extendedObject": {
#                 "@type": "extendedObject",
#                 "filters": [],
#                 "sortFields": []
#             },
#             "runtimeAttrs": {},
#             "isRESTModernSource": True,
#             "isFileList": False,
#             "handleSpecialChars": False,
#             "frsAsset": False,
#             "dynamicFileName": False,
#             "currentlyProcessedFileName": False,
#             "objectName": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "objectLabel": "'T_IU_'||Reg_Extract(op_xml, '((.|\\n)*)(<provider-id>)([^<]*)((.|\\n)*)', 4) ||'_'||  To_Char(SYSDATE,'YYYYMMDD')  ||'.xml'",
#             "tgtObjectAttributes": {},
#             "runtimeParameterData": {
#                 "@type": "mtTaskRuntimeParameterData",
#                 "isConnectionRuntimeParameter": False,
#                 "isObjectRuntimeParameter": False
#             },
#             "overriddenFields": []
#         },
#         {
#             "@type": "mtTaskParameter",
#             "id": 362430289,
#             "name": "$HierarchyBuilder$",
#             "type": "HSCHEMA",
#             "label": "HierarchyBuilder",
#             "uiProperties": {
#                 "visible": "False"
#             },
#             "newFlatFile": False,
#             "newObject": False,
#             "showBusinessNames": True,
#             "naturalOrder": True,
#             "truncateTarget": False,
#             "bulkApiDBTarget": False,
#             "customFuncCfg": {
#                 "@type": "customFuncConfig",
#                 "id": -1,
#                 "connections": [],
#                 "inputMap": [],
#                 "outputFields": []
#             },
#             "tgtFieldRefs": {},
#             "targetUpdateColumns": [],
#             "runtimeAttrs": {},
#             "isRESTModernSource": True,
#             "isFileList": False,
#             "handleSpecialChars": False,
#             "frsAsset": False,
#             "dynamicFileName": False,
#             "currentlyProcessedFileName": False,
#             "tgtObjectAttributes": {},
#             "runtimeParameterData": {
#                 "@type": "mtTaskRuntimeParameterData",
#                 "isConnectionRuntimeParameter": False,
#                 "isObjectRuntimeParameter": False
#             },
#             "overriddenFields": []
#         }
#     ],
#     "sequences": [],
#     "inOutParameters": [],
#     "connRuntimeAttrs": []
# }
# print(MTTask.updateMTTaskFull(updateFullJSON,"0119Y40Z00000000002P"))
# updatePartialJSON={
#     "@type":"mtTask",
#     "description": "NEW DESCRIPTION V2"
# }
# print(MTTask.updateMTTaskPartial(updatePartialJSON,"0119Y40Z00000000002P"))
print(MTTask.deleteMTTask("0119Y40Z00000000002P"))