# Name : Aditi Gupta
# Roll No : 2019292
# Group : B-8

import datetime as dt
import urllib.request as u

def getLatestRates():
    """ Returns: a JSON string that is a response to a latest rates query.
    The Json string will have the attributes: rates, base and date (yyyy-mm-dd)."""
    url = u.urlopen("https://api.exchangeratesapi.io/latest")
    data = url.read()
    return data
# print(getLatestRates())
def make_dict(s):
    i=0
    flag=1
    l=[]
    while(flag!=0):
        l.append(s[s.find('"',i)+1:s.find('"',s.find('"')+1+i)])
        i=s.find('"',s.find('"')+1+i)
        if i>=len(s)-2:
            flag=0
    k=[]
    for i in l:
        if i.isalpha():
            k.append(i)
    k.remove(k[0])
    k.remove(k[len(k)-1])
    k.remove(k[len(k)-1])
    k.remove(k[len(k)-1])
    j=0
    v=[]
    for i in range(0,len(k)):
        v.append(s[s.find(k[i])+5:s.find(',',j)])
        j=s.find(',',j)+1
    print(v)
    v[-1]=v[-1][:-1]
    v=[float(x) for x in v]
    d={}
    for i in range(len(k)):
        d[k[i]]=v[i]
    return d
# print(make_dict('{"rates":{"CAD":1.4682,"HKD":8.7298,"ISK":138.1,"PHP":56.286,"DKK":7.4712,"HUF":328.33,"CZK":25.514,"AUD":1.6151,"RON":4.7547,"SEK":10.6993,"IDR":15640.93,"INR":78.816,"BRL":4.4437,"RUB":71.0786,"HRK":7.46,"JPY":120.43,"THB":33.623,"CHF":1.1013,"SGD":1.5129,"PLN":4.2535,"BGN":1.9558,"TRY":6.3761,"CNY":7.844,"NOK":10.1638,"NZD":1.7326,"ZAR":16.828,"USD":1.1139,"MXN":21.3164,"ILS":3.9272,"GBP":0.86008,"KRW":1300.09,"MYR":4.64},"base":"EUR","date":"2019-11-01"}'))

def changeBase(amount, currency, desiredCurrency, date):
    """ Outputs: a float value f."""
    if(amount<0):
        return 'amount cannot be negative'
    url = u.urlopen("https://api.exchangeratesapi.io/"+date)
    strd = url.read()
    data = strd.decode('utf-8') #changing byte value to string value
    data=data.replace('}',"")
    data=data.replace('}',"")
    if currency=="EUR":
        r1=1
    else:
        x=data.find(str(currency))
        if x==-1:
            return "currency not found"
        r1=float(data[x+5:data.find(',',x)])
        
    if desiredCurrency=="EUR":
        r2=1
    else:
        y=data.find(str(desiredCurrency))
        if y==-1:
            return "currency not found"
        r2=float(data[y+5:data.find(',',y)])
    return (amount/r1)*r2

# print(changeBase(12.80,"DKK", "HUF", "2003-06-08"))


def printAscending(json):
    """ Output: the sorted order of the Rates 
		You don't have to return anything.
	
	Parameter:
	json: a json string to parse
	"""
    data = json.decode('utf-8')
    d=make_dict(data)
    l=sorted(d.values())
    for i in l:
        print('1 EURO =',i,list(d.keys())[list(d.values()).index(i)])

# print(printAscending(getLatestRates()))
def extremeFridays(startDate, endDate, currency):
    """ Output: on which friday was currency the strongest and on which was it the weakest.
        You don't have to return anything.
		
	    Parameters: 
	    stardDate and endDate: strings of the form yyyy-mm-dd
	    currency: a string representing the currency those extremes you have to determine
	"""
    ds=dt.datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
    de=dt.datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
    if(ds>de):
        print('start date bigger than end date')
    url = u.urlopen('https://api.exchangeratesapi.io/history?start_at='+startDate+'&end_at='+endDate)
    strd = url.read()
    d=eval(strd.decode())
    n=list(d['rates'].keys())
    l={}
    j=0
    for i in n:
        date=dt.datetime(int(i[:4]),int(i[5:7]),int(i[8:]))
        if date.weekday()==4:
            if(j==0):
                max=min=i
                j+=1
            l[i]=d['rates'][i][currency]
            if l[i]>d['rates'][max][currency]:
                max=i
            if l[i]<d['rates'][min][currency]:
                min=i
    if(j==0):
        print('no friday in selected range')
    else:
        print(currency,'was strongest on',min,'. 1 Euro was equal to',l[min],currency)
        print(currency,'was weakest on',max,'. 1 Euro was equal to',l[max],currency)

# extremeFridays('2018-05-04', '2018-08-27', 'GBP')


def findMissingDates(startDate, endDate):
    """ Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

		Parameters: stardDate and endDate: strings of the form yyyy-mm-dd	"""
    url = u.urlopen('https://api.exchangeratesapi.io/history?start_at='+startDate+'&end_at='+endDate)
    strd = url.read()
    d=eval(strd.decode())
    n=list(d['rates'].keys())
    ds=dt.datetime(int(startDate[:4]),int(startDate[5:7]),int(startDate[8:]))
    de=dt.datetime(int(endDate[:4]),int(endDate[5:7]),int(endDate[8:]))
    if(ds>de):
        print('start date bigger than end date')
    diff=de-ds
    l=[]
    for i in range(diff.days+1):
        l.append((ds+dt.timedelta(i)).date().strftime('%Y-%m-%d'))
    for i in l:
        if i not in n:
            print(i)
# findMissingDates('2018-10-17','2017-10-30')




