#!/bin/bash -l
#SBATCH -p azuregpu1_intr
#SBATCH --gres=gpu:1
#SBATCH --chdir=/work/lyt/GPU_test
#SBATCH --job-name=test_gpu
#SBATCH --output=test_gpu_output.txt

# Load modules if necessary, e.g., Anaconda or Python environment
# module load anaconda
# source activate your_env

echo "Starting GPU test job..."
python3 test_gpu.py
echo "Job finished."