import csv

cnt = 0
data_list = []
data = []
for i in range(1,366):
    if i == 365:
        #print("END")
        data.append(i)
        data_list.append(data)
        break
    elif cnt != 6:
        # create block(list) named "data"
        data.append(i)
        cnt += 1
    elif cnt == 6:
        data.append(i)
        data_list.append(data)
        # reset counter and block
        cnt = 0
        data = []
        #print("Reset")


print(data_list)

    
# IDEA 
# set counter n, and use if-else-clause.
# when counter n reached to 7, append the list to data_list,
# and reset n to 0, and also reset data to emtpy list.



#with open("test.csv", mode= "w", encoding = "utf-8") as fp:
#	csv_writer = csv.writer(fp, lineterminator="\n")
#	csv_writer.writerows(data_list)

#end