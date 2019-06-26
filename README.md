# MoMEMtaNeuralNet

Software to fit the Matrix Element Method using Deep Neural Networks
These scripts are used to make hyperparameter scans with Talos and learning on Keras
All scripts are **python3**

## Getting Started

This software is intended to work on Ingrid/Manneback 
Modules required : 

### Prerequisites

Modules you will need to load
```
module load root/6.12.04-sl7_gcc73 boost/1.66.0_sl7_gcc73 gcc/gcc-7.3.0-sl7_amd64 python/python36_sl7_gcc73  cmake/cmake-3.9.6 lhapdf/6.1.6-sl7_gcc73 gcc/gcc-7.3.0-sl7_amd64 slurm/slurm_utils 

```

### Installing required python packages 

Below are the required packages that can be installed with pip.
If you do not have sysadmin rights, do not forget to use ``` pipi install --user ...  ```

-[Tensorflow](https://www.tensorflow.org/install/pip) (neural networks learning)
-[Keras](https://pypi.org/project/Keras/) (wraper around Tensorflow)
-[Talos](https://pypi.org/project/talos/) (hyperparameter scans)
-[Root_numpy](https://pypi.org/project/root-numpy/) (From ROOT trees to numpy arrays)
-[Seaborn](https://pypi.org/project/seaborn/) (Data Visualization)
-[Numpy](https://pypi.org/project/numpy/) (Data manipulation)
-[Pandas](https://pypi.org/project/pandas/) (Useful to manipulate numpy arrays altogether)
-[Astetik](https://pypi.org/project/astetik/) (Simplified templates of seborn required by Talos)
-[Enlighten](https://pypi.org/project/enlighten/) (Practical process bar)
-[Scipy](https://pypi.org/project/scipy/) (Data processing)


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
