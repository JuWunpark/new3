from django.conf import settings
from django.contrib.auth import logout
from django.utils.timezone import now
from datetime import datetime, timezone
import time

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')

            if last_activity:
                # timestamp를 offset-aware datetime으로 변환
                last_activity_time = datetime.fromtimestamp(last_activity, tz=timezone.utc)
                idle_time = (now() - last_activity_time).total_seconds()

                # 설정된 시간 이상 비활성화 시 로그아웃
                if idle_time > settings.SESSION_COOKIE_AGE:
                    logout(request)
                    request.session.flush()

            # 현재 시간을 timestamp()로 변환해서 세션에 저장
            request.session['last_activity'] = time.time()

        response = self.get_response(request)
        return response
