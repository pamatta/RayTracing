import math
import numpy as np
import matplotlib.pyplot as plt

class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, s):
        return Vec3(self.x * s, self.y * s, self.z * s)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def normalize(self):
        length = self.length()
        return self * (1.0 / length)

    def length(self):
        return math.sqrt(self.dot(self))

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

class Material:
    def __init__(self, color, reflectivity):
        self.color = color
        self.reflectivity = reflectivity

class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

class Light:
    def __init__(self, position, color):
        self.position = position
        self.color = color

def intersect_corrected(ray, sphere):
    oc = ray.origin - sphere.center
    a = ray.direction.dot(ray.direction)
    b = 2.0 * oc.dot(ray.direction)
    c = oc.dot(oc) - sphere.radius * sphere.radius
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return False, None
    else:
        t = (-b - math.sqrt(discriminant)) / (2.0 * a)
        return True, t

def find_closest_intersection_corrected(ray, objects):
    found_intersection = False
    closest_t = np.inf
    closest_sphere = None
    for sphere in objects:
        intersects, t = intersect_corrected(ray, sphere)
        if intersects and t < closest_t:
            closest_sphere = sphere
            closest_t = t
            found_intersection = True
    return found_intersection, closest_sphere, closest_t

def trace_ray_fixed(ray, objects, lights, depth):
    if depth <= 0:
        return Vec3(0, 0, 0)
    found_intersection, closest_sphere, closest_t = find_closest_intersection_corrected(ray, objects)
    if not found_intersection:
        return Vec3(0, 0, 0)
    hit_point = ray.origin + ray.direction * closest_t
    normal = (hit_point - closest_sphere.center).normalize()
    color = Vec3(0, 0, 0)
    for light in lights:
        light_dir = (light.position - hit_point).normalize()
        diffuse_factor = max(0.0, light_dir.dot(normal))
        color += Vec3(closest_sphere.material.color.x * light.color.x * diffuse_factor,
                      closest_sphere.material.color.y * light.color.y * diffuse_factor,
                      closest_sphere.material.color.z * light.color.z * diffuse_factor)
    reflected_dir = ray.direction - normal * 2 * ray.direction.dot(normal)
    reflected_ray = Ray(hit_point + normal * 0.001, reflected_dir.normalize())
    color += trace_ray_fixed(reflected_ray, objects, lights, depth - 1) * closest_sphere.material.reflectivity
    return color

# Adjusted scene parameters for visualization
camera_position_adjusted = Vec3(0, 0, -2)
objects_adjusted = [
    Sphere(Vec3(0, 0, 3), 1, Material(Vec3(1, 0, 0), 0.2)),
    Sphere(Vec3(2, 0, 4), 1, Material(Vec3(0, 1, 0), 0.5))
]
lights_adjusted = [
    Light(Vec3(0, 2, 0), Vec3(1, 1, 1))
]

# Rendering process
image_data_fixed = np.zeros((50, 50, 3), dtype=np.uint8)

for j in range(50): 
	for i in range(50):
		x = (2 * (i + 0.5) / 50 - 1) * math.tan(math.pi / 6) * 2
		y = (1 - 2 * (j + 0.5) / 50) * math.tan(math.pi / 6) * 2
		ray_dir = Vec3(x, y, 1).normalize()
		ray = Ray(camera_position_adjusted, ray_dir)
		color = trace_ray_fixed(ray, objects_adjusted, lights_adjusted, 3)  # Assuming max depth of 3 for simplicity
image_data_fixed[j, i, 0] = int(max(0, min(color.x * 255, 255)))
image_data_fixed[j, i, 1] = int(max(0, min(color.y * 255, 255)))
image_data_fixed[j, i, 2] = int(max(0, min(color.z * 255, 255)))
plt.figure(figsize=(10, 10))
plt.imshow(image_data_fixed)
plt.axis('off') # Turning off the axis for a cleaner look
plt.show()
