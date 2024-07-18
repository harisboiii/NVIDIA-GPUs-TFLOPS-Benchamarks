# GPU TFLOPS Comparison Chart

This repository contains a Python script that generates a bar plot comparing the TFLOPS (Tera Floating Point Operations Per Second) of various GPUs. The chart provides a visual representation of the performance capabilities of different GPU models, helping users to easily identify the most powerful options.

![output](https://github.com/user-attachments/assets/48d7cf15-fd62-465b-83bb-43204901c47d)


## Features

- **Data Visualization**: A horizontal bar chart that showcases the TFLOPS of each GPU.
- **Customizable**: The script can be easily modified to include additional GPUs or updated data.
- **Aesthetically Pleasing**: Enhanced plot aesthetics with labels, grid lines, and data annotations for better readability.

## Included GPUs

The chart includes the following GPUs:
- **4090**: 82.5 TFLOPS
- **4080 Super**: 52.5 TFLOPS
- **4080**: 48.7 TFLOPS
- **4070 TiSuper**: 44.1 TFLOPS
- **4070 Ti**: 40 TFLOPS
- **3090 Ti**: 40 TFLOPS
- **4070 Super**: 35.4 TFLOPS
- **3090**: 35.5 TFLOPS
- **3080 Ti**: 34.1 TFLOPS
- **3080**: 30.6 TFLOPS
- **4070**: 29 TFLOPS
- **4060 Ti**: 22 TFLOPS
- **3070 Ti**: 21.7 TFLOPS
- **3070**: 20.3 TFLOPS
- **4060**: 15.1 TFLOPS
- **3060**: 12.7 TFLOPS
- **3060 Ti**: 12.2 TFLOPS

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/gpu-tflops-comparison.git
    cd gpu-tflops-comparison
    ```

2. **Install Dependencies**:
    Ensure you have `matplotlib` installed. If not, install it using:
    ```bash
    pip install matplotlib
    ```

3. **Run the Script**:
    ```bash
    python plot_tflops.py
    ```

4. **View the Chart**:
    The script will generate and display a bar chart comparing the TFLOPS of the included GPUs.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or additional GPU data to add.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
