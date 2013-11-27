import bitly_api

def bitly(longurl):
    ak = 'R_1048f29b16dae5ad8e09b74f3df83025'
    at = '8e6aa34d9566b8aa87fbfbfd94a1240f4f1c954a'

    c = bitly_api.Connection('justinta', ak)
    c = bitly_api.Connection(access_token = at)
    shorturl = c.shorten('http://%s' % longurl)

    return shorturl['url']


if __name__ == '__main__':
    longurl = raw_input('enter url to be shortened: ')
    print bitly(longurl)

