
import csv

def main():
    print("is this thing even on")
    with open('logs.csv', newline='') as csvfile:
        csvData = list(csv.reader(csvfile, delimiter = '\t'))
        
        header = csvData[0]
       
        rows = csvData[1:]
       
        employee_num_index = 0
        hour_in_index = 3
        hour_out_index = 7
        
        anomalies = []
        for row in rows:
            try:
                hourIn = int(row[hour_in_index])
                hourOut = int(row[hour_out_index])
                if hourIn == 0 or hourOut == 0:
                    anomalies.append(row)
            except ValueError:
                print("error: stupid idiot disease detected!!")

    print("anomaly type 1: (clocked out at 0):   ")
    for anomaly in anomalies:
        print (anomaly)
    



#def main():
    #print("is this thing on")
    #print(csvData)
    #anomalyFinder1()

# with open('logs.csv', newline='') as csvfile:
#data = csv.reader(csvfile, delimiter = '\t')
 
