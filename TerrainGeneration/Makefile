CC = clang
CFLAGS = -Wall -Wextra -std=c99 -lm

TARGET = perlin_noise

$(TARGET): PerlinNoiseAlgorithm.c
	$(CC) $(CFLAGS) -o $(TARGET) PerlinNoiseAlgorithm.c

.PHONY: clean

clean:
	rm -f $(TARGET)
