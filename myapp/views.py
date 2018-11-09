from django.shortcuts import render
import urllib.request
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
	return render(request, 'search/home.html')

def index(request):
	if request.method == 'GET':
		client_id = ""
		client_secret = ""
		search_word = request.GET.get('value')
		encText = urllib.parse.quote(search_word.encode('utf-8'))
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

