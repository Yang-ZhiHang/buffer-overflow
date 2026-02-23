## 操作指北

操作环境： Ubuntu 22.04 x86_64

1. 环境设置，关闭虚拟地址随机化

    ```bash
    sudo sysctl -w kernel.randomize_va_space=0
    ```

2. 使用 stack_gdb 进行调试，获取必要信息

    - rbp/ebp 到 buffer 起始地址的偏移量: 112
    - shellcode 的存放地址: &str

3. 生成 badfile，运行 stack，执行 id whoami