Container images for developer tools and environments
=====================================================

This repository contains Dockerfiles that produce container images suitable for use with the [docker-shell](https://github.com/adamrehn/docker-shell) command-line tool. These images are designed to provide self-contained and repeatable installations of various developer tools for interactive use, and range from encapsulating individual tools all the way through to representing complete development environments for working with particular middleware or frameworks. The images leverage the unique features of docker-shell to automatically configure the necessary Docker options, thus providing a convenient and concise interface.

The following container images are currently available:

- [**jekyll**](./jekyll): provides a development environment for building static sites using [Jekyll](https://jekyllrb.com/). The image is designed to accommodate both [GitHub Pages](https://pages.github.com/) sites and projects that use a `Gemfile` to manage their dependencies (e.g. sites hosted on [GitLab Pages](https://about.gitlab.com/stages-devops-lifecycle/pages/).)


## Requirements

Building and running the container images from this repository requires the following:

- An appropriate Docker installation for the host system platform:
    
    - **Windows 10:** [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
    - **macOS:** [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
    - **Linux:** [Docker Community Edition (CE)](https://docs.docker.com/engine/install/)
    

- [Python](https://www.python.org/) version 3.5 or newer

- The [docker-shell](https://github.com/adamrehn/docker-shell) Python package, version 0.0.5 or newer

- **(Optional)** To utilise GPU acceleration under Linux you will need the NVIDIA binary drivers and the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-docker)


## Legal

Copyright &copy; 2020, Adam Rehn. Licensed under the MIT License, see the file [LICENSE](./LICENSE) for details.
