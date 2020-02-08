# Rhino-Plugins
McNeel's Rhinoceros is a 3D modeling software widely used by architects and product designers. Its functionalities can be extended via various API provided by McNeel. This repository contains a variety of projects at intermediate stages of development.

### Installation
1. Locate .rhi file
2. Download & run
3. Accept default settings

### Oblique Transform

Oblique projection type of [axonometric projection](https://en.wikipedia.org/wiki/Axonometric_projection) used for creating a pictorial drawing of an object. Unlike other forms of axonometric projections, oblique type allows for dimensionally accurate depiction of the object. It was used widely prior to 3D digital modeling. Today's 3D softwares, however, are inherently unable to produce this form of projection. This plugin enables users to temporarily transform their models to be viewed in this particular form of representation and restore it with a click of a button.

This plugin adds the following commands:
* ObliquePlan: transforms selections to appear oblique in _plan viewport_
* ObliqueElevation: transforms selections to appear oblique in _Front viewport_
* ObliqueRestoration: restores previously transformed objects to appear normal

This plugin enables representation methods shown in the bottom row in this diagram:
<div align="center">
	<img width="30%" height="30%" src="https://upload.wikimedia.org/wikipedia/commons/4/41/Graphical_projection_comparison.png" alt="Preview">
</div>

### Random Transform

Random appearance is useful in creating scenes that appear organic. It can be difficult to emulate completely random appearance manually, however, as we tend to repeat our habits and favorite moves. These set of commands allow you to tap into the power of RND and shuffle your selection of objects with completely random values. 

This plugin adds the following commands:
* RandomMove: translates selected objects with random values extrapolated from two user-given points
* RandomRotate: rotates selections in random angles in axis of the current viewport
* RandomScale: _coming soon_

### Reference

[RhinoCommon API](https://developer.rhino3d.com/api/)


To do
[ ] Add example images to readme
[ ] Add documentation to Random Transform
[ ] Implement RandomScale command