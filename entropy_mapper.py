import matplotlib.pyplot as plt
from utils.entropy import calculate_entropy
from utils.timestamp import get_timestamp

def entropy_map(file_path):
    print(f"[{get_timestamp()}] [*] Generating entropy map for: {file_path}")
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        block_size = 512
        blocks = [data[i:i+block_size] for i in range(0, len(data), block_size)]
        entropies = [calculate_entropy(block) for block in blocks]

        plt.plot(entropies)
        plt.title("Entropy Map")
        plt.xlabel("Block #")
        plt.ylabel("Entropy")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"[{get_timestamp()}] [ERROR] Failed to map entropy: {e}")