#include<iostream>
#include<glad/glad.h>
#include<GLFW/glfw3.h>

int main() 
{
	glfwInit();

	// Tell glfw opengl version
	// OPENGL 3.3
	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	// Tell glfw we are using the CORE profile
	// So we have the modern functions
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

	// Create GLFWwindow object params width, height, window name, fullscreen, not important
	GLFWwindow* window = glfwCreateWindow(1000, 800, "test window", NULL, NULL);
	if (window == NULL) 
	{
		std::cout << "Failed to create GLFW window" << std::endl;
		glfwTerminate();
		return -1;
	}
	// Introduce window to current context
	glfwMakeContextCurrent(window);

	// Load glad to configure OpenGL
	gladLoadGL();

	// Specify viewport of OpenGL in the Window
	// viewport goes from x,y 0 to x,y 800
	glViewport(0, 0, 800, 800);

	// Specify color of background
	glClearColor(0.7f, 0.3f, 0.17f, 1.0f);
	// Clean back buffer and assign new color
	glClear(GL_COLOR_BUFFER_BIT);
	// Swap the back buffer with the fron buffer
	glfwSwapBuffers(window);

	// Main while loop
	while (!glfwWindowShouldClose(window)) 
	{
		// Take care of all GLFW events
		glfwPollEvents();
	}
	// Delete window before closing the program
	glfwDestroyWindow(window);
	glfwTerminate();
	return 0;
}