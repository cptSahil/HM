import psutil
import csv

processCount = {}

# Get all processes
processes = psutil.process_iter()

# Iterate through each process
for proc in processes:
   processName = proc.name()
   processCount[processName] = processCount.get(processName, 0) + 1
   
# Save process counts to a CSV file
with open('process_counts.csv', 'w', newline='') as csvfile:
   fieldnames = ['Process Name', 'Count']
   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

   writer.writeheader()
   for processName, count in processCount.items():
       writer.writerow({'Process Name': processName, 'Count': count})
print("Process count information has been saved to process_counts.csv")