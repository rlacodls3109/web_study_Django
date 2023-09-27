from django.shortcuts import render, HttpResponse

topics = [
{'id':1, 'title':'routing', 'body':'Routing is ..'},
{'id':2, 'title':'View', 'body':'View is ..'},
{'id':3, 'title':'Model', 'body':'Model is ..'},
]

#클라이언트로 정보를 전송하기 위한 함수
def index(request): 
    global topics # 리스트 사용을 위해 global 변수로 선언해야 함
    ol = ''
    for topic in topics:
        ol += f'<li>{topic["title"]}</li>'
    return HttpResponse(f'''
        <html>
        <body>
            <h1>Django</h1>
            <ol>
                {ol}
            </ol>
            <h2>Welcome</h2>
            Hello,Django
        </body>
        </html>             
                        
    ''')

def create(request): 
    return HttpResponse('create!')

def read(request, id): 
    return HttpResponse('Read! '+ id)
