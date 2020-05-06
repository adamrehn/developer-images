#!/usr/bin/env bash

# Configure Jekyll so that we can access served sites via both 127.0.0.1 and the host system's IP address
# (Based on the notes from here: <https://tonyho.net/jekyll-docker-windows-and-0-0-0-0/>)
export JEKYLL_ENV='docker'
export JEKYLL_SERVE_ARGS='--config=_config.yml,/tmp/_config_filled.yml'
sed -e "s/{HOSTIP}/$HOSTIP/g" /tmp/_config_template.yml > /tmp/_config_filled.yml

# Determine if we are dealing with a GitHub Pages project or one that uses the Ruby bundler
if [[ -a "Gemfile" ]]; then
	
	# A Gemfile is present, so use the Ruby bundler
	bundle exec jekyll serve $JEKYLL_SERVE_ARGS "$@"
	
else
	
	# No Gemfile present, so it must be a GitHub Pages project
	jekyll serve $JEKYLL_SERVE_ARGS "$@"
	
fi
