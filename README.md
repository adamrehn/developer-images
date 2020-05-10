Container images for developer tools and environments
=====================================================

This repository contains Dockerfiles that produce container images suitable for use with the [docker-shell](https://github.com/adamrehn/docker-shell) command-line tool. These images are designed to provide self-contained and repeatable installations of various developer tools for interactive use, and range from encapsulating individual tools all the way through to representing complete development environments for working with particular middleware or frameworks. The images leverage the unique features of docker-shell to automatically configure the necessary Docker options, thus providing a convenient and concise interface.

The following container images are currently available:

- [**jekyll**](./jekyll): provides a development environment for building static sites using [Jekyll](https://jekyllrb.com/). The image is designed to accommodate both [GitHub Pages](https://pages.github.com/) sites and projects that use a `Gemfile` to manage their dependencies (e.g. sites hosted on [GitLab Pages](https://about.gitlab.com/stages-devops-lifecycle/pages/).)

- [**swiss-army-knife**](./swiss-army-knife): encapsulates multiple tools for converting and manipulating a variety of file formats, including multimedia files, raster images, text and PDF documents.


## Requirements

Building and running the container images from this repository requires the following:

- An appropriate Docker installation for the host system platform:
    
    - **Windows 10:** [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
    - **macOS:** [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
    - **Linux:** [Docker Community Edition (CE)](https://docs.docker.com/engine/install/)
    

- [Python](https://www.python.org/) version 3.5 or newer

- The [docker-shell](https://github.com/adamrehn/docker-shell) Python package, version 0.0.7 or newer

- **(Optional)** To utilise GPU acceleration under Linux you will need the NVIDIA binary drivers and the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker)


## Exporting aliases

Most of the container images produced by the Dockerfiles in this repository contain additional metadata specifying the useful commands supported by their containers. You can run the [generate-aliases.py](generate-aliases.py) Python script from the root of this repository to generate wrapper scripts on the host system that will invoke these tools directly via docker-shell. Adding the directory containing the generated aliases to your system's `PATH` environment variable will allow you to run the aliased commands without the intermediate step of first creating an interactive shell. This can be convenient for scripting purposes or when mixing commands from different container images, although it is important to remember that the tools are still run inside containers in exactly the same manner as shells are, which limits them to accessing host system files within the current working directory or its subdirectories.


## Legal

Copyright &copy; 2020, Adam Rehn. Licensed under the MIT License, see the file [LICENSE](./LICENSE) for details.
