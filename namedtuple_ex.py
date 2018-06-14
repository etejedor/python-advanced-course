from collections import namedtuple

# Generation of classes at runtime
vec3 = namedtuple('Vec3', 'x,y,z')
type(vec3)
v = Vec3(1,2,3)
Vec3(x=1,y=2,z=3)

# Like c structs, but immutable
v.x
v[0]
