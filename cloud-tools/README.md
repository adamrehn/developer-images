# Cloud Tools Image

This image encapsulates tools for interacting with various public cloud providers. The following tools are currently included:

- [AWS Command Line Interface](https://aws.amazon.com/cli/)
- [eksctl - The official CLI for Amazon EKS](https://eksctl.io/)
- [kubectl](https://kubernetes.io/docs/reference/kubectl/) (required by eksctl)

To get started using the image, ensure you have the [common prerequisites](../README.md) installed and then do the following:

1. Build the image by running the following command from the directory containing this README:
    
    ````
    docker build -t cloud-tools:latest .
    ````

2. Start a container by running the following command from any directory:
    
    ```
    dbash cloud-tools
    ```

You can also [export aliases](../README.md#exporting-aliases) for all of the encapsulated tools.
