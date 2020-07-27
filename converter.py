import csv


def open_csv(path):
    # Check CSV file format
    if path.split(".")[1] != "csv":
        print("Only CSV files can be converted.")
        return
    try:
        return open(path)
    except FileNotFoundError:
        print("File Path Not Found")
        return


def vcfWriter(csvfilepath):
    # Read CSV file
    csvFile = open_csv(csvfilepath)
    if csvFile:
        csvReader = csv.reader(csvFile)
        csvData = list(csvReader)

        # Create the ouput file
        outputfilename = csvfilepath.split(".")[0] + ".vcf"
        outputFile = open(outputfilename, "w")
        vcardinfo = ""

        print("Convertion began.....")
        for row in range(len(csvData)):
            if row == 0:
                continue  # Skip the first row (headers)
            else:
                vcfLines = []
                vcfLines.append("BEGIN:VCARD")
                vcfLines.append("VERSION:4.0")
                vcfLines.append("FN:%s" % csvData[row][0])
                vcfLines.append("TEL;TYPE=VOICE,HOME;VALUE=text:%s" % csvData[row][1])
                vcfLines.append("END:VCARD")
                vcfString = "\n".join(vcfLines) + "\n"
                vcardinfo += vcfString

        outputFile.write(vcardinfo)
        outputFile.close()
        print("Converted Successfully !!!")


# Run the Main Function....
vcfWriter("sample_contacts.csv")
