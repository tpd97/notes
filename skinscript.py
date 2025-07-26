'''
clear all orients by making identity before orient constraining (put in world space, then use aim cosntraint)
use locator as up and move in target joints up plane and only in that translate vector (use group as offset, then locator is 0)
move from end to start of chain. aim elbow aat wrist, shoulder at elbow
find centers using clusters then match a joint to the cluster then delete cluster
make live, use quad draw to create low poly, skin low poly, project low poly weights to mesh using copy skin weights (closest point, closest joint, one to one, one to one)
spine: make pelvis to center of chest. chest is one bone, but can put one more bone inside of the chest jointfor extra. 
fpr chest, take spine end, run joint and joint again, then move another joint off to be the neck joint 
for advanced spline spine, create straight spine skinned to advanced spline curve

.1 air density, increase wind noise, SET UNITS TO CM NOT METERS

joints in the skeletons hierarchy, but parented to locator (point on poly cosntrained) to mesh
flatten (fl) lets you sleect components. for loop for each face, create clusters at each face, select clusters, match joints. joints have their own hierarchy

'''
######################################

cmds. import 
