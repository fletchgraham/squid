import click

#folder names beginning with an underscore won't be acted upon.

@click.group()
def squid():
    pass

@squid.command()
def extract():
    pass
    # recursively unzip all files in current directory.

@squid.command()
def prune():
    pass
    # copy each folder to the home directory.
    # for each folder: put all images in a folder called textures.
    # if a folder has no obj files, add it to a list and do nothing further
    # to it.
    # put all obj files in a folder called obj.
    # delete all other files.
    # report which folders didn't have objs.

@squid.command()
def blendify():
    pass
    # for each folder in the directory.
    # open standard blender studio scene.
    # import all obj files in the folder.
    # scale to .001.
    # add all to group with the name of the folder.
    # create a principaled material with all images from the textures
    # folder sitting there ready.
    # apply that material to all imported objects.

@squid.command()
def render():
    # for each folder, render the blend file and save the image.
    # this will for sure need a progress bar.

    # by default it should render at full res and samples
    # and only the folders without rendered images will be acted on.

    # options could be --all which would render all and
    # overwrite existing renders.
    # and --half which would do a lower quality render.
    pass

@squid.command()
def images():
    # copy all the rendered images to an _images folder.
    pass

@squid.command()
def cleanup():
    # delete all but the textures folder, the blend, and the render.
    pass

@squid.command()
def rename():
    # for each folder.
    # tell the user the name and ask what the new name is.
    # rename the group in the blend, the rendered image, the blend file
    # and the folder name.
    pass
    
    
@squid.command()
def config():
    pass
    # open the squid config file in the default text editor.
    

if __name__ == '__main__':
    squid()
