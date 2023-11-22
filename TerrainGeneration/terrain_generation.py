from manim import *
from noise import snoise2

class TerrainGenerationAlgorithmVisualization(Scene):
    #  Set up parameters
    width = 1920
    height = 1080
    scale = 0.1  # Adjust the self.scale to control the granularity of the noise

    def getDetails(self, filename):
        # Initialize an empty list to store rows
        rows = []

        # Open the file for reading
        with open(filename, 'r') as file:
            # Read each line from the file
            for line in file:
                # Split the line into individual values and convert them to float
                row = [float(value) for value in line.split()]

                # Add the row to the list of rows
                rows.append(row)

        return rows
    
    def generateNoise(self):
        # Generate Perlin noise array
        gradient_array = np.zeros((self.width, self.height, 3))
        for i in range(self.width):
            for j in range(self.height):
                value = snoise2(i * self.scale, j * self.scale)
                color_value = int((value + 1) * 127.5)
                gradient_array[i, j] = [color_value, color_value, color_value]

        return gradient_array

    def generateRandomNoise(self):
        return np.random.randint(0, 256, size=(self.width, self.height, 3), dtype=np.uint8)


    def construct(self):
        # arr = self.getDetails("out.txt")

        # Create 10 frames
        for frame_number in range(1, 11):
            # Generate a random image for each frame
            gradient_array = self.generateRandomNoise()

            # Convert NumPy array to Manim image
            image = ImageMobject(gradient_array).scale(2)

            # Display the image for the current frame
            self.add(image)
            self.wait(1)  # Wait for 1 second before moving to the next frame
