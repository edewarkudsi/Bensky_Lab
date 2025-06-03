import statistics
import matplotlib.pyplot as plt
import csv
id = '24h,5m'
timestamps = []
periods = []

# Open the CSV file
with open("/Users/elizabethdewar-kudsi/PyCharmMiscProject/555_time_interval_24h_5m.csv", mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if len(row) < 3:
            print(f"Skipping short row: {row}")
            continue
        try:
            time_val = float(row[1])
            period_val = float(row[2])
            timestamps.append(time_val)
            periods.append(period_val)
        except ValueError:
            print(f"Skipping invalid data: {row}")

r = []
num = []

for x in range(2, len(periods) + 1):
    num.append(x)
    r.append(statistics.stdev(periods[:x]))


plt.plot(num, r, "k.")
plt.xlabel("Number of Measurements")
plt.ylabel("Standard Deviation")
#plt.xlim([25,125])
#plt.ylim([5.5e-8,10e-7])
plt.title("288 samples ~1day 5 min delay")
plt.grid(True)
plt.show()

plt.savefig(f'555_time_interval_{id},num.png')

plt.plot(timestamps[1:], r, "k.")
plt.xlabel("Time [s]")
plt.ylabel("Standard Deviation")
#plt.xlim([50,10000])
#plt.ylim([5.5e-8,10e-7])
plt.title("288 samples ~1day 5 min delay")
plt.grid(True)
plt.show()

plt.savefig(f'555_time_interval_{id},time.png')

id = '24h,5m'
csv_filename = f'555_time_interval_{id}.csv'
with open(csv_filename,mode ='w', newline = '') as file:
     writer = csv.writer(file)
     writer.writerow(["sample #","time elapsed","standard deviation"])
     for i in range(len(r)):
        writer.writerow([num[i],timestamps[i],r[i]])

print(len(num), len(r), len(timestamps))
