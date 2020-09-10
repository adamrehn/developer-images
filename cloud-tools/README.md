# Cloud Tools Image

This image encapsulates tools for interacting with various public cloud providers. The following tools are currently included:

- [AWS Command Line Interface](https://aws.amazon.com/cli/)
- [eksctl - The official CLI for Amazon EKS](https://eksctl.io/)
- [gcloud - Google Cloud SDK Command Line Interface](https://cloud.google.com/sdk/gcloud)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/) (used by eksctl and gcloud)

To get started using the image, ensure you have the [common prerequisites](../README.md) installed and then do the following:

1. Build the image by running the following command from the directory containing this README:
    
    ````
    docker build -t cloudtools:latest .
    ````

2. Start a container by running the following command from any directory:
    
    ```
    dbash cloudtools
    ```

You can also [export aliases](../README.md#exporting-aliases) for all of the encapsulated tools.
