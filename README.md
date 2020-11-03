# on_g2o
This package contains files to understand how to use the g2o library.

### TO-DO
- [x] Use `tutorial_slam2d` along with `python-helpers`
- [x] Understand how to make 3D plots using `matplotlib`
- [x] Understand how to use `g2opy`
- [ ] Generate robot path (without landmarks)
	- [x] Ground truth data generation (visualize in matplot)
	- [x] Convert ground truth data into g2o format
	- [ ] Generate sensor readings (visualize in matplot)
	- [ ] Convert sensor data into g2o format
- [ ] Generate robot path (with landmarks)
- [ ] Test the output for known correspondence
- [ ] Integration with ROS

### Repositories referred
1. [g2o][6]
2. [g2opy][5]
3. [GraphSLAM][7]

### Python modules used
1. [Spatial-Math][8]
2. [Numpy][9]
3. [Matplotlib][10]
4. g2o (from g2opy)
5. [getch][11] (for linux) / msvcrt (for windows)

### FAQs

1. What is G2O library for? <br>
A: Provides tools to build a hyper graphs and algorithms to optimize these large large graphs. <br>

2. How do I go about implementing G2O library? <br>
A: The official documentation is very good in itself. You may check out the links given in the end to sharpen the basics required. The examples that come along with this library are a great starting point to understand it. <br>

3. What are odometry measurements? <br>
A: Difference between robot's pose at two consecutive timesteps. In 2D case simulated under `sim_2d.py`, it is represented as (delta x, delta y, theta).

### Useful links to sharpen pre-requisites
1. Solving matrices via linear least squares - [YouTube link][1]
2. Solving via non-linear least squares - [YouTube link][2]
3. Least squares by Cyrill Stachniss - [YouTube link][3]




[1]: https://www.youtube.com/watch?v=Z0wELiinNVQ&list=PLZcI2rZdDGQrb4VjOoMm2-o7Fu_mvij8F&index=69
[2]: https://www.youtube.com/watch?v=RyhOBY5qUQI
[3]: https://www.youtube.com/watch?v=r2cyMQ5NB1o&list=PLgnQpQtFTOGQh_J16IMwDlji18SWQ2PZ6&index=4
[4]: https://
[5]: https://github.com/uoip/g2opy
[6]: https://github.com/RainerKuemmerle/g2o
[7]: https://github.com/francocurotto/GraphSLAM
[8]: https://pypi.org/project/spatialmath-python/
[9]: https://pypi.org/project/numpy/
[10]: https://pypi.org/project/matplotlib/
[11]: https://pypi.org/project/getch/