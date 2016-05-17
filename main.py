import os
import pickle
import datetime
import time
import sys

if not os.path.exists("c:\py_schedular"):
        os.makedirs("c:\py_schedular")
        todo = []
        file_obj = open("c:\\py_schedular\\data.txt","wb")
        pickle.dump(todo,file_obj)
        file_obj.close()

def open_file(mode):
    return open("c:\py_schedular\data.txt",mode)

def show_tasks():
        file_obj = open_file('rb')
        todo = pickle.load(file_obj)
        file_obj.close()
        if todo:
            print("AvailableTasks :")
            for i,each_tuple in enumerate(todo):
                print("\nNumber "+str(i+1)+":")
                for each_element in each_tuple:
                    print(each_element)
                print("\n")
        else:
            print("\n\nNo Task Available At This Moment.\n\n")
 

def start():
    action = input("\n1-Create\n2-Delete\n3-View\n4-Quit\n>> ")
    main(action)
    
def main(action):  
    if action == '1':
        file_obj = open_file('rb')
        todo = pickle.load(file_obj)
        file_obj.close()
        
        task = input("\nName :\n>> ")
        desc = input("Description :\n>> ")
        creation_time = datetime.datetime.now().replace(second=0,microsecond=0)
        
        todo.append((task,desc,creation_time))        
        
        file_obj = open_file('wb')
        pickle.dump(todo,file_obj)
        file_obj.close()
        
        print("Task Created :)")
        time.sleep(4)
        start()
    
    if action == '2':
        show_tasks()
        time.sleep(2)
        op = int(input("Enter Number Of Task You Want To Delete."))
       
        file_obj = open_file('rb')
        todo = pickle.load(file_obj)
        file_obj.close()
        
        title = todo[op-1][0]
        delete = input("Do You Want To Delete "+title+"?\n[Y/N]\n>>").upper()        
            
        if delete == 'Y':
            deleted_task_detail = todo[op-1]
            todo.pop(op-1)
        else:
            time.sleep(2)
            start()   
        
        file_obj = open_file('wb')
        todo = pickle.dump(todo,file_obj)
        file_obj.close()
        
        print("Successfully Deleted..")
        comment = input("\nWrite Short Comment/Summery : \n>> ")
        time_of_destruction = datetime.datetime.now().replace(second=0,microsecond=0)
        diff_time = time_of_destruction-deleted_task_detail[2]
        
        print("\nIt Took "+str(diff_time.days)+" Days To Complete Task! :)")
        
        file_obj = open("c:\py_schedular\accomplishment.txt","a")
        
        file_obj.write("Name : "+deleted_task_detail[0]+"\n")
        file_obj.write("Description : "+deleted_task_detail[1]+"\n")
        file_obj.write("Created On : "+ str(deleted_task_detail[2])+"\n")
        file_obj.write("Completed On : "+ str(time_of_destruction)+"\n")
        file_obj.write("Time Taken : "+str(diff_time)+"\n")
        file_obj.write("Comment : "+comment+"\n"+"-"*40+"\n\n\n")
        
        
        file_obj.close()
        
        time.sleep(2)
        start()
    
    if action == '3':
       show_tasks()
       time.sleep(4)
       start()


    if  action == '4':   
        sys.exit()
        
if __name__ == "__main__":
    start()
