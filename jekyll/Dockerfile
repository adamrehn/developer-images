FROM ruby:2.7

# Configure the Ruby bundler to automatically install gems locally for each project
ENV BUNDLE_AUTO_INSTALL=true
ENV BUNDLE_DEFAULT_INSTALL_USES_PATH=true

# Install the GitHub Pages gem for GitHub Pages projects (GitLab Pages projects will use the Ruby bundler)
USER root
RUN gem install github-pages

# Install the dependencies for our wrapper script, along with sudo support
RUN apt-get update && apt-get install -y sed sudo && \
	rm -rf /var/lib/apt/lists/*

# Disable the default "lecture" message the first time a user runs a command using sudo
RUN echo 'Defaults lecture="never"' >> /etc/sudoers

# Create a non-root user with no password and allow them to runs commands using sudo
RUN useradd --create-home --home /home/user --shell /bin/bash --uid 1000 user && \
	passwd -d user && \
	usermod -aG sudo user

# Install our wrapper for invoking `jekyll serve`
COPY --chown=user:user wrapper/_config_template.yml /tmp/_config_template.yml
COPY wrapper/serve.sh /usr/local/bin/serve
RUN chmod +x /usr/local/bin/serve
USER user

# Expose port 4000 to the host under Windows and macOS (under Linux we just use host networking mode)
# (Note that you will need to run Jekyll using the supplied wrapper script for this to work correctly when using absolute URLs)
LABEL docker-shell.args.1="-e"
LABEL docker-shell.args.2="HOSTIP=\$HOSTIP"
LABEL docker-shell.windows.args.1="-p=4000:4000"
LABEL docker-shell.mac.args.1="-p=4000:4000"

# Export an alias for our wrapper script
LABEL developer-images.aliases.1="serve"
