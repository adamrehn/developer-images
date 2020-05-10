# Swiss Army Knife Tools Image

This image encapsulates multiple tools for converting and manipulating a variety of file formats, including multimedia files, raster images, text and PDF documents. The following tools are included:

- [FFmpeg](https://www.ffmpeg.org/)
- [GDAL](https://gdal.org/)
- [Graphviz](https://www.graphviz.org/)
- [ImageMagick](https://imagemagick.org/index.php)
- [Pandoc](https://pandoc.org/)
- [Poppler utilities](https://poppler.freedesktop.org/)

To get started using the image, ensure you have the [common prerequisites](../README.md) installed and then do the following:

1. Build the image by running the following command from the directory containing this README:
    
    ````
    docker build -t swissarmy:latest .
    ````

2. Start a container by running the following command from the directory containing files you wish to convert or manipulate:
    
    ```
    dbash swissarmy
    ```

You can also [export aliases](../README.md#exporting-aliases) for all of the encapsulated tools.
