import csv
print("test if it works")

def main():
    print("anomaly finder v1")
    #open CSV and tell it that it uses tabs and not commas
    with open('logs.csv') as csvfile:
        csvData = list(csv.reader(csvfile, delimiter = '\t'))
        #define what rows to read from
        header = csvData[0]
        rows = csvData[1:]
        
        #define what columns hold what data
        employee_num_index = 0
        hour_in_index = 3
        min_in_index = 4
        hour_out_index = 7
        min_out_index = 8
        #create list for anomalies
        anomalies = []
        
        for row in rows:
            try:
                hourIn = int(row[hour_in_index])
                hourOut = int(row[hour_out_index])
                minIn = int(row[min_in_index])
                minOut = int(row[min_out_index])
                empNum = row[employee_num_index].strip()

                #make these into numbers that are easier to call and print out
                
                if hourIn == 0 or hourOut == 0:
                    anomalies.append((empNum, hourIn, minIn, hourOut, minOut))
            except ValueError:
                print("error: stupid idiot disease detected!")
                        #just in case. you never know.
    
    print("anomaly type 1: (clocked out at 0):  \n ")
    for i, anomaly in enumerate(anomalies, start=1):
        empNum, hourIn, minIn, hourOut, minOut = anomaly
        print(f"Anomaly {i}: Employee {empNum} - Time in: {hourIn}:{minIn} - Time out: {hourOut}:{minOut} ")
    else:
        print("Done.")
    
main()


#def main():
    #print("is this thing on")
    #print(csvData)
    #anomalyFinder1()

# with open('logs.csv', newline='') as csvfile:
#data = csv.reader(csvfile, delimiter = '\t')
 
