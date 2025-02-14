from django.contrib import admin
from django.urls import path, include
from blog.views import home  # blog 앱의 home 뷰 가져오기
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # 🔹 루트 URL에서 blog 홈화면 띄우기 (수정됨)
    path('blog/', include('blog.urls')),  # 회원 관리 URL 포함
    path('', include('blog.urls')),  # 홈 URL이 blog 앱으로 연결되도록 설정할 수 있습니다.
]
