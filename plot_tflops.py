import matplotlib.pyplot as plt


gpus = [
    {"name": "4090", "tflops": 82.5},
    {"name": "4080 Super", "tflops": 52.5},
    {"name": "4080", "tflops": 48.7},
    {"name": "4070 TiSuper", "tflops": 44.1},
    {"name": "4070 Ti", "tflops": 40},
    {"name": "3090 Ti", "tflops": 40},
    {"name": "4070 Super", "tflops": 35.4},
    {"name": "3090", "tflops": 35.5},
    {"name": "3080 Ti", "tflops": 34.1},
    {"name": "3080", "tflops": 30.6},
    {"name": "4070", "tflops": 29},
    {"name": "4060 Ti", "tflops": 22},
    {"name": "3070 Ti", "tflops": 21.7},
    {"name": "3070", "tflops": 20.3},
    {"name": "4060", "tflops": 15.1},
    {"name": "3060", "tflops": 12.7},
    {"name": "3060 Ti", "tflops": 12.2}
  #You can add more GPUs and TFLOPs data here
]

names = [gpu['name'] for gpu in gpus]
tflops = [gpu['tflops'] for gpu in gpus]

plt.figure(figsize=(12, 8))
plt.barh(names, tflops, color='skyblue')
plt.xlabel('TFLOPS')
plt.ylabel('GPU')
plt.title('TFLOPS for Each GPU')
plt.gca().invert_yaxis()
plt.grid(axis='x')

plt.show()
