

#print( imgMap)
from matplotlib.widgets import Slider, Button
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

imgMap= mpimg.imread( 'D:\\OneDrive\\00_UNI_STUFF\\THE_FLOOD\\nicoTest\\01.jpg')
SLIDE= 10
axcolor= 'lightgoldenrodyellow'

#imgRemap= imgMap.copy()
hh= len( imgMap)
ww= len( imgMap[ 0])

#print( len( imgRemap))
def drawMap( val):
    imgRemap=[ 0.0]* hh
    for i in range( len( imgMap)):
        imgRemap[ i]=[ 0.0]* ww #* 3 # np.array( [ ww])
        # imgRGB[ i+ hh]=[ 0.0]* ww* 3 # np.array( [ ww])
        # imgRGB[ i+ hh+ hh]=[ 0.0]* ww* 3 # np.array( [ ww])
        for j in range( len( imgMap[ i])):
            #print( "imgR[ i][ j]: "+ str( img[ i][ j]))
            imgRemap[ i][ j]=[ 0.0]* 3 # np.array( [ 4])
            #imgRemap[ i][ j]= setPixel( imgMap[ i][ j])
            #print( val)
            imgRemap[ i][ j]= imgMap[ i][ j]
            newVal= imgMap[ i][ j][ 0]
            if newVal< val: imgRemap[ i][ j]=[ 0, 0, 255]
            j+= 1
        i+= 1
    return imgRemap

def reset( event): lvl_slider.reset()
def update( val): imgplot= plt.imshow( drawMap( lvl_slider.val))
    # line.set_ydata( f( t, lvl_slider.val))
    # fig.canvas.draw_idle()

imgplot= plt.imshow( drawMap( SLIDE))
ax= plt.subplot()
ax.set_xlabel( 'Map')
ax.margins( y= 1)
plt.subplots_adjust( left= 0.25, bottom= 0.1)

lvl_slider= Slider(
    ax= plt.axes( [ 0.1, 0.25, 0.03, 0.65], facecolor= axcolor),
    label= 'Sea Level',
    valmin= 0,
    valmax= 255,
    valinit= SLIDE,
    orientation="vertical"
)

lvl_slider.on_changed( update)

resetax= plt.axes( [ 0.8, 0.025, 0.1, 0.04])
button= Button( resetax, 'Reset', color=axcolor, hovercolor='0.975')

button.on_clicked( reset)
plt.show()