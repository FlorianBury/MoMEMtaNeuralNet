#! /bin/env python

import glob
import argparse
import copy
import os
import datetime
import sys

# Slurm configuration
from CP3SlurmUtils.Configuration import Configuration
from CP3SlurmUtils.SubmitWorker import SubmitWorker
from CP3SlurmUtils.Exceptions import CP3SlurmUtilsException

parser = argparse.ArgumentParser(description='Compute weights on the cluster.')
parser.add_argument('-n', '--name', type=str, help='Name of the production', required=True)
parser.add_argument('-i', '--input', type=str, help='Input file', required=True)
parser.add_argument('-m', '--max', type=int, help='Maximum number of events to process', required=True)
parser.add_argument('-c', '--check', type=str, help='Check the given path and avoids to send the outputs already been processed', required=False,default='')

args = parser.parse_args()

config = Configuration()

config.sbatch_partition = 'Def'
config.sbatch_qos = 'normal'
#config.sbatch_workdir = '.'
config.sbatch_time = '0-14:00'
#config.sbatch_mem = '2048'
#config.sbatch_additionalOptions = []
config.inputSandboxContent = []#['confs/*']
config.useJobArray = True
config.inputParamsNames = ['from', 'to', 'input', 'output']
config.inputParams = []

config.payload = """
{executable_path} --from ${{from}} --to ${{to}} --input ${{input}} --output ${{output}}
"""
#--confs-dir "../confs/"

datasets = {
        'TTbar': args.max#,
        #'TW': 20000,
        #'TbarW': 20000

        # 'ttH': 65000,
        # 'tt': 65000,

        # 'ttH': 40000,
        # 'tt': 40000,
        }

order = [
    'TTbar'#,
    #'TW',
    #'TbarW'
    ]
events_per_jobs = 30

#if round(args.max/events_per_jobs)>5000:
#    n_jobs = 2000
#    events_per_jobs = round(args.max/n_jobs)

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
timestamp = '{}_{}'.format(timestamp, args.name)
print ('Size of tree : {}, number of events per job : {}, number of jobs : {}'.format(args.max,events_per_jobs,round(args.max/events_per_jobs)))
print (timestamp)

for dataset in order:
    nevents = datasets[dataset]
    executable_path = os.path.abspath('../build/MEMWeight')
    output = "output"

    out_dir = '/home/ucl/cp3/fbury/scratch/MoMEMta_output/'

    slurm_config = copy.deepcopy(config)
    slurm_working_dir = os.path.join(out_dir,'slurm', timestamp)

    slurm_config.batchScriptsDir = os.path.join(slurm_working_dir, 'scripts')
    slurm_config.inputSandboxDir = slurm_config.batchScriptsDir
    slurm_config.stageoutDir = os.path.join(slurm_working_dir, 'output')
    slurm_config.stageoutLogsDir = os.path.join(slurm_working_dir, 'logs')
    slurm_config.stageoutFiles = [output + "*.root"]

    slurm_config.payload = config.payload.format(executable_path=executable_path)
    # Compute number of jobs
    jobs = list(range(0, nevents, events_per_jobs))
    if jobs[-1] != nevents:
        jobs += [nevents]
    jobs = list(zip(jobs[:-1], jobs[1:]))

    print ('Sending %0.f jobs'%(len(jobs)))        

    # Check #
    list_check = []
    if args.check != '':
        print (args.check)
        for f in glob.glob(args.check+'/*.root'):
            filename = f.replace(args.check,'')
            list_check.append(filename)
        if len(list_check)==0:
            print ('Wait ... could not find previous root files, is the path correct ?')
            sys.exit(1)

    # Detail jobs #
    for i, job in enumerate(jobs):
        job_output = "{}_{}.root".format(output, i)
        if job_output in list_check:
            print (job_output+' -> Already done')
            continue
        slurm_config.inputParams.append([job[0], job[1],args.input, job_output])

    # Submit job!

    print("Submitting job...")
    submitWorker = SubmitWorker(slurm_config, submit=True, yes=True, debug=False, quiet=False)
    submitWorker()
    print("Done")

