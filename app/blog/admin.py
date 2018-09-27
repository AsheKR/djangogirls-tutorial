from django.contrib import admin

# Pycharm에서는 root가 djangogirls-tutorial 이라고 생각한다.
# 하지만 runsever에서는 app이 루트라고 생각하기 때문에 오류가 발생한다.
# Root Directory 설정을 위해 원하는 루트 폴더를 우클릭 Mark Directory as -> Source Root 하면 된다.
# from app.blog.models import Post

# 자동 IMPORT, 절대경로로 입력되는것은 추천되지 않는다.
# ALT + ENTER
#from blog.models import Post

from .models import Post

admin.site.register(Post)
