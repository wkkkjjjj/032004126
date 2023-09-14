import requests
import re
import csv
import numpy as np
import pandas as pd

pd.set_option("display.unicode.ambiguous_as_wide",True)
pd.set_option("display.unicode.east_asian_width",True)

def get_response(html_url):
    headers = {
        'Cookie':
'buvid3=1B24090C-625F-5D6A-33F9-C2C8676AD09055616infoc; b_nut=1693815855; i-wanna-go-back=-1; b_ut=7; _uuid=BC1022EE1-58F7-AE1E-F713-A75E7BFCDD4765044infoc; buvid4=355B3E64-7114-321E-7E7A-2D8CB29C6C9367607-023090416-X83v1qigvaXaWzfk4QM9rA%3D%3D; buvid_fp=02d9944d11f8b9f618b05c1e66cf2bac; DedeUserID=700937803; DedeUserID__ckMd5=16e09be0058f1010; CURRENT_FNVAL=4048; rpdid=|(u)luk)YYJR0J\'uYmJ)ulmlk; bp_video_offset_700937803=837129502994726963; PVID=1; b_lsid=177D174F_18A786C2953; bsource=search_baidu; header_theme_version=CLOSE; home_feed_column=4; browser_resolution=767-706; SESSDATA=cfa685d0%2C1709789477%2C18272%2A91CjDYV9L73A3ajSkiT3IQpxqkuHYI1Zj1ir5VVKaAljm-eAp0K6-0_pUdbdDpGDrbSgkSVlE3S1ZIcXBVcS02aUJRTnZVVnhnX28wdUlkcTdpbmlNcFRTbU0wOVlIQnRFRF9NVkhJbUJRSXBhUTc0VExhUXRuNG90WHRaUHRJdmpDQWZPelFWdzN3IIEC; bili_jct=d96a265d33654e041d2db3089c105148; sid=81gkwgjc; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ0OTcyNjMsImlhdCI6MTY5NDIzODA2MywicGx0IjotMX0.9c2Wth23b9e9JInaVi0SRzGclI4RHkTddEbgXK2wFfI; bili_ticket_expires=1694497263',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/video/BV1t94y147Fk/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }
    response = requests.get(url=html_url, headers=headers)
    return response

if '__main__'==__name__:
    response=get_response('https://api.bilibili.com/x/v2/dm/wbi/web/seg.so?type=1&oid=1253529510&pid=362912126&segment_index=1&pull_mode=1&ps=0&pe=120000&web_location=1315873&w_rid=a002816dbd3eb2dccfffc11a68377056&wts=1694241282')
    # print(type(response))
    # print(response.text)
    result = re.findall(".*?([\u4E00-\u9FA5]+).*?",response.text)
    ''''print(result)
    with open('B站弹幕.csv',mode='w',newline='') as file:
        csv_writter=csv.writer(file)
        csv_writter.writerows(result)
    '''
    with open('B站弹幕.csv', mode='w', encoding='utf-8') as f:
        pass
    with open('B站弹幕.csv', mode='a', encoding='utf-8',newline='') as file:
        csv_writter=csv.writer(file)
        for i in result:
                mylist=[i,1]
                csv_writter.writerow(mylist)
    df = pd.read_csv('./B站弹幕.csv',header=None,names=['弹幕','数量'])
    print(df)
    gr=df.groupby(by='弹幕')
    print(gr.agg({'数量':'sum'}))



