#データベースからスクレイピングを行って、URLを取ってきました


import requests
import bs4

url ='http://1641.tcd.ie/browse.php'
res = requests.get(url)
#print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')
#type(soup)
trs=soup.select('tr[valign="top"]')
#type(trs)
#trs[0]
#type(trs[0])
#trs[1].td.a.attrs['href']
county_url_list = []
for tr in trs:
	if tr.find('th') == None:
		tds=tr.select('td')
		a_tag=tds[0].a
		url=a_tag.attrs['href']
		county= tds[1].getText()
		county_url_list.append('http://1641.tcd.ie/'+url)

#————————————————————————————————

url_pages = 'http://1641.tcd.ie/searchResults.php?msID=809'
res = request.get(url_pages)

span_tags = soup.select('span[class="pagingTop"]')
dublin_1_urls=[]
for a_tag in a_tags:
	href = a_tag.attrs['href']
	dublin_1_urls.append('http://1641.tcd.ie/'+href)