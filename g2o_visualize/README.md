# Understanding the implementation

Imagine you have a 3-wheeled differential drive robot with symmetric geometry, and a castor wheel in the front. <br>
Sensors used:
1. Encoder(s) on the rear wheel(s)
2. IMU (gyroscope and/or magnetometer) with axis aligned with the geometric center
3. Vision sensor (will be elborated in **Landmarked land** section)

## What is the goal?
To implement a full-SLAM system for the robot. In other words, a system that enables the robot to keep a track of the path it travelled (goal[0]), and map the environment around (goal[1]) it while it is travelling through it.

## No landmark land

> The subsequent discussion is in the context of `sim_2d_noLM.py`.
### Environment
Imagine that your robot is in an infinite open environment with nothing around it.

### Assumptions
1. Encoder gives the displacement between two of it's readings
2. IMU gives the heading angle wrt initial heading *(assumed to be zero)*
3. Sensors are non-ideal and the noise is modeled as random Gaussian variable with mean zero
4. There is an inbuilt system in the robot that randomly generates control signals that drive the robot around
5. There exists no control loop that makes sure a given set-point is achieved
6. Heading of the robot and the local `x-axis` coincide
7. Robot's local `z-axis` and the global `z-axis` coincide

Since there are no landmarks in the environment, we are not bothered about the vision sensor. <br>

### How is the sensor data is processed?
The g2o framework takes the odometry data along with its uncertainity. The odometry data from encoders can be directly fed into g2o because encoders are incremental sensors and g2o takes incremental values to form edges between 2 poses. But non-incremental sensors like the IMU must be used like an incremental sensor by reading only the difference between the previous and current angle.

> *Sidenote: In practical implemetation of g2o framework, we generate a `.g2o` consisting of only edges between poses. The algorithm determines the poses from the edges.*

Given the assumptions, the `delta y` value can be considered to be zero forever. This is because our robot can only perform yaw and translation in `x` direction. Hence, the difference in the poses of the robot will be due `delta x` and `delta theta` only.

### How to achieve the goal[0]?
To understand the implementation of goal[0], the robot is going to move around:
### Algorithm
1. Assume the robot at origin. *(all the future poses will be estimated wrt the coordinate frame attached to origin)*
2. At every `k`th instant, the odometry is read. This odometry corresponds to `delta x` (wrt local frame (x is heading)) and `delta theta`. These values are fed into a `.g2o` file for optimization.
3. After every sample, the graph is optimized. The optimized graph gives me `x, y, theta` wrt to global frame.

The output of this algorithm is an `matplotlib.pyplot` showcasing the estimated path against the ground truth.

## Land with landmarks
### Environment
Imagine that your robot is in an environment with multiple landmarks.

### Assumptions
1. The vision sensor correctly IDs the unique signature of a landmark.
2. The coordinates of the landmark are perfectly determinable.
3. The correspondance of the landmarks is not known, i.e., if a landmark A is observed from pose i, and pose j, then both of these observations will form 2 landmarks instead of a single landmark. The attempt here is to extract a single landmark from multiple readings.

### How to achieve the goal[1]?
To understand the implementation of goal[1], the robot is going to move around:
### Algorithm
1. Assume the robot at origin. The position of the landmarks as seen from origin are noted.
2. At every `k`th instant, location of the landmarks are noted. These values are fed into a `.g2o` file for optimization.
3. Execute the algorithm proposed in paper : `GraphSLAM Algorith implementation for solving simultaneous localization and mapping` by *Franco Andreas Curotto Molina* for unknown correspondance case.