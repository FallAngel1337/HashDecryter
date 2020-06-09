# Educational Purpose Only

# HashDecryter
 A simple hash decryption tool

# How to use?

USE: `python3 HashDecrypter.py <your_custom_wordlist.txt>`

# How does it works?

Everybody knows that a hash can't be "reversed", but we can get the original value of them. But HOW??

Simple: We can make guesses and compare the results with the hash you input.

Ex: Take the MD5 hash: 21232f297a57a5a743894a0e4a801fc3, how we can discover your value?
    Get a wordlist, making a hash of all the words and finnaly compare with the hash you want discover the value

    flower = 608f0b988db4a96066af7dd8870de96c is different than 21232f297a57a5a743894a0e4a801fc3
    house = 2ca63cddd54f9490efad22421891a9d1  is different than 21232f297a57a5a743894a0e4a801fc3
    admin = 21232f297a57a5a743894a0e4a801fc3  is equals than 21232f297a57a5a743894a0e4a801fc3

# Links to Study

 - https://en.wikipedia.org/wiki/Hash_function
 - https://techterms.com/definition/hash
 - https://en.wikipedia.org/wiki/MD5
