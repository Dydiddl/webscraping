import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 값 출력

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class = "Nbtn_upload" 인 a element 를 찾아줘
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("div", attrs={"class":"ComponentHead__component_head--O2tPr"})
print(rank1.div)

# <div class="ComponentHead__component_head--O2tPr"><div class="ComponentHead__title_area--IEQEG"><h2 class="ComponentHead__title--TjYVo"><span class="ComponentHead__text--dhKW7">요일별 전체 웹툰</span></h2><span class="ComponentHead__count--bRLNZ"></span><div role="tablist" class="ComponentHead__tab_control--R1TyL"><button type="button" role="tab" class="ComponentHead__button_tab--YoR6Z" aria-selected="true">인기순</button><button type="button" role="tab" class="ComponentHead__button_tab--YoR6Z" aria-selected="false">업데이트순</button><button type="button" role="tab" class="ComponentHead__button_tab--YoR6Z" aria-selected="false">조회순</button><button type="button" role="tab" class="ComponentHead__button_tab--YoR6Z" aria-selected="false">별점순</button></div></div></div>