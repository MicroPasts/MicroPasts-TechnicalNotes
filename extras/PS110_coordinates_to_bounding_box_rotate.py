#compatibility PhotoScan Pro 1.1.0 
#creates Custom Menu item.#this script should be put in the following folder:# C:/users/<user name>/AppData/Local/AgiSoft/PhotoScan Pro/scripts
import PhotoScan import math
def main():
	doc = PhotoScan.app.document
	for chunk in doc.chunks:
		R = chunk.region.rot		C = chunk.region.center
		T = chunk.transform.matrix		s = math.sqrt(T[0,0] ** 2 + T[0,1] ** 2 + T[0,2] ** 2)		S = PhotoScan.Matrix( [[s, 0, 0, 0], [0, s, 0, 0], [0, 0, s, 0], [0, 0, 0, 1]] )
		T = PhotoScan.Matrix( [[R[0,0],R[0,1],R[0,2], C[0]], [R[1,0],R[1,1],R[1,2],C[1]], [R[2,0],R[2,1],R[2,2],C[2]], [0,0,0,1]])
		xm = PhotoScan.Matrix( [[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]] )		ym = PhotoScan.Matrix( [[0,0,-1,0],[0,1,0,0],[1,0,0,0],[0,0,0,1]] )		zm = PhotoScan.Matrix( [[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]] )
		chunk.transform.matrix = ym * xm * S * T.inv()
		#Rotation matrices (by 90 degrees):		# the use chunk.transform = zm * S * T.inv()
	print("Script finished. Coordinate system is now parallel to Bounding Box\n")
PhotoScan.app.addMenuItem("Custom menu/Coordinates to bounding box + rotate", main)	