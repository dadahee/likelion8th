from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_cnt = {}
    for word in words:
        if word in word_cnt: word_cnt[word] += 1
        else: word_cnt[word] = 1
    return render(request,'result.html', { "text": text, 'total': len(words), 
    'word_cnt': sorted(word_cnt.items(), key=lambda x: x[1], reverse=True) })

    # form 태그에서 action을 통해 request가 들어오는데
    # 그 form 안에 있던 name이 fulltext라는 tag의 정보가
    # get 메소드를 통해 넘어온다

    # 데이터를 넘길 때에는 세번째 파라미터, dictionary 형으로 보내야 함!
    # dictionary : { 'key': value }
    # value는 우리가 보낼 변수, key는 html 상에서 받는 템플릿 변수
    # result.html의 템플릿 변수 == 딕셔너리 key값 이어야 한다.

    # 템플릿 언어에서는 dic.items()를 쓰면 오류가 나기 때문에 views.py에서 items() 메소드를 사용하여 
    # 인자로 넘겨 주어야 정상적으로 key, value를 읽을 수 있다.