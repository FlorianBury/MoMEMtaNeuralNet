from CP3SlurmUtils.Configuration import Configuration

config = Configuration()

#--------------------------------------------------------------------------------
# 1. SLURM sbatch command options
#--------------------------------------------------------------------------------

config.sbatch_partition = 'cp3'
config.sbatch_qos = 'cp3'
config.sbatch_workdir = '.'
config.sbatch_time = '0-4:00'
config.sbatch_mem = '2048'
config.sbatch_output = '/dev/null'
config.sbatch_error = '/dev/null'
config.sbatch_additionalOptions = []

#--------------------------------------------------------------------------------
# 2. User batch script parameters that are same for all jobs
#--------------------------------------------------------------------------------

config.environmentType = ''
config.cmsswDir = ''

config.inputSandboxContent = []
config.inputSandboxDir = ''
config.inputSandboxFilename = ''

config.batchScriptsDir = config.sbatch_workdir + '/slurm_batch_scripts'
config.batchScriptsFilename = ''

config.stageout = True
config.stageoutFiles = ['output_file_for_job_*.txt']
# We chose the filename of the outputs to be independent of the job array id number (but dependent on the job array task id number).
# So let's put the output files in a directory whose name contains the job array id number,
# so that each job array we may submit will write in a different directory.
config.stageoutDir = config.sbatch_workdir + '/slurm_outputs/job_array_${SLURM_ARRAY_JOB_ID}'

config.writeLogsOnWN = True
config.separateStdoutStderrLogs = False
config.stdoutFilename = ''
config.stderrFilename = ''
config.stageoutLogs = True
# The default filename of the slurm logs has already a job array id number and a job array task id number in it.
# So we can put all logs together (even from different job arrays we may submit) in a unique directory; they won't overwrite each other.
config.stageoutLogsDir = config.sbatch_workdir + '/slurm_logs'

config.useJobArray = True

# 2 jobs will be submitted, because the config parameter 'inputParams' has length 2.
config.numJobs = None

#--------------------------------------------------------------------------------
# 3 Job-specific input parameters and payload
#--------------------------------------------------------------------------------

config.inputParamsNames = ['outputFile']

config.inputParams = [['output_file_for_job_1.txt'], ['output_file_for_job_2.txt']]

# For job number 1, the environment variable 'outputFile' will be equal to 'output_file_for_job_1.txt'.
# For job number 2, the environment variable 'outputFile' will be equal to 'output_file_for_job_2.txt'.
# The payload will have access to environment variables like 'SLURM_ARRAY_JOB_ID' and 'SLURM_ARRAY_TASK_ID',
# so we can use those variables here.
config.payload = \
"""
echo "Start of 'Hello World' user payload for job ${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}"
echo "Hello World! I am a SLURM job with ID ${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}" > ${outputFile}
echo "  End of 'Hello World' user payload for job ${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}"
"""
