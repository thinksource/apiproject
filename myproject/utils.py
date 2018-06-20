import csv
import codecs
import io
class csvParser:
    columns_mapping={'Name':'name','Type':'type','Maximum Rabi Rate':'maximum_rabi_rate','Polar Angle':'polar_angle'}
    dictkeys=['name','type','maximum_rabi_rate','polar_angle']

    @staticmethod
    def readercsv(file):
        dialect = csv.Sniffer().sniff(io.StringIO(file.read().decode('utf-8')).read(1024))
        file.open() #seek to 0
        reader = csv.DictReader(io.StringIO(file.read().decode('utf-8')),dialect=dialect)
        dict_list = []
        re=[]
        for line in reader:
            print(line)
            dict_list.append(line)
        
        for item in dict_list:
            newmap=dict()
            for key in item:
                newmap[csvParser.columns_mapping[key]]=item[key]

            re.append(newmap)
        
        return re

    @staticmethod
    def writecsv(dict_items, csvfile):
        writer=csv.DictWriter(csvfile, fieldnames=csvParser.dictkeys)
        
        for item in dict_items:
            writer.writerow(item)

        return csvfile 