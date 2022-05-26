def splitToDict(data_tmp):
    tmp = data_tmp.split(';')
    return tmp

def splitPhoto(tmp_jpg):
    tmp = tmp_jpg.split("||")
    return tmp

def linkolustur(fcode,photoUrl):
    return f"https://xxx.com/Library/Upl/{fcode}/Product/{photoUrl}"


def line_func(fCode,tmp_data):
    tmp_data = tmp_data.split('\n')[0]
    tmp_dict = splitToDict(tmp_data)
    tmp_photo = splitPhoto(tmp_dict[1])
    tmp_link_photo =""
    for pht in tmp_photo:
        if len(pht)>0:
            tmp_link_photo+=linkolustur(fCode,pht)+ "||"
    return tmp_dict[0] + ";" + tmp_link_photo

def main():
    lines = []
    list_out= []
    with open('sys_stock_card.csv') as f:
        lines = f.readlines()
    for line in lines:
        if "||" in line:
            list_out.append(line_func('firmakodugelecek',line))
        else:
            list_out.append(line.split('\n')[0])
    textfile = open("out_put_url.csv", "w")
    for element in list_out:
        textfile.write(element + "\n")
    textfile.close()

if __name__ == '__main__':
    main()

