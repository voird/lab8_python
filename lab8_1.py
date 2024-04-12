import xmltodict


def check_tags(check, dct_c):
    tag_public_transport = {}
    tag_public_transport_adress = {}
    for ch in dct_c['osm'][check]:
        if 'tag' in ch:
            tags = ch['tag']
            if isinstance(tags, list):
                for tag in tags:
                    if tag['@k'] == 'public_transport':
                        for tag_ad in tags:
                            if tag_ad['@k'] == 'name':
                                tag_public_transport_adress[tag_ad['@v']] = tag['@v']
                                break 

                        if not tag_public_transport.get(tag['@v']):
                            tag_public_transport[tag['@v']] = 1

                        else:
                            tag_public_transport[tag['@v']] += 1

    return tag_public_transport, tag_public_transport_adress


file = open(r'D:\лабораторные работы по питону\Ортем\labor8\pythonProject\13 - 2.osm', 'r', encoding='utf-8')
text = file.read()
file.close()


dct = xmltodict.parse(text)
dct_public_transport2, add_2 = check_tags('node', dct)
sorted_add1 = dict(sorted(add_2.items()))


print(dct_public_transport2, sorted_add1.keys())
