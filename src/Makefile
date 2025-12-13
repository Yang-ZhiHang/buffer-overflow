.PHONY: clean

SRCS := $(wildcard *.c)
PROGS := $(SRCS:.c=)

all: $(PROGS)

%: %.c
	gcc -o $@ -z execstack -fno-stack-protector $<
	gcc -z execstack -fno-stack-protector -g -o $@_gdb $<
	sudo chown root $@
	sudo chmod 4755 $@

clean:
	rm -f stack stack_gdb test test_gdb