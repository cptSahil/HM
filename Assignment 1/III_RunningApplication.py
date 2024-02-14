import psutil
# import subprocess

def count_running_instances(processName):
   count = 0
   for proc in psutil.process_iter(['name']):
       if proc.info['name'] == processName:
           count += 1
           if count > 2:
               proc.kill()
   return count

def monitorApplications():
    for app in applications: 
        processName = app['processName']
        maxInstances = app['maxInstances']
        runningInstances = count_running_instances(processName)
        if runningInstances > maxInstances:
            print(f'Warning: More than {maxInstances} instances of {processName} running!') 
        else:
            print(f'{processName}: {runningInstances}/{maxInstances}')

applications = [
    {'processName': "chrome.exe",'maxInstances': 2},
    {'processName': "notepad.exe",'maxInstances': 2,},
    {'processName': "calc.exe",'maxInstances': 2},
    {'processName': "msedge.exe",'maxInstances': 2}
]

if __name__ == "__main__":
    monitorApplications()