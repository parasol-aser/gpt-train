#!/bin/bash

source /sw/eb/sw/Anaconda3/2022.05/etc/profile.d/conda.sh
conda activate base

export WORLD_SIZE=4

export MASTER_PORT=$(expr 10000 + $(echo -n $SLURM_JOBID | tail -c 4))
master_addr=$(getent hosts $(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1) | awk '{ print $1 }')
export MASTER_ADDR=$master_addr
echo "MASTER_ADDR="$MASTER_ADDR
echo "MASTER_PORT="$MASTER_PORT 

NODE_RANK=$SLURM_NODEID
torchrun --nproc_per_node=2 --nnodes=$SLURM_NNODES --node_rank=$NODE_RANK --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT train.py config/train_gpt2_large.py

