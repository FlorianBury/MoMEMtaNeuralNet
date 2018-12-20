from CP3SlurmUtils.Configuration import Configuration

config = Configuration()

#--------------------------------------------------------------------------------
# 1. SLURM sbatch command options
#--------------------------------------------------------------------------------

# The cluster partition(s) where jobs can run.
# Comma-separated list (a comma means a union) of the following allowed values:
# 'Def' - refers to the CISM portion of the cluster;
# 'cp3' - refers to the CP3 portion of the cluster.
# CP3 users are allowed to run their jobs on the whole cluster. The same is true for non-CP3 users.
# The difference is in the priorities: CP3 users can request a special quality of service (see 'sbatch_qos' below)
# on the CP3 partition, while non-CP3 users can not. That's why CP3 users are recommended to run
# only on the CP3 partition. But if you want to submit your jobs to the CISM partition
# (e.g. because the CP3 partition is full while the CISM partition is not), you can do so by setting
# this parameter to 'Def' (or 'Def,cp3' to submit to the whole cluster).
# Defaults to 'cp3'.
# This parameter has precedence over the SLURM environment variable SBATCH_PARTITION.
#config.sbatch_partition = 'cp3'

# This parameter is used to request a given quality of service for the jobs.
# Valid values are 'normal' and 'cp3'. The quality of service 'cp3' is only allowed in the CP3 partition
# and only for CP3 users, and what it does is to boost the priority by 10000 (compare this to the maximum
# priority of 2500 in the 'normal' quality of service). Thus, the recommendation for CP3 users is to run
# on the CP3 partition with quality of service 'cp3'.
# If 'sbatch_partition' is not set to 'cp3', then 'sbatch_qos' should be set to 'normal'.
# Defaults to 'cp3' if 'sbatch_partition' is set to 'cp3'; otherwise defaults to 'normal'.
# This parameter has precedence over the SLURM environment variable SBATCH_QOS.
#config.sbatch_qos = 'cp3'

# The working directory where the SLURM batch script will be executed.
# Can be specified with a full path or with a relative path.
# In the last case, SLURM will consider it relative to the directory where the sbatch command is executed.
# If no other location is specified for the SLURM stdout and stderr files,
# this working directory will be the directory where these files will be written when a job starts running.
# This directory must exist already.
# Defaults to the current working directory (symlinks are resolved to physical paths).
#config.sbatch_workdir = '.'

# Maximum cpu time needed by each job (days-hours:minutes).
# CMS jobs should tipically not run for more than 4 hours. But if you need more, you can (and should) request it.
# Slurm will kill the jobs that use more cpu time than requested.
# Having a good estimate of the maximum cpu time your jobs need may help your jobs to start running earlier.
# Slurm has a backfill scheduling mechanism that will start lower priority jobs if doing so does not delay the expected 
# start time of any higher priority jobs. Also, since the expected start time of pending jobs depends upon the expected
# completion time of running jobs, reasonably accurate time limits are important for backfill scheduling to work well.
# Defaults to '0-04:00' (4 hours).
#config.sbatch_time = '0-04:00'

# Maximum memory per cpu needed by each job (in MB).
# CMS jobs should not use more than 2 GB. But if you imperatively need more, you can (and should) request it.
# Slurm will kill the jobs that use more memory (RSS) than requested.
# Obviously, the more you request the longer your jobs will wait in the queue for the resources to become available.
# Defaults to '2048' (2 GB).
#config.sbatch_mem = '2048'

# SLURM will connect the batch script's standard output directly to the file specified in this parameter.
# By default both standard output and standard error are directed to the same file.
# For job arrays, the default filename is "slurm-%A_%a.out", where "%A" is replaced by the job ID and "%a" with the array index.
# For other jobs, the default filename is "slurm-%j.out", where "%j" is replaced by the job ID.
# If a relative path is given, it will be relative to the work directory `sbatch_workdir`.
# If 'writeLogsOnWN' is True (the default), this parameter will default to '/dev/null'
# so that SLURM does not create log files by itself outside the worker nodes. Moreover, assigning
# to it other value than '/dev/null' will produce an error.
# Setting this parameter to None or to an empty string will not turn off the SLURM output logging;
# instead it will simply let SLURM use the default file for the standard output.
# Defaults to an empty string.
#config.sbatch_output = ''

# SLURM will connect the batch script's standard error directly to the file specified in this parameter. 
# By default both standard output and standard error are directed to the same file.
# For job arrays, the default filename is "slurm-%A_%a.out", where "%A" is replaced by the job ID and "%a" with the array index.
# For other jobs, the default filename is "slurm-%j.out", where "%j" is replaced by the job ID.
# If a relative path is given, it will be relative to the work directory `sbatch_workdir`.
# If 'writeLogsOnWN' is True (the default), this parameter will default to '/dev/null'
# so that SLURM does not create log files by itself outside the worker nodes. Moreover, assigning
# to it other value than '/dev/null' will produce an error.
# Setting this parameter to None or to an empty string will not turn off the SLURM error logging;
# instead it will simply let SLURM use the default file for the standard error.
# Defaults to an empty string.
#config.sbatch_error = ''

