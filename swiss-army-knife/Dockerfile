# Use the latest GDAL image as our base image, since GDAL is typically out-of-date in the Ubuntu repositories
ARG BASEIMAGE="osgeo/gdal:ubuntu-full-3.1.0"

# Build ImageMagick 7 from source, since the Ubuntu repositories only contain ImageMagick 6.9
FROM $BASEIMAGE as builder

# Install the ImageMagick build dependencies
USER root
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
		autoconf \
		automake \
		build-essential \
		chrpath \
		ghostscript \
		graphviz \
		gsfonts \
		libbz2-dev \
		libdjvulibre-dev \
		libexif-dev \
		libfftw3-dev \
		libfontconfig1-dev \
		libfreetype6-dev \
		libgraphviz-dev \
		libgs-dev \
		libjbig-dev \
		libjpeg-dev \
		liblcms2-dev \
		liblqr-1-0-dev \
		libltdl-dev \
		liblzma-dev \
		libopenexr-dev \
		libpango1.0-dev \
		libpng-dev \
		librsvg2-dev \
		libtiff-dev \
		libwebp-dev \
		libwmf-dev \
		libxml2-dev \
		zlib1g-dev && \
	rm -rf /var/lib/apt/lists/*

# Download and extract the ImageMagick source tarball
WORKDIR /tmp
RUN curl -fsSL "https://imagemagick.org/download/releases/ImageMagick-7.0.10-11.tar.gz" -o ImageMagick-7.0.10-11.tar.gz && \
	tar xvzf ImageMagick-7.0.10-11.tar.gz && \
	rm ImageMagick-7.0.10-11.tar.gz

# Configure and build ImageMagick
WORKDIR /tmp/ImageMagick-7.0.10-11
RUN ./configure \
		--prefix=/opt/imagemagick \
		--with-quantum-depth=16 \
		--enable-hdri=no \
		--enable-shared \
		--disable-static \
		--disable-docs \
		--with-gslib=yes \
		--without-perl \
		--without-magick-plus-plus \
		--without-x && \
	make && \
	make install

# Copy the ImageMagick binaries into a clean image without our build dependencies
FROM $BASEIMAGE
COPY --from=builder /opt/imagemagick /opt/imagemagick
ENV PATH "$PATH:/opt/imagemagick/bin"

# Install the ImageMagick runtime dependencies, our other tools, and sudo support
USER root
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
		ffmpeg \
		ghostscript \
		graphviz \
		gsfonts \
		libbz2-1.0 \
		libdjvulibre21 \
		libexif12 \
		libfftw3-bin \
		libfontconfig1 \
		libfreetype6 \
		libjbig0 \
		libjpeg-turbo8 \
		libjpeg8 \
		liblcms2-2 \
		liblqr-1-0 \
		libltdl7 \
		liblzma5 \
		libopenexr24 \
		libpango-1.0-0 \
		libpangocairo-1.0-0 \
		libpangoft2-1.0-0 \
		libpng16-16 \
		librsvg2-bin \
		libtiff5 \
		libtiffxx5 \
		libwebp6 \
		libwebpdemux2 \
		libwebpmux3 \
		libwmf0.2-7 \
		libxml2 \
		pandoc \
		poppler-utils \
		sudo \
		zlib1g && \
	rm -rf /var/lib/apt/lists/*

# Disable the default "lecture" message the first time a user runs a command using sudo
RUN echo 'Defaults lecture="never"' >> /etc/sudoers

# Create a non-root user with no password and allow them to runs commands using sudo
RUN useradd --create-home --home /home/user --shell /bin/bash --uid 1000 user && \
	passwd -d user && \
	usermod -aG sudo user
USER user

# Export aliases for the FFmpeg binaries
LABEL developer-images.aliases.ffmpeg.1="ffmpeg"
LABEL developer-images.aliases.ffmpeg.2="ffprobe"

# Export aliases for the GDAL binaries
LABEL developer-images.aliases.gdal.1="gdal2tiles"
LABEL developer-images.aliases.gdal.2="gdal_calc.py"
LABEL developer-images.aliases.gdal.3="gdal_contour"
LABEL developer-images.aliases.gdal.4="gdal_edit"
LABEL developer-images.aliases.gdal.5="gdal_fillnodata"
LABEL developer-images.aliases.gdal.6="gdal_grid"
LABEL developer-images.aliases.gdal.7="gdal_merge"
LABEL developer-images.aliases.gdal.8="gdal_pansharpen.py"
LABEL developer-images.aliases.gdal.9="gdal_polygonize"
LABEL developer-images.aliases.gdal.10="gdal_proximity"
LABEL developer-images.aliases.gdal.11="gdal_rasterize"
LABEL developer-images.aliases.gdal.12="gdal_retile"
LABEL developer-images.aliases.gdal.13="gdal_sieve"
LABEL developer-images.aliases.gdal.14="gdal_translate"
LABEL developer-images.aliases.gdal.15="gdal_viewshed"
LABEL developer-images.aliases.gdal.16="gdaladdo"
LABEL developer-images.aliases.gdal.17="gdalbuildvrt"
LABEL developer-images.aliases.gdal.18="gdalcompare"
LABEL developer-images.aliases.gdal.19="gdaldem"
LABEL developer-images.aliases.gdal.20="gdalinfo"
LABEL developer-images.aliases.gdal.21="gdallocationinfo"
LABEL developer-images.aliases.gdal.22="gdalmanage"
LABEL developer-images.aliases.gdal.23="gdalmdiminfo"
LABEL developer-images.aliases.gdal.24="gdalmdimtranslate"
LABEL developer-images.aliases.gdal.25="gdalmove"
LABEL developer-images.aliases.gdal.26="gdalsrsinfo"
LABEL developer-images.aliases.gdal.27="gdaltindex"
LABEL developer-images.aliases.gdal.28="gdaltransform"
LABEL developer-images.aliases.gdal.29="gdalwarp"
LABEL developer-images.aliases.gdal.30="gnmanalyse"
LABEL developer-images.aliases.gdal.31="gnmmanage"
LABEL developer-images.aliases.gdal.32="nearblack"
LABEL developer-images.aliases.gdal.33="ogr2ogr"
LABEL developer-images.aliases.gdal.34="ogrinfo"
LABEL developer-images.aliases.gdal.35="ogrlineref"
LABEL developer-images.aliases.gdal.36="ogrmerge"
LABEL developer-images.aliases.gdal.37="ogrtindex"
LABEL developer-images.aliases.gdal.38="pct2rgb"
LABEL developer-images.aliases.gdal.39="rgb2pct"

# Export aliases for the Graphviz binaries
LABEL developer-images.aliases.graphviz.1="acyclic"
LABEL developer-images.aliases.graphviz.2="bcomps"
LABEL developer-images.aliases.graphviz.3="ccomps"
LABEL developer-images.aliases.graphviz.4="circo"
LABEL developer-images.aliases.graphviz.5="cluster"
LABEL developer-images.aliases.graphviz.6="diffimg"
LABEL developer-images.aliases.graphviz.7="dijkstra"
LABEL developer-images.aliases.graphviz.8="dot"
LABEL developer-images.aliases.graphviz.9="dot2gxl"
LABEL developer-images.aliases.graphviz.10="dot_builtins"
LABEL developer-images.aliases.graphviz.11="dotty"
LABEL developer-images.aliases.graphviz.12="edgepaint"
LABEL developer-images.aliases.graphviz.13="fdp"
LABEL developer-images.aliases.graphviz.14="gc"
LABEL developer-images.aliases.graphviz.15="gml2gv"
LABEL developer-images.aliases.graphviz.16="graphml2gv"
LABEL developer-images.aliases.graphviz.17="gv2gml"
LABEL developer-images.aliases.graphviz.18="gv2gxl"
LABEL developer-images.aliases.graphviz.19="gvcolor"
LABEL developer-images.aliases.graphviz.20="gvgen"
LABEL developer-images.aliases.graphviz.21="gvmap"
LABEL developer-images.aliases.graphviz.22="gvmap.sh"
LABEL developer-images.aliases.graphviz.23="gvpack"
LABEL developer-images.aliases.graphviz.24="gvpr"
LABEL developer-images.aliases.graphviz.25="gxl2dot"
LABEL developer-images.aliases.graphviz.26="gxl2gv"
LABEL developer-images.aliases.graphviz.27="lefty"
LABEL developer-images.aliases.graphviz.28="lneato"
LABEL developer-images.aliases.graphviz.29="mingle"
LABEL developer-images.aliases.graphviz.30="mm2gv"
LABEL developer-images.aliases.graphviz.31="neato"
LABEL developer-images.aliases.graphviz.32="nop"
LABEL developer-images.aliases.graphviz.33="osage"
LABEL developer-images.aliases.graphviz.34="patchwork"
LABEL developer-images.aliases.graphviz.35="prune"
LABEL developer-images.aliases.graphviz.36="sccmap"
LABEL developer-images.aliases.graphviz.37="sfdp"
LABEL developer-images.aliases.graphviz.38="tred"
LABEL developer-images.aliases.graphviz.39="twopi"
LABEL developer-images.aliases.graphviz.40="unflatten"
LABEL developer-images.aliases.graphviz.41="vimdot"

# Export an alias for ImageMagick
LABEL developer-images.aliases.imagemagick.1="magick"

# Export an alias for Pandoc
LABEL developer-images.aliases.pandoc.1="pandoc"

# Export aliases for the poppler-utils binaries
LABEL developer-images.aliases.poppler.1="pdfattach"
LABEL developer-images.aliases.poppler.2="pdfdetach"
LABEL developer-images.aliases.poppler.3="pdffonts"
LABEL developer-images.aliases.poppler.4="pdfimages"
LABEL developer-images.aliases.poppler.5="pdfinfo"
LABEL developer-images.aliases.poppler.6="pdfseparate"
LABEL developer-images.aliases.poppler.7="pdfsig"
LABEL developer-images.aliases.poppler.8="pdftocairo"
LABEL developer-images.aliases.poppler.9="pdftohtml"
LABEL developer-images.aliases.poppler.10="pdftoppm"
LABEL developer-images.aliases.poppler.11="pdftops"
LABEL developer-images.aliases.poppler.12="pdftotext"
LABEL developer-images.aliases.poppler.13="pdfunite"
