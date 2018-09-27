from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone


def post_list(request):
    # 현재 지역에 맞는 시간&날짜 객체 할당
    current_time = timezone.now()

    return HttpResponse('<h1>Post List</h1><br><p>{}</p>'.format(
        # 날짜 & 시간 객체가 가진 정볼들 문자열로 변환
        # 프로젝트 설정을 바꾸어주지 않으면 국제 표준시를 기반으로 리턴해준다.
        # settings.py 에 TIME_ZONE 을 바꾸어준다.
        # 서버에선 UTC로 저장하는 것이 좋고
        # 클라이언트 단에서 TIMEZONE을 바꾸어주는 것이 좋다.
        current_time.strftime('%Y. %m. %d<br>%H:%M:%S')
        )
    )
    # return HttpResponse('<h1>Post List</h1>')
