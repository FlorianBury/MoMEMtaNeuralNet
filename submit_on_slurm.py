#! /bin/env python

import copy
import os
import datetime
import sys
import glob

# Slurm configuration
from CP3SlurmUtils.Configuration import Configuration
from CP3SlurmUtils.SubmitWorker import SubmitWorker
from CP3SlurmUtils.Exceptions import CP3SlurmUtilsException

# Personal files #
import parameters


def submit_on_slurm(name):
    config = Configuration()

    config.sbatch_partition = 'cp3'
    config.sbatch_qos = 'cp3'
    config.sbatch_workdir = '/home/ucl/cp3/fbury/MoMEMtaNeuralNet/'
    config.sbatch_time = '0-4:00'
    config.sbatch_mem = '2048'
    config.sbatch_additionalOptions = []
    config.inputSandboxContent = []
    config.useJobArray = True
    config.inputParamsNames = ['scan','task']
    config.inputParams = []

    config.payload = """
    python {script} --scan ${{scan}} --task ${{task}} --DY --TT  
    """
    print (config.sbatch_workdir)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    out_dir = parameters.main_path

    slurm_config = copy.deepcopy(config)
    slurm_working_dir = os.path.join(out_dir,'slurm', timestamp)

    slurm_config.batchScriptsDir = os.path.join(slurm_working_dir, 'scripts')
    slurm_config.inputSandboxDir = slurm_config.batchScriptsDir
    slurm_config.stageoutDir = os.path.join(slurm_working_dir, 'output')
    slurm_config.stageoutLogsDir = os.path.join(slurm_working_dir, 'logs')
    slurm_config.stageoutFiles = ["*.csv"]

    #slurm_config.payload = config.payload.format(scan=name,task=task)
    slurm_config.payload = config.payload.format(script=out_dir+"/MoMEMtaNeuralNet.py")

    for f in glob.glob('split/*.pkl'):
        task = os.path.basename(f)
        slurm_config.inputParams.append([name,task])

    # Submit job!

    print("Submitting job...")
    submitWorker = SubmitWorker(slurm_config, submit=True, yes=True, debug=False, quiet=False)
    submitWorker()
    print("Done")

