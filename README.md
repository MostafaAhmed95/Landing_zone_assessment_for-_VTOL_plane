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

**Create the data set using labelme**<br/>

Follow this [link](https://jsk-docs.readthedocs.io/projects/jsk_recognition/en/latest/deep_learning_with_image_dataset/annotate_images_with_labelme.html)<br/>
Now you put your images and the json files generated in one folder and call it for example data_annotated<br/>

**the following steps is to convert to VOC format dataset<br/>**

Make sure you have the labelme2voc.py file in your current directory<br/>
then run the following command
```bash
./labelme2voc.py data_annotated data_dataset_voc --labels labels.txt
```