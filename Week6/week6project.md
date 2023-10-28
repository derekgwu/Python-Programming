# Week 6 Project: Encryption and Decryption

## Introduction
A popular field in computer science is the the study of cybersecurity. This study of hacking culture, passwords, and combinations, is growing in computer science. This week, we are going to dip our feets into the world of cybersecurity, more specifically study how passwords work.

## Developing Our Own Secret Messages
When you text your friends, in order to prevent unwanted people seeing your message, Apple will encrypt your message and decrypt your message to the receiver. This week we will be creating our own encryption and decryption service. 

## Encryption and Decryption Process
Our encryption process will take advantage of a character ASCII values. Recall that each character has its own number like:
```
a   b   c   d   e
97 98  99 100 101
```

Our encryption process will work like this:

1. Take the message we want to encrypt - for example `Hello World`
2. Move the first character to the end: `ello Worldh`
3. Shift each character 3 values. For example - shifting `a` would make it `d`

Note in order to decrypt, you will have to perform your encryption process backwards. 

## Writing Code
For this assignment you'll see two blocks of code:
```
def encrypt(msg):
    "ENCRYPTION PROCESS HERE"

def decrypt(msg):
    "DECRYPTION PROCESS HERE"
```
Please write your code within these `def` blocks. My units test will call them to test them. 