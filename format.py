import os 
import json
# import pandas as pd
# cols = ['Zip']
# lst = []
count=0
check=""
f = open('test.json') 
data = json.load(f)
for key,value in data.items():
    if(isinstance(value,list)):
        for entry in value:
            for key1,value1 in entry.items():
                if(isinstance(value1,dict)):
                    if(key1=='resource'):
                        check=value1['resourceType']
                        # print(check)
                        if(check=='Patient'):
                            for key2,value2 in value1.items():
                                if(isinstance(value2,dict)):
                                    for key3,value3 in value2.items():
                                        if(isinstance(value3,list)):
                                            if(key3=='coding'):
                                                for coding in value3:
                                                    for key4,value4 in coding.items():
                                                        # print(key4,":",value4)
                                                            continue
                                            elif(key3=='profile'):
                                                # for profile in value3:
                                                # print(value3[0])
                                                continue
                                            else:
                                                continue     
                                        else:
                                            # print(key3,":",value3)
                                            continue
                                elif(isinstance(value2,list)):
                                    if(key2=='extension'):
                                        for extension in value2:
                                            for key3,value3 in extension.items():
                                                if(isinstance(value3,dict)):
                                                    for key4,value4 in value3.items():
                                                        # print(key4,value4)
                                                        continue
                                                elif(isinstance(value3,list)):
                                                    if(key3=='extension'):
                                                        for extension in value3:
                                                            for key5,value5 in extension.items():
                                                                if(isinstance(value5,dict)):
                                                                    for key6,value6 in value5.items():
                                                                        # print(key6,":",value6)
                                                                        continue
                                                                else:
                                                                    # print(key5,":",value5)
                                                                    continue
                                                else:
                                                    # print(key3,":",value3)
                                                    continue
                                    elif(key2=='identifier'):  
                                        for identifier in value2:
                                            for key3,value3 in identifier.items():
                                                if(isinstance(value3,dict)):
                                                    for key4,value4 in value3.items():
                                                        if(isinstance(value4,list)):
                                                            for coding in value4:
                                                                for key5,value5 in coding.items():
                                                                    # print(key5,":",value5)
                                                                    continue
                                                        else:
                                                            # print(key4,":",value4)
                                                            continue
                                                else:
                                                    # print(key3,":",value3)
                                                    continue
                                    elif(key2=='name'):  
                                        if(isinstance(value2,list)):
                                            for name in value2:
                                                for key3,value3 in name.items():
                                                    if(isinstance(value3,list)):
                                                        # print(key3,":",value3[0])
                                                        continue
                                                    else:
                                                        # print(key3,":",value3)
                                                        continue
                                        continue 
                                    elif(key2=='telecom'):  
                                        if(isinstance(value2,list)):
                                            for telecom in value2:
                                                for key3,value3 in telecom.items():
                                                    # print(key3,":",value3)
                                                    continue 
                                    elif(key2=='address'): 
                                        for address in value2:
                                            for key3,value3 in address.items():
                                                if(isinstance(value3,list)):
                                                    if(key3=='extension'):
                                                        for extensions in value3:
                                                            for key4,value4 in extensions.items():
                                                                if(isinstance(value4,list)):
                                                                    for extension in value4:
                                                                        for key5,value5 in extension.items():
                                                                            # print(key5,":",value5)
                                                                            continue
                                                                else:
                                                                    # print(key4,":",value4)
                                                                    continue
                                                    if(key3=='line'):
                                                        # print(key3,":",value3[0])
                                                        continue
                                                    else: 
                                                        continue
                                                else:
                                                    # print(key3,":",value3)
                                                    continue
                                        continue 
                                    elif(key2=='communication'):  
                                         for communication in value2:
                                            for key3,value3 in communication.items():
                                                if(isinstance(value3,dict)):
                                                    if(key3=='language'):
                                                        for key4,value4 in value3.items():
                                                            if(isinstance(value4,list)):
                                                                for coding in value4:
                                                                    for key5,value5 in coding.items():
                                                                        # print(key5,":",value5)
                                                                        continue
                                                            else:
                                                                # print(key4,":",value4)
                                                                continue
                                                else:
                                                    # print(key3,":",value3)
                                                    continue
                                    else:
                                        continue            
                                else:
                                    continue
                        elif(check=='Encounter'):
                            for key2,value2 in value1.items():
                                if(isinstance(value2,dict)):
                                    for key3,value3 in value2.items():
                                        if(isinstance(value3,list)):
                                            # print(key3,":",value3[0])
                                            continue
                                        else:
                                            # print(key3,":",value3)
                                            continue
                                if(isinstance(value2,list)):
                                    if(key2=='identifier'):
                                        for identifier in value2:
                                            for key3,value3 in identifier.items():
                                                # print(key3,":",value3)
                                                continue
                                    elif(key2=='type'):
                                        for types in value2:
                                            for key3,value3 in types.items():
                                                if(isinstance(value3,list)):
                                                    for coding in value3:
                                                        for key4,value4 in coding.items():
                                                            # print(key4,":",value4)
                                                            continue
                                                else:
                                                    # print(key3,":",value3)
                                                    continue
                                    elif(key2=='participant'):
                                        for participant in value2:
                                            for key3,value3 in participant.items():
                                                if(isinstance(value3,dict)):
                                                    for key4,value4 in value3.items():
                                                        # print(key4,":",value4)
                                                        continue
                                                elif(isinstance(value3,list)):
                                                    for types in value3:
                                                        for key4,value4 in types.items():
                                                            if(isinstance(value4,list)):
                                                                for coding in value4:
                                                                    for key5,value5 in coding.items():
                                                                        # print(key5,":",value5)
                                                                        continue
                                                            else:
                                                                # print(key4,":",value4)
                                                                continue    
                                                else:
                                                    continue
                                    elif(key2=='location'):
                                        for location in value2:
                                            for key3,value3 in location.items():
                                                if(isinstance(value3,dict)):
                                                    for key4,value4 in value3.items():
                                                        # print(key4,":",value4)
                                                        continue
                                                else:
                                                    continue
                                    elif(key2=='reasonCode'):
                                        for reasonCode in value2:
                                            for key3,value3 in reasonCode.items():
                                                if(isinstance(value3,list)):
                                                    for coding in value3:
                                                        for key4,value4 in coding.items():
                                                            # print(key4,":",value4)
                                                            continue
                                                else:
                                                    continue
                                    else:
                                        continue
                                else:
                                    # print(key2,":",value2)
                                    continue            
                        elif(check=='Condition'):
                            for key2,value2 in value1.items():
                                if(isinstance(value2,dict)):
                                    for key3,value3 in value2.items():
                                        if(isinstance(value3,list)):
                                            for coding in value3:
                                                if(isinstance(coding,dict)):
                                                    for key4,value4 in coding.items():
                                                        # print(key4,":",value4)
                                                        continue
                                                else:
                                                    if(key3=='profile'):
                                                        # print(key3,":",value3[0])
                                                        continue
                                                    else:
                                                        # print(key3,":",value3)
                                                        continue
                                        else:
                                            # print(key3,":",value3)
                                            continue
                                    pass
                                elif(isinstance(value2,list)):
                                    for category in value2:
                                        for key3,value3 in category.items():
                                            for coding in value3:
                                                for key4,value4 in coding.items():
                                                    # print(key4,":",value4)
                                                    continue
                                else:
                                    # print(key2,":",value2)
                                    continue
                        elif(check=='DiagnosticReport'):
                            for key2,value2 in value1.items():
                                if(isinstance(value2,dict)):
                                    for key3,value3 in value2.items():
                                        if(isinstance(value3,list)):
                                            for coding in value3:
                                                if(isinstance(coding,dict)):
                                                    for key4,value4 in coding.items():
                                                        # print(key4,":",value4)
                                                        continue
                                                else:
                                                    if(key3=='profile'):
                                                        # print(key3,":",value3[0])
                                                        continue
                                                    else:
                                                        continue

                                        else:
                                            # print(key3,":",value3)
                                            continue
                                    continue
                                elif(isinstance(value2,list)):
                                    if(key2=='category'):
                                        for category in value2:
                                            for key3,value3 in category.items():
                                                for coding in value3:
                                                    for key4,value4 in coding.items():
                                                        # print(key4,":",value4)
                                                        continue
                                    elif(key2=='performer'):
                                        for performer in value2:
                                            for key3,value3 in performer.items():
                                                # print(key3,":",value3)
                                                continue
                                    elif(key2=='presentedForm'):
                                        for presentedForm in value2:
                                            for key3,value3 in presentedForm.items():
                                                # print(key3,":",value3)
                                                continue
                                    elif(key2=='result'):
                                        for result in value2:
                                            for key3,value3 in result.items():
                                                # print(key3,":",value3)
                                                continue
                                    else:
                                        continue
                                else:
                                    # print(key2,":",value2)
                                    continue
                        elif(check=='DocumentReference'):
                            break
                        elif(check=='Claim'):
                            break
                        elif(check=='ExplanationOfBenefit'):
                            break
                        elif(check=='Observation'):
                            break
                        elif(check=='Procedure'):
                            break
                        elif(check=='Immunization'):
                            break
                        elif(check=='MedicationRequest'):
                            break
                        elif(check=='MedicationAdministration'):
                            break
                        elif(check=='Medication'):
                            break
                        elif(check=='ImagingStudy'):
                            break
                        elif(check=='CareTeam'):
                            break
                        elif(check=='CarePlan'):
                            break
                        elif(check=='Provenance'):
                            break
                        else:
                            break

        break                   


# f.close()


 

