# LLVM Toolchain Image

This image encapsulates a complete [LLVM](https://llvm.org/) compiler toolchain, including the following components:

- [Clang](https://clang.llvm.org/) C/C++/Objective-C compiler
- [libc++](https://libcxx.llvm.org/) C++ Standard Library
- [libc++abi](https://libcxxabi.llvm.org/) C++ Standard Library Support
- [compiler-rt](https://compiler-rt.llvm.org/) runtime library
- [LLD](https://lld.llvm.org/) linker

In addition to the LLVM toolchain itself, the image also includes:

- [CMake](https://cmake.org/)
- [Ninja](https://ninja-build.org/)

The clang compiler is configured to use lld, libc++ and compiler-rt by default, and will statically link against libc++, libc++abi and libunwind.

To get started using the image, ensure you have the [common prerequisites](../README.md) installed and then do the following:

1. Build the image by running the following command from the directory containing this README:
    
    ````
    docker build -t llvm-toolchain:latest .
    ````

2. Start a container by running the following command from the directory containing source code you wish to compile:
    
    ```
    dbash llvm-toolchain
    ```

This image does not support [exporting aliases](../README.md#exporting-aliases) for its encapsulated tools, since these would likely clash with compilers and build tools on the host system.
