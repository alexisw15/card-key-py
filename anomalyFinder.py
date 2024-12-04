import csv #needed to process the csv file.

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
        
        for row in rows: #go through all the rows that arent the header
            try:
                hourIn = int(row[hour_in_index])
                hourOut = int(row[hour_out_index])
                minIn = int(row[min_in_index])
                minOut = int(row[min_out_index])
                empNum = row[employee_num_index].strip()
                #make these into numbers that are easier to call and print out
                # strip on empNum means that we remove the whitespace for cleaner output
                if hourIn == 0 or hourOut == 0: #check for anomalies in clock in/out times. It's not normal to clock in or out at 0:0.
                    anomalies.append((empNum, hourIn, minIn, hourOut, minOut))
                    # adds these values to our list of anomalies
            except ValueError:
                print("error: stupid idiot disease detected!")
                        #have to have error handling just in case.
    #outputting the detected anomalies
    print("anomaly type 1: (clocked in/out at 0):  \n ") #named it type 1 because i thought there would be others.
    for i, anomaly in enumerate(anomalies, start=1):
        empNum, hourIn, minIn, hourOut, minOut = anomaly
        print(f"Anomaly {i}: Employee {empNum} - Time in: {hourIn}:{minIn} - Time out: {hourOut}:{minOut} ") #outputs formatted entry for each anomaly.
    else:
        print("Done.")
    
main()


#def main():
    #print("is this thing on")
    #print(csvData)
    #anomalyFinder1()

# with open('logs.csv', newline='') as csvfile:
#data = csv.reader(csvfile, delimiter = '\t')
 
