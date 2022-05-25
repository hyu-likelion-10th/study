# 설문조사 프로젝트 확장 구현- 문항이 여러 개인 Survey 페이지 #
> 1. survey app 과 accounts app을 생성 (앱 이름은 자유)
> 2. 유저를 생성 (createsuperuser 이용)

## <accounts app> ##
1. views.py -  로그인, 로그아웃 기능 구현
2. templates -  login.html (로그인하는 화면)
## <survey app> ##
1. models.py - 기존의 survey모델과 answer모델

2. views.py
- main : 설문조사를 목록 형식으로 보여줌 (여러개 표시)
- save : 각 설문조사에 대해 응답하고 완료창으로 이동
- result :  각 설문조사에 대해 응답결과 보여줌
- new : 새로운 설문조사 작성 화면 보여줌
- create : 새로운 설문조사 만들기(POST), main으로 돌아감

3. templates
- main.html : 로그인이 되었으면 설문조사 목록 반환 + 로그아웃 버튼 / 로그인 되지 않았으면 로그인 링크 보여줌
- complete.html : 설문조사 응답 완료 화면
- result.html : 설문조사 응답 결과 화면
- new.html : 새로운 설문 문항 작성 화면

------------

# restful api 요약 #
> restful api에 대해 공부하고, 공부한 내용을 정리하여 readme 파일로 git에 업로드

------------

# 다음 주 세션까지 들어와야 할 강의 #

1. 코드라이언 강의: Chapter6 ~ 7
2. 아래 링크 강의: 준비운동 ~ rest와 serializer
 + https://class.likelion.org/lectures/django%20%EC%8B%AC%ED%99%94/160
 + id: bluekmky@likelion.org
 + pw: 96393439
