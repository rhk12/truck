#!/bin/bash
  
#### specify the job and project name
#SBATCH --job-name=abaqus
#SBATCH --account=rhk12

#### specify the required resources
#SBATCH --account=open
#SBATCH --partition=open
#SBATCH --nodes=1                 # Number of nodes
#SBATCH --ntasks-per-node=1       # Number of tasks per node (MPI processes)
#SBATCH --mem=128GB               # Total memory allocation
#SBATCH --time=30:00:00           # Job time limit (hh:mm:ss)

# Load necessary modules
source ~/.bashrc
module load abaqus/2022

# Change to the directory containing the job file
cd $SLURM_SUBMIT_DIR

# Ensure Abaqus uses the correct number of CPUs
total_cpus=$SLURM_NTASKS  # Total tasks (ntasks-per-node * nodes)

# Run the Abaqus job using MPI
abaqus job=Job-1 input=Job-1.inp cpus=$total_cpus mp_mode=mpi interactive
