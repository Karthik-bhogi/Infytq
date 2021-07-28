'''
Created on Apr 23, 2021

@author: Karthik
'''
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    pat_id=[]
    pat_vis=[]
    for i in range(len(patient_medical_speciality_list)):
        if i%2==0:
            pat_id.append(patient_medical_speciality_list[i])
        else:
            pat_vis.append(patient_medical_speciality_list[i])
    
    a=pat_vis.count('P')
    b=pat_vis.count('O')
    c=pat_vis.count('E')
    
    if a>b and a>c:
        return(medical_speciality['P'])
    elif b>a and b>c:
        return(medical_speciality['O'])
    else:
        return(medical_speciality['E'])
   
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)