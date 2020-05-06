#!/usr/bin/env bash

# Determine if we are running under Docker Desktop, which prevents us from using host networking mode
IS_DOCKER_DESKTOP=$(ping -c 1 host.docker.internal > /dev/null 2>&1; echo $?)
if [[ "$IS_DOCKER_DESKTOP" == "0" ]]; then
	
	# Configure Jekyll so that we can access served sites via both 127.0.0.1 and the host system's IP address
	# (Based on the notes from here: <https://tonyho.net/jekyll-docker-windows-and-0-0-0-0/>)
	export JEKYLL_ENV='docker'
	export JEKYLL_SERVE_ARGS='--config=_config.yml,/tmp/_config_filled.yml'
	sed -e "s/{HOSTIP}/$HOSTIP/g" /tmp/_config_template.yml > /tmp/_config_filled.yml

else
	
	# Under Linux we use host networking mode, so served sites will automatically be available via 127.0.0.1
	# We set the host to 0.0.0.0 here to permit access from other machines on the same network, for consistency with Windows and macOS
	export JEKYLL_SERVE_ARGS='--host=0.0.0.0'
	
fi

# Determine if we are dealing with a GitHub Pages project or one that uses the Ruby bundler
if [[ -a "Gemfile" ]]; then
	
	# A Gemfile is present, so use the Ruby bundler
	bundle exec jekyll serve $JEKYLL_SERVE_ARGS "$@"
	
else
	
	# No Gemfile present, so it must be a GitHub Pages project
	jekyll serve $JEKYLL_SERVE_ARGS "$@"
	
fi
