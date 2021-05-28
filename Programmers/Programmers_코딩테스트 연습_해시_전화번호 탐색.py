def solution(phone_book):
    phone_book.sort()


    for i in range(len(phone_book)-1):
        l = len(phone_book[i])
        sta = phone_book[i]

        if sta == phone_book[i+1][:l]:
            return False


    return True

print(solution(["119", "97674223", "1195524421"]))