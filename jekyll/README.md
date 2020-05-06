# Jekyll Development Image

This image provides a development environment for building static sites using [Jekyll](https://jekyllrb.com/). The image is designed to accommodate both [GitHub Pages](https://pages.github.com/) sites and projects that use a `Gemfile` to manage their dependencies (e.g. sites hosted on [GitLab Pages](https://about.gitlab.com/stages-devops-lifecycle/pages/).) To get started using the image, ensure you have the [common prerequisites](../README.md) installed and then do the following:

1. Build the image by running the following command from the directory containing this README:
    
    ````
    docker build -t jekyll:latest .
    ````

2. Start a container by running the following command from your project's root directory:
    
    ```
    dbash jekyll
    ```

3. Build and serve your site by running the supplied [wrapper script](./wrapper/serve.sh), which configures Jekyll to ensure sites can be accessed via `127.0.0.1` (or the host system's IP address) on non-Linux systems where host networking mode is not available:
    
    ```
    serve
    ```


## Jekyll project configuration

### Using absolute URLs

The logic in the supplied [wrapper script](./wrapper/serve.sh) configures Jekyll to ensure served sites can be accessed via both `127.0.0.1` and the host system's IP address, even when absolute URLs are used. However, it is best practice to use relative URLs instead, which avoids this issue in the first place and provides maximum flexibility across all environments, irrespective of whether or not Jekyll is running inside a container. You can use relative paths by prefixing links with the following:

```
{{ "/" | relative_url }}
```

### Excluding the `.bundle` subdirectory from version control

If your project uses a `Gemfile` to manage its dependencies then you will find that gems are installed in a `.bundle` subdirectory under your project's root directory, which is done to avoid storing cached gems in the container's ephemeral filesystem. If your project is under version control then it is recommended that you exclude the `.bundle` directory, optionally adding an exception for the file `.bundle/config` if you use that to provide project-specific configuration options to the Ruby bundler.
