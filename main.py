import motion

#main
r = 1 #circle radius
x_c = abs(1 + r) #circle center x
y_c = - abs(1 + r) #circle center y
time = 2 #modeling time
dt = 0.1 #delta time
w = 2 #w for cos
n = 100 #number of body points
body = motion.body_init(x_c, y_c, r, w, n) #body initialisation
motion.trajectory(time, dt, body, w, n) #trajectory modeling
motion.velocity_fields(time, dt, 2, w)

