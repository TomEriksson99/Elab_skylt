import requests

def get_apidata2(link_real):
    try:
            var = requests.get(link_real)
            data = var.json()
            respdata = data['ResponseData']
            #print(respdata)

            tbana = []
            tbana_data = respdata['Metros']
            for i in range(len(tbana_data)):
                temp = tbana_data[i]
                tbana_row = []
                tbana_row.append(temp['DisplayTime'])
                tbana_row.append(temp['Destination'])
                tbana.append(tbana_row)

            buss = []
            buss_data = respdata['Buses']
            for i in range(len(buss_data)):
                temp = buss_data[i]
                buss_row = []
                buss_row.append(temp['DisplayTime'])
                buss_row.append(temp['Destination'])
                buss_row.append(temp['LineNumber'])
                buss.append(buss_row)
            return [tbana, buss] 

    except TypeError:
        print(TypeError)
        pass
    except:
        pass

