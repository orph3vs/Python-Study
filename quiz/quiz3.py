# 사이트별로 비밀번호를 만들어 주는 프로그램 작성
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성  
# ex) nav51!

site = "http://google.com"
# 1 http:// 삭제
pwd = site[7:]
#pwd = site.replace("http://", "")
# 2 
pwd = pwd[:pwd.find('.')]
#pwd = pwd[:pwd.index('.')]
# 3 
pwd = pwd[:3] + str(len(pwd)) + str(pwd.count('e')) + '!'
print("{0}의 비밀번호는 {1}입니다.".format(site, pwd))