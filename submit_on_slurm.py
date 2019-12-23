#! /bin/env python

import copy
import os
import datetime
import sys
import glob
import logging

# Slurm configuration
from CP3SlurmUtils.Configuration import Configuration
from CP3SlurmUtils.SubmitWorker import SubmitWorker
from CP3SlurmUtils.Exceptions import CP3SlurmUtilsException

# Personal files #
import parameters

def submit_on_slurm(name,args,debug=False,GPU=False):
    config = Configuration()

    config.sbatch_partition = parameters.partition
    config.sbatch_qos = parameters.QOS
    config.sbatch_workdir = parameters.main_path
    config.sbatch_time = parameters.time
    #config.sbatch_mem = parameters.mem
    #config.sbatch_additionalOptions = ['--ntask='+parameters.tasks , "--gpus=1", "--export=ALL"]
    #config.sbatch_additionalOptions = ['-n 20', '-G 1']
    config.sbatch_additionalOptions = ['-n 20','-G 1','--export=NONE']
    config.inputSandboxContent = []
    config.useJobArray = True
    config.inputParamsNames = ['scan','task']
    config.inputParams = []

    config.payload = """ """

    if GPU:
        config.payload += "export PYTHONPATH=/root6/lib:$PYTHONPATH\n"
        config.payload += "module load cp3\n" # needed on gpu to load slurm_utils
        config.payload += "module load slurm/slurm_utils\n"
    config.payload += "python3 {script} --scan ${{scan}} --task ${{task}}"
    config.payload += args

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    out_dir = parameters.main_path

    slurm_config = copy.deepcopy(config)
    slurm_working_dir = os.path.join(out_dir,'slurm',name+'_'+timestamp)

    slurm_config.batchScriptsDir = os.path.join(slurm_working_dir, 'scripts')
    slurm_config.inputSandboxDir = slurm_config.batchScriptsDir
    slurm_config.stageoutDir = os.path.join(slurm_working_dir, 'output')
    slurm_config.stageoutLogsDir = os.path.join(slurm_working_dir, 'logs')
    slurm_config.stageoutFiles = ["*.csv","*.zip","*png"]

    #slurm_config.payload = config.payload.format(scan=name,task=task)
    slurm_config.payload = config.payload.format(script=out_dir+"/MoMEMtaNeuralNet.py")

    for f in glob.glob(os.path.join(parameters.main_path,'split',name,'*.pkl')):
        task = os.path.basename(f)
        slurm_config.inputParams.append([name,task])

    # Submit job!

    logging.info("Submitting job...")
    if not debug:
        submitWorker = SubmitWorker(slurm_config, submit=True, yes=True, debug=False, quiet=False)
        submitWorker()
        logging.info("Done")
    else:
        logging.debug(slurm_config.payload)
        logging.debug(slurm_config.inputParams)
        logging.info('... don\'t worry, jobs not sent')

