# One day, many beautiful helper functions will live in this file.
# For now we are just loading data :)

# Python imports
import os
# My imports
import strain_class

def read_gisaid_file(filename):
    # This method reads the dna sequence from the file downloaded from NCBI and crates a python dictionary.
    datafile = open(filename,'r')
    file_contents = datafile.read().replace('\n', '')
    datafile.close()

    allData = {} # Use a dict for easy access :)

    # Index from 1 onwards because the first '>' throws things off a bit.
    segments = file_contents.split('>')[1:]
    for segment in segments:
        try:
            temp_name, temp_date, temp_segname, temp_segdata = segment.split('|')
            # We are using the name as a key.
            # If it doesn't exist, initialize it.
            if not temp_name in allData:
                tempStrain = strain_class.DnaData(temp_name, temp_date)
                allData[temp_name] = tempStrain
            allData[temp_name].segments[temp_segname] = temp_segdata
        except:
            print(f'Found bad data in {filename}')
    return allData

def get_all_data(directory="../sample_data", extension=".fasta"):
    allData = {}
    for file in os.listdir(directory):
        if file.endswith(extension):
            allData.update(read_gisaid_file(os.path.join(directory, file)))
    return allData