# Use this parameter to set any other SLURM sbatch options you may need.
# Example: config.sbatch_additionalOptions = ['--mail-type=END', '--mail-user=<your-email-address>']
# Defaults to an empty list (no additional options).
#config.sbatch_additionalOptions = []

#--------------------------------------------------------------------------------
# 2. User batch script parameters that are same for all jobs
#--------------------------------------------------------------------------------

# This parameter specifies the environment that has to be setup before the payload.
# For the moment the only possible environment setup is the CMS one, in which case
# a CMSSW work area should also be specified in the 'cmsswDir' parameter below.
# Valid values are: 'cms' (case insensitive).
# To not setup any environment, set this parameter to None or to an empty string.
# Defaults to an empty string.
#config.environmentType = ''

# For CMS jobs, this is the CMSSW work area src directory where `cmsenv` should be executed.
# This directory must exist already.
# This parameter is only relevant and mandatory when environmentType = 'cms'.
# Defaults to an empty string.
#config.cmsswDir = ''

# The input files, apart from input data in the storage, needed by the jobs.
# Do NOT include archive files (tarballs) in this list.
# A tarball (input sandbox) will be created containing all the files in this list.
# The tarball will be copied to, and unpacked in, the scratch directory of each job.
# Do NOT use absolute paths. Keep in mind also that relative paths are not only to locate the files locally,
# but also when the tarball is unpacked the relative paths are respected. That is, if you add in the input sandbox a line "mydir/*.txt",
# then all txt files present in ./mydir will be included in the input sandbox and when unpacked in the worker nodes
# you will have a directory mydir with all these txt files inside.
# Defaults to an empty list (i.e. no input sandbox).
#config.inputSandboxContent = []

# A directory (in a scratch or user area) where the input sandbox should be placed.
# If the directory doesn't exist, it will be created by the slurm_submit command.
# The jobs will copy the input sandbox from this directory once they start running.
# Defaults to the directory defined in 'sbatch_workdir'.
#config.inputSandboxDir = config.sbatch_workdir

# The filename of the input sandbox tarball.
# It is recommended to use the default in order to avoid overwritting by mistake other input sandboxes.
# Defaults to "input_sandbox_<timestamp>_<4-random-characters>.tar.gz"
#config.inputSandboxFilename = ''

# A directory where the SLURM batch script(s) should be written.
# If the directory doesn't exist, it will be created by the slurm_submit command.
# Defaults to the directory defined in 'sbatch_workdir'.
#config.batchScriptsDir = config.sbatch_workdir

# The filename of the SLURM batch script(s).
# In case of job arrays, only one batch script is created with the filename given by this parameter.
# In case of independent jobs, one batch script per job is created. The filenames are constructed from this parameter
# by appending "_<job-number>" just before the filename extension if there is one, or at the end otherwise.
# It is recommended to use the default in order to avoid overwritting by mistake other batch scripts.
# Defaults to "slurm_batch_script_<timestamp>_<4-random-characters>.sh" for job arrays,
# "slurm_batch_script_<timestamp>_<4-random-characters>_<job-number>.sh" otherwise.
#config.batchScriptsFilename = ''

# This flag tells whether to copy user files back from the worker node. 
# The files that will be copied back are the ones listed in 'stageoutFiles'.
# The stageout location should be specified in 'stageoutDir'.
# The copy is done by the batch script, after the payload.
# Note: the stageout of the job's stdout/stderr log file(s) is controlled by a separate flag ('stageoutLogs').
# Defaults to True.
#config.stageout = True

# A list with all the user files you want to stage out from the worker node.
# Only needed if 'stageout' is True.
# You don't need to include the job's stdout/stderr log file(s) in this list.
# The batch script will use the 'cp' command on each element of the list (so you can use wildcards in the filenames).
# Defaults to an empty list (i.e. no user files are copied back).
#config.stageoutFiles = []

# The stageout directory (in a scratch or user area) for the user files.
# If the directory doesn't exist, it will be created by the slurm job.
# Only needed if 'stageout' is True.
# Defaults to the directory defined in 'sbatch_workdir'.
#config.stageoutDir = config.sbatch_workdir

# When this flag is True (the default), the job's stdout/stderr log file(s) will be written
# locally on the worker nodes and the configuration parameters 'sbatch_output'
# and 'sbatch_error' will be both set to '/dev/null'.
# To retrieve the log file(s) at the end of the job execution, set 'stageoutLogs' to True (the default).
# Defaults to True.
#config.writeLogsOnWN = True

