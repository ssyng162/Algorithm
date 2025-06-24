### 백준 4659: 비밀번호 발음하기

vowel = ['a', 'e', 'i', 'o', 'u']


def no_vowel(password):
    return not any(v in password for v in vowel)


def have_continuous_3_same_type(password):
    if len(password) < 3:
        return False
    
    count = 1
    prev_is_vowel = password[0] in vowel

    for i in range(1, len(password)):
        current_is_vowel = password[i] in vowel
        if current_is_vowel == prev_is_vowel:
            count += 1
        else:
            count = 1
            prev_is_vowel = current_is_vowel
        if count >= 3:
            return True
    return False



def have_continuous_2_same_char(password):
    if len(password) < 2:
        return False
    
    prev = ''
    
    for p in password:
        if p==prev:
            if p in ('e', 'o'): continue
            return True
        prev = p
    return False


while(True):
    password = input()
    
    if password == "end": break
    
    if no_vowel(password) or have_continuous_3_same_type(password) or have_continuous_2_same_char(password):
        print(f"<{password}> is not acceptable.")
    else:
        print(f"<{password}> is acceptable.")
        