# 토큰을 관리해주는 파일

BLOCKLIST = set()

def add_to_blocklist(jti): # 추가
    BLOCKLIST.add(jti)

def remove_from_blocklist(jti): # 삭제
    BLOCKLIST.discard(jti)