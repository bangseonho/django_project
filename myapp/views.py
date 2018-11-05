from django.shortcuts import render
import urllib.request
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
	if request.method == 'GET':
		client_id = "9dzy3DDrzUBJE7yPrRss"
		client_secret = "XlQtL4lsv8"
		#search_lang = input("검색할 단어를 입력하세요. : ")
		encText = urllib.parse.quote("어벤져스")
		url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
		# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
		movie_request = urllib.request.Request(url)
		movie_request.add_header("X-Naver-Client-Id",client_id)
		movie_request.add_header("X-Naver-Client-Secret",client_secret)
		response = urllib.request.urlopen(movie_request)
		rescode = response.getcode()
		if(rescode==200):
		    response_body = response.read()
		    results = json.loads(response_body.decode('utf-8'))
		    items = results.get("items")
		    context = {
		    	"items" : items
		    }
		    return render(request, 'search/search.html', context)
		else:
		    print("Error Code:" + rescode)