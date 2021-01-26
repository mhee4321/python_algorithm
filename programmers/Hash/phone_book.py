def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1): # i < phone_book.len
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break
    return answer

a = ["119", "97674223", "1195524421"]
print(solution(a))