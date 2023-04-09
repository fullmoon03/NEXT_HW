from django.db import models
from django.utils import timezone
# import datetime
# 말고 timzezone을 써야 하는 이유 : datetime 사용시 offset-naive offset-aware 충돌하는 문제 발생


class List(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    end_date = models.DateTimeField()

    def deadline(self):
        end_date = timezone.localtime(self.end_date) # Aware (UTC) → Aware (TIME_ZONE)
        today = timezone.localtime(timezone.now()) # Aware (UTC) → Aware (TIME_ZONE)
        # 장고는 timezone 설정하고 use_tz = true라고 했을 때 
        # aware 객체(utc를 기본으로 사용하면서 timezone 변수 값 가지는)를 사용하고, 
        # 템플릿에 렌더링할 때만 current timezone으로 보여줌.
        # 그래서 그 중간에 값을 읽어오고 싶을 땐 timezone(한국) 시간대로 바꿔줘야!

        d_day = (end_date.date() - today.date()).days
        print(end_date.date(), today.date(), d_day)
        return d_day


    
    def __str__(self):
        return self.title