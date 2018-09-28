from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import os


def post_list(request):

    # templates/blog/post_list.html 파일의 내용을 일거온 후,
    # 해당 내용을 아래에 리턴해주는 HttpResponse인스턴스 생성 시 인수로 넣어준다.
    #   os.path.abspath(__file__)           <- 코드가 실행중인 파일의 경로를 나타냄
    #   os.path.dirname(<경로>)              <- 특정 경로의 상위폴더를 나타냄
    #   os.path.join(<경로>, <폴더/파일명>)    <- 특정 경로에서 하위폴더 또는 하위 파일을 나타냄

    current_path = os.path.abspath(__file__)
    parent_app_blog_dir = os.path.dirname(current_path)
    parent_dir = os.path.dirname(parent_app_blog_dir)
    post_list_html = os.path.join(parent_dir, 'templates', 'blog', 'post_list.html')

    content = open(post_list_html, 'rb').read()

    return HttpResponse(content)

    # 현재 지역에 맞는 시간&날짜 객체 할당
    # current_time = timezone.now()
    #
    # return HttpResponse('<h1>Post List</h1><br><p>{}</p>'.format(
    #     # 날짜 & 시간 객체가 가진 정볼들 문자열로 변환
    #     # 프로젝트 설정을 바꾸어주지 않으면 국제 표준시를 기반으로 리턴해준다.
    #     # settings.py 에 TIME_ZONE 을 바꾸어준다.
    #     # 서버에선 UTC로 저장하는 것이 좋고
    #     # 클라이언트 단에서 TIMEZONE을 바꾸어주는 것이 좋다.
    #     current_time.strftime('%Y. %m. %d<br>%H:%M:%S')
    #     )
    # )
    # return HttpResponse('<h1>Post List</h1>')
