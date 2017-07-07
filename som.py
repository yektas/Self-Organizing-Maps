from mvpa2.suite import *

#white(1,1,1) black(0,0,0)
#Training inputs for RGB Colors (between 0 and 1)
colors = np.array(
         [[0., 0., 0.],
          [0., 0., 1.],
          [0., 0., 0.5],
          [0.125, 0.529, 1.0],
          [0.33, 0.4, 0.67],
          [0.6, 0.5, 1.0],
          [0., 1., 0.],
          [1., 0., 0.],
          [0., 1., 1.],
          [1., 0., 1.],
          [1., 1., 0.],
          [1., 1., 1.],
          [.33, .33, .33],
          [.5, .5, .5],
          [.66, .66, .66]])


# store the names of the colors for visualization later on
color_names = \
        ['black', 'blue', 'darkblue', 'skyblue',
         'greyblue', 'lilac', 'green', 'red',
         'cyan', 'violet', 'yellow', 'white',
         'darkgrey', 'mediumgrey', 'lightgrey']

'''
We tell the mapper to use a rectangular later with 20x30 units.
This will be the output space of the mapper
Additionally, we tell it to train the network using 400 iterations
and to use custom learning rate
'''
som = SimpleSOMMapper((20, 30), 600, learning_rate=0.05)

#Train the mapper
som.train(colors)

pl.imshow(som.K, origin='lower')

"""
And now, let's take a look onto which coordinates the initial training
prototypes were mapped to. The get those coordinates we can simply feed
the training data to the mapper and plot the output.
"""

mapped = som(colors)

pl.title('Color SOM')

# SOM's kshape is (rows x columns), while matplotlib wants (X x Y)
for i, m in enumerate(mapped):
    pl.text(m[1], m[0], color_names[i], ha='center', va='center',
           bbox=dict(facecolor='white', alpha=0.5, lw=0))

"""
The text labels of the original training colors will appear at the 'mapped'
locations in the SOM -- and should match with the underlying color.
"""

# show the figure
pl.show()
