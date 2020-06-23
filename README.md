# Landing_zone_assessment_for-_VTOL_plane
**steps to collect the data set**<br/>

Clone the repo and move Nodes folder to the src folder inside your catkin workspace<br/>
Then do the following steps
```bash
roscd 
cd ..
catkin build OR catking_make  
```
Make sure we already run the [simulation](https://github.com/frontw/inno_sim_interface-)<br/>
Make any mission from the QGC<br/>
Then run the node in a new terminal with these commands
```bash
roscd Nodes
rosrun Nodes sub_img.py
```
You will find your dataset created inside a data_set folder inside Nodes package 