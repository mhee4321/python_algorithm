import re

def solution(new_id):
    # 1. 소문자 치환
    new_id = new_id.lower()
    # 2. 알파벳 소문자, 숫자, -, _, . 빼고 제거
    new_id = re.sub(r"[^a-z0-9\-\_\.]","",new_id)
    # 3. . 두 개 이상이면 하나로 치환
    new_id = re.sub(r"[\.]+", ".", new_id)
    # 4. 마침표가 처음이나 끝에 있으면 제거
    if new_id.startswith("."): new_id = new_id[1:]
    if new_id.endswith("."): new_id = new_id[:-1]
    # 5. 빈 문자열이면 a 대입
    if new_id == "": new_id = "a"
    # 6. 16자 이상이면, 앞 15글자 제외한 나머지 제거, 제거 후 맨 뒷문자가 .이면 .제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith("."):
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

a = str(input())
solution(a)