import pandas as pd 
import os 

def salary (data , i) :
    if data["salary"][i]<250 :
        return True
    else :
        return False

def num_person (data , i) :
    if data["#person"][i]>=2 :
        return True
    else :
        return False

def gender (data , i) :
    if data["gender"][i]=="f" :
        return True
    else :
        return False    

def desice (data , i) :
    if data["desice"][i]=="yes" :
        return True
    else :
        return False



file_name = input(" enter excel file name : ")
path = "C:\\Users\\share\\Desktop"
data  =pd.read_excel(path+"\\"+file_name+".xlsx")
filter_data = {"name" : [] , "number" : [] ,"location" : []}        
save_file_name = input(" enter folder name  to save: ")     

for i in range(0,len(data)) :
    if (salary(data,i) and num_person(data,i) and gender(data,i)  and desice(data,i)  ):
        filter_data["name"].append(data["name"][i])
        filter_data["number"].append(data["number"][i])
        filter_data["location"].append(data["location"][i])   
        
os.chdir(path)
os.mkdir(save_file_name)     
        
filter_data_frame = pd.DataFrame(filter_data)
filter_data_frame.to_excel(path+"\\"+save_file_name+"\\" +"output.xlsx")        
        
        