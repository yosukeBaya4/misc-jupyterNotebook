import csv

data_list = []
for i in range(1,5):
				data = [h + str(i) for h in "ABC"]
				print(data)
				data_list.append(data)


with open("test.csv", mode= "w", encoding = "utf-8") as fp:
	csv_writer = csv.writer(fp, lineterminator="\n")
	csv_writer.writerows(data_list)

#end
