import psutil
import csv

processes = psutil.process_iter()
processCount = {}
for process in processes:
   processName = process.name()
   processCount[processName] = processCount.get(processName, 0) + 1
with open('process_counts.csv', 'w', newline='') as csvfile:
   fieldnames = ['Process Name', 'Count']
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

   writer.writeheader()
   for processName, count in processCount.items():
       writer.writerow({'Process Name': processName, 'Count': count})
print("Process count information has been saved to process_counts.csv")