# This flag is only relevant when 'writeLogsOnWN' is True.
# By default, stdout and stderr are redirected to the same file. If this flag is set to True,
# they will instead be redirected to different files.
# Defaults to False.
#config.separateStdoutStderrLogs = False

# This parameter is only relevant when 'writeLogsOnWN' is True.
# If 'separateStdoutStderrLogs' is False (the default), this parameter sets the name of the stdout/stderr log file.
# If 'separateStdoutStderrLogs' is True, this parameter sets the name of the stdout log file.
# Defaults to "slurm-${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.out" for job arrays, "slurm-${SLURM_JOB_ID}.out" otherwise.
#config.stdoutFilename = "slurm-${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.out"

# This parameter is only relevant when 'writeLogsOnWN' and 'separateStdoutStderrLogs' are both True,
# in which case this parameter sets the name of the stderr log file.
# Defaults to "slurm-${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.err" for job arrays, "slurm-${SLURM_JOB_ID}.err" otherwise.
#config.stderrFilename = "slurm-${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.err"

# This flag tells whether to copy the job's stdout/stderr log file(s) back from the worker node.
# Only relevant when 'writeLogsOnWN' is True.
# The stageout location should be specified in 'stageoutLogsDir'.
# The copy is done by the batch script, at the very end (just before exiting).
# You don't need to include the log filename in the 'stageoutFiles' list.
# Defaults to True.
#config.stageoutLogs = True

# The stageout directory (in a scratch or user area) for the job's stdout/stderr log file(s).
# If the directory doesn't exist, it will be created by the slurm job.
# Only needed if 'stageoutLogs' is True.
# Defaults to a subdirectory named 'logs' inside the directory defined in 'stageoutDir'.
#config.stageoutLogsDir = config.stageoutDir + '/logs'

# This flag tells whether to work with a SLURM job array or with indenpendent jobs.
# Defaults to True.
#config.useJobArray = True

# This parameter must be a positive integer. It specifies how many jobs to submit.
# If you work with a job array, the array will contain (the first) `numJobs` jobs.
# If you work with independent jobs, the meaning is obvious.
# You can set it to None to deactivate it. In that case the number of jobs to submit
# will be determined by the list of input parameters.
# Defaults to None.
#config.numJobs = None

#--------------------------------------------------------------------------------
# 3 Job-specific input parameters and payload
#--------------------------------------------------------------------------------

# Job input parameters will be passed to the job via bash environment variables.
# There will be one variable per input parameter (e.g. if each of your jobs needs
# N input parameters, there will be N bash environment variables defined in each job).
# You will have to provide the variable names in the configuration parameter 'inputParamsNames'.
# The same variable names will be used for all jobs, while their values will be set per job.
# Then it is the user responsability to correctly use these variables in his/ber payload.
# The payload is a set of bash lines (which can execute programs in any other language of course).
# So one way to retrieve the input variables is to do it in the bash lines of the payload.
# The way to access a variable in bash is with the following syntax: ${variable-name}.

# This configuration parameter should be a list containing the names of the job input parameters.
# It is important that the names in this list and the values in the 'inputParams' list
# follow the same order (the slurm_submit tool will assume that this is the case).
# Defaults to an empty list (i.e. no input parameters).
#config.inputParamsNames = []

# This configuration parameter should be a list where each element is itself a list containing
# the values of the job input parameters.
# It is important that the values in this list and the names in the 'inputParamsNames' list
# follow the same order (the slurm_submit tool will assume that this is the case).
# Defaults to an empty list (i.e. no input parameters).
#config.inputParams = []

# The payload is code that you want the job to run. It consists of a set of bash lines.
# In principle, it can be as simple as "./my_code" (remember to put the file 'my_code' in the input sandbox)
# and inside 'my_code' you do whatever you want.
# For CMS jobs, the payload can be for example "cmsRun my_code".
# (Remember: for CMS jobs, the `cmsenv` command does not need to be included in the payload;
# if 'cmsswDir' is specified, `cmsenv` will be executed before running the payload inside that directory).
# No validation of the content of this parameter is done.
# If you want to propagate an error inside the payload to the job exit code, make sure the payload
# exits with the right exit code. Following the suggestion in http://www.tldp.org/LDP/abs/html/exitcodes.html
# user-defined exit codes should be in the range 79-113, but we reserved the range 100-113
# for batch script errors. Payload exit codes in the range 100-113 will be propagated
# as job exit code 103 (the general exit code used by the batch script for signaling error in user payload).
# This is a schematic example of how to use exit codes in a payload:
# config.payload = \
# """
# do something ...
# if `do something ...` failed
#    exit 79
# do something else ...
# if `do something else ...` failed
#     exit 80
# exit 0
# """
# This parameter is mandatory and has no default value.
#config.payload = None
