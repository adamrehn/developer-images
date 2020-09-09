FROM ubuntu:20.04

# Install our required system packages
USER root
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
		apt-transport-https \
		ca-certificates \
		curl \
		gnupg2 \
		groff \
		less \
		software-properties-common \
		unzip && \
	rm -rf /var/lib/apt/lists/*

# Install the AWS CLI
RUN curl --silent -L "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/awscliv2.zip && \
	unzip /tmp/awscliv2.zip -d /tmp && \
	./tmp/aws/install && \
	rm -rf ./tmp/aws && \
	rm /tmp/awscliv2.zip

# Install kubectl (required by eksctl)
ARG KUBECTL_VERSION=1.19.0
RUN curl --silent -L "https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl" -o /usr/local/bin/kubectl
RUN chmod a+x /usr/local/bin/kubectl

# Install eksctl
RUN curl --silent -L "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /usr/local/bin

# Disable the default "lecture" message the first time a user runs a command using sudo
RUN echo 'Defaults lecture="never"' >> /etc/sudoers

# Create a non-root user with no password and allow them to runs commands using sudo
RUN useradd --create-home --home /home/user --shell /bin/bash --uid 1000 user && \
	passwd -d user && \
	usermod -aG sudo user
USER user

# Bind-mount the SSH configuration directory
LABEL docker-shell.mounts.1="~/.ssh:/home/user/.ssh"

# Bind-mount the kubectl configuration directory
LABEL docker-shell.mounts.2="~/.kube:/home/user/.kube"

# Propagate AWS credentials from the host system
LABEL docker-shell.args.1="-e"
LABEL docker-shell.args.2="AWS_ACCESS_KEY_ID"
LABEL docker-shell.args.3="-e"
LABEL docker-shell.args.4="AWS_SECRET_ACCESS_KEY"
LABEL docker-shell.args.5="-e"
LABEL docker-shell.args.6="AWS_DEFAULT_REGION"

# Export aliases for the AWS CLI and eksctl
LABEL developer-images.aliases.aws="aws"
LABEL developer-images.aliases.eksctl="eksctl"

# Export an alias for kubectl
LABEL developer-images.aliases.kubectl="kubectl"
