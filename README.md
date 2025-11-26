# Custom ComfyUI Nodes

This repository contains **custom nodes** for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), including:

1. **Custom Caption Generator** – Generate captions for images using BLIP (Salesforce model).  
2. **Custom Calculator** – Perform basic arithmetic operations.

---

## 1. Custom Caption Generator

### Description
Generates textual captions from input images using the BLIP model (`Salesforce/blip-image-captioning-base`).  
The node can handle PIL images or tensors from other nodes and outputs a string caption.

### Inputs
- **image** (`IMAGE`) – The image to caption.

### Outputs
- **Caption** (`STRING`) – The generated caption text.

### Features
- Automatically converts tensors to PIL images.
- Supports GPU if available.
- Returns captions as a string for ComfyUI compatibility.

## 2. Meklit's Calculator
### Description

Performs basic arithmetic operations between two floating-point numbers.

### Inputs
- num1 (FLOAT):First number.

- num2 (FLOAT):Second number.

- operand (STRING) – Operation type: "+", "-", "*", "/".

### Outputs

Result (STRING) – Computed result as text.

Here’s an **updated and clearer version** of your Installation section, reflecting the two separate node folders (`ComfyUI-Calculator` and `ComfyUI-CaptionGenerator`):

---

## Installation

1. **Clone the repository** into your ComfyUI `custom_nodes` directory:

```bash
git clone https://github.com/meklithab/comfy-ui-custom-node
```

This will create the following folders under `custom_nodes`:

* `ComfyUI-Calculator`
* `ComfyUI-CaptionGenerator`

2. **Install required Python packages**:

```bash
pip install torch torchvision transformers pillow
```

> These are needed for the Caption Generator node to work properly. The Calculator node has no extra dependencies.

3. **Restart ComfyUI** to load the new nodes.

4. You should now see:

* **"Custom Caption Generator"** under `image/captioning` category.
* **"Custom Calculator"** node under `tools` (or top-level) category.

---

