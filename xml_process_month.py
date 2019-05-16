from bs4 import BeautifulSoup
import pandas as pd
import os 

def parse_location(location_item):
    stationid = location_item.stationid.string 
    locationname = location_item.locationname.string
    ele_name = [ele.string for ele in location_item.find_all('elementname')]
    # ele_value = [float(ele.string) for ele in location_item.find_all('value')]
    ele_value = []
    for ele in location_item.find_all("value"):
        try:
            ele_value.append(float(ele.string))
        except ValueError:
            ele_value.append(ele.string)
    df = {"stationid": stationid, "localname":locationname}
    df.update(dict(zip(ele_name,ele_value)))

    return df

def main():
    dirs = 'xml_weather/'
    filelist = os.listdir(dirs)
    print(filelist)
    for file in filelist:
        with open(dirs + file, 'r') as f:
            xml = f.read()

        # with open("xml_weather/2018-01.xml") as f:
        #     xml = f.read()
        print(f"{file} start")
        base = os.path.basename(file)
        soup = BeautifulSoup(xml,'lxml')
        location_data = soup.select('location')
        month_data = [parse_location(row) for row in location_data]
        
        month_data = pd.DataFrame(month_data)
        month_data.to_csv(f"csv_weather/{base}.csv", index=False)
        
if __name__ == "__main__":
    main()