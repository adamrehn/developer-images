FROM ubuntu:18.04 as builder

# The version of LLVM we will be building
ENV LLVM_VERSION 11.1.0

# Disable interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install our build prerequisites
RUN apt-get update && apt-get install -y --no-install-recommends \
		build-essential \
		ca-certificates \
		git \
		cmake \
		ninja-build \
		python3 \
		python3-distutils && \
	rm -rf /var/lib/apt/lists/*

# Clone the LLVM source code
RUN git clone --progress --depth=1 -b "llvmorg-${LLVM_VERSION}" https://github.com/llvm/llvm-project.git /tmp/llvm-project

# Patch the clang source code to automatically link against libc++abi when linking against libc++
RUN sed -i 's/CmdArgs.push_back("-lc++");/CmdArgs.push_back("-lc++");CmdArgs.push_back("-lc++abi");/' /tmp/llvm-project/clang/lib/Driver/ToolChain.cpp

# Patch the clang source code to always link against the static version of libunwind, which also requires libdl and pthreads
RUN sed -i 's/CmdArgs.push_back("-l:libunwind.so");/CmdArgs.push_back("-l:libunwind.a");CmdArgs.push_back("-ldl");CmdArgs.push_back("-lpthread");/' /tmp/llvm-project/clang/lib/Driver/ToolChains/CommonArgs.cpp

# Create a directory in which to perform the build
RUN mkdir /tmp/llvm-project/build
WORKDIR /tmp/llvm-project/build

# Configure the build
RUN cmake \
	-G Ninja \
	-DCMAKE_INSTALL_PREFIX=/opt/llvm \
	-DBUILD_SHARED_LIBS=OFF \
	-DCMAKE_BUILD_TYPE=Release \
	-DLLVM_ENABLE_PROJECTS="clang;compiler-rt;libcxx;libcxxabi;libunwind;lld" \
	-DCLANG_DEFAULT_CXX_STDLIB=libc++ \
	-DCLANG_DEFAULT_RTLIB=compiler-rt \
	-DCLANG_DEFAULT_LINKER=lld \
	-DCLANG_DEFAULT_UNWINDLIB=libunwind \
	-DLIBCXX_USE_COMPILER_RT=YES \
	-DLIBCXXABI_USE_COMPILER_RT=YES \
	-DLIBCXXABI_USE_LLVM_UNWINDER=YES \
	../llvm

# Perform the build
RUN cmake --build . && \
	cmake --build . --target install

# Copy the LLVM toolchain files into a clean image
FROM ubuntu:18.04
COPY --from=builder /opt/llvm/bin/* /usr/bin/
COPY --from=builder /opt/llvm/include/c++/v1 /usr/include/c++/v1
COPY --from=builder /opt/llvm/lib/clang /usr/lib/clang
COPY --from=builder /opt/llvm/lib/libc++.a /usr/lib/
COPY --from=builder /opt/llvm/lib/libc++abi.a /usr/lib/
COPY --from=builder /opt/llvm/lib/libc++experimental.a /usr/lib/
COPY --from=builder /opt/llvm/lib/libunwind.a /usr/lib/
COPY --from=builder /opt/llvm/libexec/* /usr/libexec/

# Create symlinks for clang, clang++ and llvm-ar
RUN ln -s /usr/bin/clang /usr/bin/cc
RUN ln -s /usr/bin/clang++ /usr/bin/c++
RUN ln -s /usr/bin/llvm-ar /usr/bin/ar

# Install build systems to use with the LLVM toolchain, along with sudo support
# (Note that we do NOT install GCC, which is present in the previous build stage)
RUN apt-get update && apt-get install -y --no-install-recommends \
		ca-certificates \
		git \
		cmake \
		libc-dev \
		ninja-build \
		python3 \
		python3-distutils \
		python3-pip \
		sudo && \
	rm -rf /var/lib/apt/lists/*

# Install the Conan package management system and override the auto-detected C++ standard library with the correct value
RUN pip3 install setuptools wheel && \
	pip3 install conan && \
	conan profile new default --detect && \
	conan profile update "settings.compiler.libcxx=libc++" default

# Disable the default "lecture" message the first time a user runs a command using sudo
RUN echo 'Defaults lecture="never"' >> /etc/sudoers

# Create a non-root user with no password and allow them to runs commands using sudo
RUN useradd --create-home --home /home/user --shell /bin/bash --uid 1000 user && \
	passwd -d user && \
	usermod -aG sudo user
USER user
