import psutil

# Define a function to count the number of running instances of a specified process name
def count_running_instances(processName):
   count = 0 # initalize the count variable

   # Iterate through each Process in monitor
   for proc in psutil.process_iter(['name']):
       if proc.info['name'] == processName:
           count += 1

           # If the number of running instances exceeds the maximum allowed instances, kill the process
           if count > 2:
               proc.kill()
   return count

# Define a function to monitor the running instances of specified applications
def monitorApplications():
    for app in applications: 
        processName = app['processName']
        maxInstances = app['maxInstances']

         # Count the number of running instances of the application
        runningInstances = count_running_instances(processName)
        
        # If the number of running instances exceeds the maximum allowed instances, print a warning message
        if runningInstances > maxInstances:
            print(f'Warning: More than {maxInstances} instances of {processName} running!') 
         # Otherwise, print the number of running instances
        else:
            print(f'{processName}: {runningInstances}/{maxInstances}')

# Define a list of applications to monitor
applications = [
    {'processName': "chrome.exe",'maxInstances': 2},
    {'processName': "notepad.exe",'maxInstances': 2,},
    {'processName': "calc.exe",'maxInstances': 2},
    {'processName': "msedge.exe",'maxInstances': 2}
]

if __name__ == "__main__":
    monitorApplications()