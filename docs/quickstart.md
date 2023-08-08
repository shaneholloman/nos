# 🔥 Quickstart

## 🛠️ Install Dependencies

You will need to install [Docker](https://docs.docker.com/get-docker/), [Nvidia Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker) and [Docker Compose](https://docs.docker.com/compose/install/).

=== "Linux (Debian/Ubuntu)"
    On Linux, you can install Docker and Docker Compose via the following commands:
    ```bash
    sudo apt-get update \
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin \
    && sudo systemctl restart docker
    ```

    Next, let's install Nvidia Docker. This will install the Nvidia Container Toolkit which is required to run GPU accelerated containers. This is only required if you plan to run the NOS server with GPU support.
    ```bash
    sudo apt-get update nvidia-container-toolkit-base
    ```

    Finally, you should be able to run the following command without any errors and the `nvidia-smi` output:
    ```bash
    docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
    ```

    If you run into issues, refer to the official Nvidia install [guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) or just ping us on [#nos-support](https://discord.gg/qEvfUcgS5m).

=== "MacOS (Intel/Apple Silicon)"
    Download and install [Docker Desktop](https://docs.docker.com/desktop/mac/install/) directly from the Docker website.

## 👩‍💻 Install NOS

We highly recommend doing all of the following inside of a Conda or Virtualenv environment. You can install Conda on your machine following the official [guide](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Create a new env:
```bash
conda create -n nos python=3.8
```

=== "Without PyTorch"

    ``` sh
    pip install autonomi-nos
    ```

=== "With PyTorch"

    ``` sh
    pip install autonomi-nos[torch]"
    ```
    This will install the `torch` extra dependencies for NOS. If you plan to run the NOS server locally (i.e. outside docker), you will also need to install the `server` extra dependencies:
    ```sh
    pip install autonomi-nos[torch,server]"
    ```

    **Note:** For running the NOS server, Python 3.8 is currently required to run the server on MacOS due to Ray requirements. If you don't plan to run the server locally then this requirement can be relaxed.

## ⚡️ Start the NOS backend server

There are three ways to launch the NOS server:

=== "Via SDK"

    You can start the nos server programmatically via the NOS SDK:
    ```python
    import nos

    nos.init(runtime="auto")
    ```

=== "Via CLI"

    Start the nos server with the appropriate backend:
    ```bash
    nos docker start --runtime=gpu
    ```
    Alternatively, you can run the server with CPU support by replacing `--runtime=gpu` with `--runtime=cpu`.

=== "Via Docker Compose"

    Navigate to the `examples/quickstart` folder and run:
    ```bash
    docker compose -f docker-compose.quickstart.yml up
    ```

We're now ready to issue our first inference request with NOS!


## 🚀 Run Inference
Try out an inference request via the CLI or [Python SDK](https://pypi.org/project/autonomi-nos):

=== "Via [Python SDK](https://pypi.org/project/autonomi-nos)"

    ```python
    from nos.client import InferenceClient, TaskType

    client = InferenceClient()
    response = client.Run(
        task=TaskType.IMAGE_GENERATION
        model_name="stabilityai/stable-diffusion-2",
        texts=["astronaut on the moon"],
        num_images=1, width=512, height=512)
    img = response["images"][0]
    ```

=== "Via CLI"
    ```bash
    nos predict txt2img -i "dog riding horse"
    ```

If you run into issues after following this guide, feel free to ping us on [#nos-support](https://discord.gg/qEvfUcgS5m).