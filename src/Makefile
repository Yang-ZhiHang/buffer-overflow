.PHONY: clean

SRCS := $(wildcard *.c)
PROGS := $(SRCS:.c=)
OUTPUT_DIR := output

all: $(PROGS)

%: %.c
	mkdir -p $(OUTPUT_DIR)
	gcc -o $(OUTPUT_DIR)/$@ -z execstack -fno-stack-protector $<
	gcc -z execstack -fno-stack-protector -g -o $(OUTPUT_DIR)/$@_gdb $<
	sudo chown root $(OUTPUT_DIR)/$@
	sudo chmod 4755 $(OUTPUT_DIR)/$@
clean:
	rm -f $(OUTPUT_DIR)/stack*