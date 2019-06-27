# MoMEMtaNeuralNet

Software to fit the Matrix Element Method using Deep Neural Networks

These scripts are used to make hyperparameter scans with Talos and learning on Keras

All scripts are **python3**

## Getting Started

This software is intended to work on Ingrid/Manneback 

### Prerequisites

Modules you will need to load
```
module load root/6.12.04-sl7_gcc73 boost/1.66.0_sl7_gcc73 gcc/gcc-7.3.0-sl7_amd64 python/python36_sl7_gcc73  cmake/cmake-3.9.6 lhapdf/6.1.6-sl7_gcc73 gcc/gcc-7.3.0-sl7_amd64 slurm/slurm_utils 

```

### Installing required python packages 

Below are the required packages that can be installed with pip.

If you do not have sysadmin rights, do not forget to use ``` pipi install --user ...  ```

- [Tensorflow](https://www.tensorflow.org/install/pip) (neural networks learning)
- [Keras](https://pypi.org/project/Keras/) (wraper around Tensorflow)
- [Talos](https://pypi.org/project/talos/) (hyperparameter scans)
- [Root_numpy](https://pypi.org/project/root-numpy/) (From ROOT trees to numpy arrays)
- [Seaborn](https://pypi.org/project/seaborn/) (Data Visualization)
- [Numpy](https://pypi.org/project/numpy/) (Data manipulation)
- [Pandas](https://pypi.org/project/pandas/) (Useful to manipulate numpy arrays altogether)
- [Astetik](https://pypi.org/project/astetik/) (Simplified templates of seborn required by Talos)
- [Enlighten](https://pypi.org/project/enlighten/) (Practical process bar)
- [Scipy](https://pypi.org/project/scipy/) (Data processing)


## Parameters



## Authors

* **Florian Bury** -- [Github](https://github.com/FlorianBury)

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
