from django.shortcuts import render, HttpResponse

topics = [
{'id':1, 'title':'routing', 'body':'Routing is ..'},
{'id':2, 'title':'View', 'body':'View is ..'},
{'id':3, 'title':'Model', 'body':'Model is ..'},
]

def HTMLTemplete(articletag):
    global topics # 리스트 사용을 위해 global 변수로 선언해야 함
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return(f'''
        <html>
        <body>
            <h1><a href = "/">Django</a></h1>
            <ol>
                {ol}
            </ol>
            {articletag}
        </body>
        </html>             
                        
    ''')

#클라이언트로 정보를 전송하기 위한 함수
def index(request): 
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplete(article))

def create(request): 
    return HttpResponse('create!')

def read(request, id): #read 쪽도 똑같은 HTML 코드를 공유한다.
    article=''

    for topic in topics:
        if topic["id"] == int(id):
            article = f'''
            <h2>{topic["title"]}</h2>
            {topic["body"]}
            '''
    return HttpResponse(HTMLTemplete(article))
