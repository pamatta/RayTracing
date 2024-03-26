# RayTracing
simple ray tracing for NLOS - No need for Blender tools or Libraries 

Overview

This code implements a basic ray tracer that can render spheres with reflections and basic lighting. Key features include:

3D Vector Class (Vec3): Provides basic vector operations for 3D calculations.
Ray Class: Defines rays with an origin and direction.
Material Class: Defines surface properties of objects (color, reflectivity).
Sphere Class: Represents spherical objects in the scene.
Light Class: Represents simple point light sources.
Intersection Calculations: Determines if and where a ray intersects a sphere.
Ray Tracing Algorithm: Implements a recursive ray tracing algorithm to calculate color and reflections.
Core Functions

intersect_corrected(ray, sphere): Improved intersection test between a ray and a sphere.
find_closest_intersection_corrected(ray, objects): Finds the closest sphere intersected by a ray.
trace_ray_fixed(ray, objects, lights, depth): Traces a ray's path through the scene, calculating lighting and reflections.
Scene Setup

The code includes adjustable parameters to modify the scene:

camera_position_adjusted: Sets the camera's position.
objects_adjusted: Defines a list of spheres in the scene.
lights_adjusted: Defines light sources within the scene.
Rendering

The code performs the following to generate a 50x50 image:

Calculates the direction of a ray for each pixel.
Uses trace_ray_fixed to compute color values based on ray intersections, lighting, and reflections.
Displays the rendered image using matplotlib.pyplot.
Dependencies

NumPy
Matplotlib
How to Run

Make sure you have NumPy and Matplotlib installed (pip install numpy matplotlib).
Save the provided Python code as ray_tracer.py.
Execute the script from your terminal: python ray_tracer.py
Example Output
The code will generate a simple image of two spheres with reflections and basic lighting.

If you have questions or suggestions about this code, feel free to reach out to:
Pascal Matta: kolmo.io.now@gmail.com
