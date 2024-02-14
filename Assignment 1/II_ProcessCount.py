import psutil
import csv

# Get all processes
processes = psutil.process_iter()
processCount = {}

# Iterate through each process
for process in processes:
   processName = process.name()
   processCount[processName] = processCount.get(processName, 0) + 1
   
# Save process counts to a CSV file
with open('process_counts.csv', 'w', newline='') as csvfile:
   fieldnames = ['Process Name', 'Count']
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

   writer.writeheader()
   for processName, count in processCount.items():
       writer.writerow({'Process Name': processName, 'Count': count})
print("Process count information has been saved to process_counts.csv")