## Supported Games
- **Resident Evil Village**
- **Resident Evil 4 Remake**

## Requirements
* [Blender 4.1 or higher](https://www.blender.org/download/)
* [RE Mesh Editor](https://github.com/NSACloud/RE-Mesh-Editor/tree/main)

## To-Do
- Add velvet material

# Installation
Click the code icon -> Download ZIP

Unpack into any directory

Go to Edit -> Preferences -> Addons -> Install and select the included uvrotate.py 

Install and enable the addon



## Usage
1. Go to File -> Append -> Shaders.blend -> Object -> Sphere.
2. Append the Sphere into your current scene.
3. Add appropritate NodeGroup to your material with Add -> Group or alternatively with F3 and search (Or for FRM_WMmultipliers just copy that and it's textures from the Sphere's material.
4. Import MDF using [RE Mesh Editor](https://github.com/NSACloud/RE-Mesh-Editor/tree/main).
5. Match the values present in the MDF with the values in the NodeGroup.
6. For hair to have anistrophy you need to make a new UV and rotate it 90 degrees (UV Rotate and Rename N-Panel does this automatically on all selected meshes).
7. For DisolveRange/DisolveThresold parameters to work tab into the NodeGroup
8. Find the ColorRamp select the first handle and right click on the factor
9. Swap the Material under Prop: to the material you have the NodeGroup under
10. Repeat step 7 for the other handle (Make new instances of the NodeGroup for every material).
