print("Running test_gpu.py")
import torch

def test_gpu():
    print("Checking GPU availability...")
    if torch.cuda.is_available():
        print(f"CUDA is available. Device count: {torch.cuda.device_count()}")
        device = torch.device("cuda:0")
        print(f"Using device: {torch.cuda.get_device_name(device)}")

        # 矩阵乘法测试
        a = torch.randn((1000, 1000), device=device)
        b = torch.randn((1000, 1000), device=device)
        print("Performing matrix multiplication on GPU...")
        c = torch.matmul(a, b)

        print("Matrix multiplication completed.")
        print(f"Result tensor shape: {c.shape}")
        print("GPU test successful.")
    else:
        print("CUDA is not available. GPU test failed.")

if __name__ == "__main__":
    test_gpu()