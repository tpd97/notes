'''
import maya.cmds as cmds

def jnt2comp():
    cl = cmds.cluster()[1] #0 selects the deformer, handle is the 2nd 
    cmds.select(cl = True)
    jnt = cmds.joint(rad = 10)
    
    cmds.matchTransform(jnt, cl, pos = True, rot = True)
    
    
    cmds.delete(cl)
import maya.cmds as cmds

#cmds.xform(piv = [0,0,0], ws = True)
cmds.delete(cn = True)
cmds.makeIdentity(apply = True, t= 1, r = 1, s = 1, pn = True, jo = True)
jnt2comp()
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
import maya.cmds as cmds
rad = 20
numJnts = 5
jnts = cmds.ls(sl = True, type = "joint")
for jnt in jnts:
    rad = cmds.getAttr(f"{jnt}.radius")
    endJnt =  cmds.listRelatives(jnt, c = True)[0]
    cmds.select(jnt, r = True)
    segRootJnt = cmds.joint(rad = rad+5)
    segEndJnt = cmds.joint(rad = rad+5)
    cmds.matchTransform(segEndJnt, endJnt, pos = True)
    jntLen = cmds.getAttr(f"{endJnt}.tx")

    
    
    cmds.select(jnt, r = True)
    for i in range(1, numJnts):
        segJnt = cmds.joint(radius = rad)
        cmds.move((jntLen/numJnts),0,0, ls = True)
    newSegEndJnt = cmds.ls(sl = True, type = "joint")
    cmds.parent(segEndJnt, newSegEndJnt)


poly select convert (1 faces, 2 edges, 3 verts)

'''
clnCmps = []
for fc in fcs:
  clnFc = fc.replace("body", "body1")
  clnCmps.append(clnFc)
'''

    
'''
######################################

from maya import cmds, mel

fcs = cmds.ls(sl = True, flatten = True)
jnts = cmds.ls(sl = True, type = "joint")
cmds.select(jnts, tgl = True)
mel.eval("PolySelectConvert 3;")
pts = cmds.ls(fl = True)
shp = cmds.listRelatives(pts[0], p = True)[0]
xform = cmds.listRelatives(shp, p = True)[0]

cmds.select(xform, r = True)
cmds.duplicate(rr = True)
clnXform = cmds.ls(sl= True, type = "transform")[0]
clnCmps = []

for pt in pts:
  clnPt = pt.replace(xform, clnXfm)
  clnCmps.append(clnPt)

cmds.select(clnCmps, r = True)
keepClnCmps = cmds.ls(sl = True, fl = True)
cmds.select(clnXform, r = True)
mel.eval("PolySelectConvert 3;")
cmds.select(keepClnCmps, tgl = True)
keepClnCmps = cmds.ls(sl = True, fl = True)
mel.eval("PolySelectConvert 1;")
cmds.delete()
cmds.select(clnXform, r = True)
cmds.sets(n="src")

cmds.select(pts, r = True)
mel.eval("PolySelectConvert" 3;)
cmds.sets(n="tgt")

mel.eval("SelectToggleMode;")
cmds.select(clnXform, Jnts, r = True)
cmds.skinCluster(tsb = True, bm = 0, sm = 0, mi = 4) #change mi based on what part youre skinning 

cmds.select("src", "tgt", r = True)
cmds.copySkinWeights(sa = "closestPoint", ia = ["closestJoint","oneToOne", "oneToOne"], nr = True)
cmds.delete("src", "tgt", clnXform)

mel.eval("SelectToggleMode;")
print("weights transfered")
cmds.select(cl = True)


















