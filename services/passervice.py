from hashlib import md5, sha256, sha3_512
from passlib.hash import pbkdf2_sha256

slat = "netology"
pas = "12345" + slat


# hash_md5 = md5(pas.encode()).hexdigest()
hash_sha256 = sha256(pas.encode()).hexdigest()
# hash_sha3512 = sha3_512(pas.encode()).hexdigest()

hash_pbk = pbkdf2_sha256.hash(pas)

my_hash = "$pbkdf2-sha256$29000$hjBGCAFAyLm3tnbuXev9nw$pYNl1BYWe0ZhDH1W.BRd/DGVLmb0aDdo2M0.KQ0laO1"
my_hash2 = "$pbkdf2-sha256$29000$eI8x5jxnTCkFwBjDuBfinA$hTpqWQzKIQVAqmJZVQsj6Pygcr3qOJ3dt6tXLyUjIKA"
# print(hash_md5)
print(hash_sha256)
print(hash_pbk)
print(pbkdf2_sha256.verify(pas, my_hash2))

# print(hash_sha3512)



# ЗАДАЧА
# есть три пароля: w1, w2, w3. Каждый состоит из 6 символов. 
# Символы - только цифры и латинские буквы в верхнем и нижнем регистрах
# известно что:
# md5(w1.encode()).hexdigest() =  b9e9e5e6bb679e91c43a229e9f21a37f
# md5(w2.encode()).hexdigest() =  20afc891efbd174d0cbb8f02bd49b587
# md5(w3.encode()).hexdigest() =  1a6de0f03d8c7578e4114ebc8c0f9fec
# а также что если:
# check = word1 + " " + word2 + " " + word3
# то md5(check.encode()).hexdigest() = 265ca39ad0ce090e790fc57e383ade73
# найдите w1, w2, w3.



