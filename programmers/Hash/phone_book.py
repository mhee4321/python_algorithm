def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    # [('119', '1195524421'), ('1195524421', '97674223')]
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

a = ["119", "97674223", "1195524421"]
print(solution(a))