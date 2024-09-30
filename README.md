# Use Extism PDK for Python to send HTTP(s) requests from inside WASM

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/wasm-outbound-http-examples/extism-python-pdk)


## Instructions for this devcontainer

Tested with Extism Python PDK [v0.1.0](https://github.com/extism/python-pdk/releases/tag/v0.1.0),
Extism CLI [v1.5.4](https://github.com/extism/cli/releases/tag/v1.5.4).

### Preparation

1. Open this repo in devcontainer, e.g. using Github Codespaces.
   Type or copy/paste following commands to devcontainer's terminal.


2. Install extism-python-pdk and its dependencies like Binaryen's wasm-merge and wasm-opt by invoking the official installation script:

```sh
curl -O https://raw.githubusercontent.com/extism/python-pdk/v0.1.0/install.sh
sh install.sh
```

### Building

1. Compile the example by using just-installed `extism-py` binary:

```sh
extism-py httpget.py -o HTTPRequestingPlugin.wasm
```

### Test with Extism CLI

For testing purposes, you can invoke functions from Extism plugins with [Extism CLI](https://github.com/extism/cli).

1. Install `Extism CLI` from Github releases: 

```sh
wget https://github.com/extism/cli/releases/download/v1.5.4/extism-v1.5.4-linux-amd64.tar.gz -O /tmp/extism.tar.gz
tar -xzf /tmp/extism.tar.gz -C /tmp ; mv /tmp/extism .
```

And now you have `extism` binary in current folder.

2. Run `httpget` function from extism plugin with CLI, allowing outbound connections to all hosts:

```sh
./extism call HTTPRequestingPlugin.wasm httpget --allow-host '*' --wasi
```

### Finish

Perform your own experiments if desired.

---

<sub>Created for (wannabe-awesome) [list](https://github.com/vasilev/HTTP-request-from-inside-WASM)</sub>
