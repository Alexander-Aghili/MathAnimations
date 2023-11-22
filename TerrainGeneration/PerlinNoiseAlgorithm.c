#include <math.h>
#include <stdio.h>
#include <stdlib.h>

float interpolate(float a0, float a1, float w) {
    return (a1 - a0) * w + a0;
} 

typedef struct {
    float x,y;
} Vector2;

Vector2 randomGradient(int ix, int iy) {
    const unsigned w = 8 * sizeof(unsigned);
    const unsigned s = w / 2;
    unsigned a = ix, b = iy;
    a *= 3284157443; b ^= a << s | a >> w-s;
    b *= 1911520717; a ^= b << s | b >> w-s;
    a *= 2048419325;
    float random = a * (3.14159265 / ~(~0u >> 1)); // in [0, 2*Pi]
    Vector2 v;
    v.x = cos(random); v.y = sin(random);
    return v;
}

// Computes the dot product of the distance and gradient vectors.
float dotGridGradient(int ix, int iy, float x, float y) {
    // Get gradient from integer coordinates
    Vector2 gradient = randomGradient(ix, iy);

    // Compute the distance vector
    float dx = x - (float)ix;
    float dy = y - (float)iy;

    // Compute the dot-product
    return (dx*gradient.x + dy*gradient.y);
}

// Compute Perlin noise at coordinates x, y
float perlin(float x, float y) {
    // Seed the random number generator with the current time
    srand((unsigned int)time(NULL));


    // Determine grid cell coordinates
    int x0 = (int)floor(x);
    int x1 = x0 + 1;
    int y0 = (int)floor(y);
    int y1 = y0 + 1;

    // Determine interpolation weights
    // Could also use higher order polynomial/s-curve here
    float sx = x - (float)x0;
    float sy = y - (float)y0;

    // Interpolate between grid point gradients
    float n0, n1, ix0, ix1, value;

    n0 = dotGridGradient(x0, y0, x, y);
    n1 = dotGridGradient(x1, y0, x, y);
    ix0 = interpolate(n0, n1, sx);

    n0 = dotGridGradient(x0, y1, x, y);
    n1 = dotGridGradient(x1, y1, x, y);
    ix1 = interpolate(n0, n1, sx);

    value = interpolate(ix0, ix1, sy);
    return value; // Will return in range -1 to 1. To make it in range 0 to 1, multiply by 0.5 and add 0.5
}

int main() {
    // Set the size of the terrain map
    int width = 10;
    int height = 10;

    // Create a 2D array to store the terrain map
    float terrain[width][height];

    // Seed the random number generator with the current time
    srand((unsigned int)time(NULL));

    // Generate Perlin noise for each point in the terrain map
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            // Adjust the parameters as needed based on your requirements
            float frequency = 0.1;  // Controls the "zoom" of the terrain
            float amplitude = 1.0;  // Controls the height of the terrain

            // Generate Perlin noise for the current point
            float perlinValue = perlin(x * frequency, y * frequency) * amplitude;

            // Store the result in the terrain map
            terrain[x][y] = perlinValue;
        }
    }

    // Print the terrain map (optional)
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            printf("%f ", terrain[x][y]);
        }
        printf("\n");
    }

    return 0;
}

