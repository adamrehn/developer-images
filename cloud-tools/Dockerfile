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
		lsb-release \
		software-properties-common \
		unzip && \
	rm -rf /var/lib/apt/lists/*

# Add the Google Cloud distribution and public key
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl --silent "https://packages.cloud.google.com/apt/doc/apt-key.gpg" | apt-key --keyring "/usr/share/keyrings/cloud.google.gpg" add -

# Add the HashiCorp distribution and public key
RUN curl -fsSL "https://apt.releases.hashicorp.com/gpg" | apt-key add -
RUN apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"

# Add the Microsoft distribution and public key
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/azure-cli.list
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null

# Install the AWS CLI
RUN curl --silent -L "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/awscliv2.zip && \
	unzip /tmp/awscliv2.zip -d /tmp && \
	./tmp/aws/install && \
	rm -rf ./tmp/aws && \
	rm /tmp/awscliv2.zip

# Install the Azure CLI, the Google Cloud SDK, Packer and Terraform
RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
		azure-cli \
		google-cloud-sdk \
		packer \
		terraform && \
	rm -rf /var/lib/apt/lists/*

# Install kubectl
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

# Bind-mount the boto configuration directory (used by the AWS SDK)
LABEL docker-shell.mounts.2="~/.boto:/home/user/.boto"

# Bind-mount the Azure CLI configuration directory
LABEL docker-shell.mounts.2="~/.azure:/home/user/.azure"

# Bind-mount the gcloud configuration directory
LABEL docker-shell.mounts.3="~/.config/gcloud:/home/user/.config/gcloud"

# Bind-mount the kubectl configuration directory
LABEL docker-shell.mounts.4="~/.kube:/home/user/.kube"

# Propagate AWS credentials from the host system
LABEL docker-shell.args.01="-e"
LABEL docker-shell.args.02="AWS_ACCESS_KEY_ID"
LABEL docker-shell.args.03="-e"
LABEL docker-shell.args.04="AWS_SECRET_ACCESS_KEY"
LABEL docker-shell.args.05="-e"
LABEL docker-shell.args.06="AWS_DEFAULT_REGION"

# Propagate Packer and Terraform logging configuration from the host system
LABEL docker-shell.args.07="-e"
LABEL docker-shell.args.08="PACKER_LOG"
LABEL docker-shell.args.09="-e"
LABEL docker-shell.args.10="TF_LOG"

# Export aliases for the AWS CLI and eksctl
LABEL developer-images.aliases.aws="aws"
LABEL developer-images.aliases.eksctl="eksctl"

# Export an alias for the Azure CLI
LABEL developer-images.aliases.az="az"

# Export an alias for gcloud
LABEL developer-images.aliases.gcloud="gcloud"

# Export an alias for kubectl
LABEL developer-images.aliases.kubectl="kubectl"

# Export aliases for Packer and Terraform
LABEL developer-images.aliases.packer="packer"
LABEL developer-images.aliases.terraform="terraform"
