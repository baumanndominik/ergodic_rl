# Ergodic reinforcement learning

This repository contains an algorithm for transforming time-series data into time-series with ergodic increments. As an example application, it contains an implementation of a game with non-ergodic dynamics and a demo where reinforcement learning agents try to learn optimal policies for this game with transformed and untransformed reward time-series. A more detailed description of the method can be found in

* Dominik Baumann, Erfaun Noorani, James Price, Ole Peters, Colm Connaughton, and Thomas B. Schön, "Reinforcement learning with non-ergodic reward increments: robustness via ergodicity transformations," Transactions on Machine Learning Research, 2025, [arXiv](https://arxiv.org/abs/2310.11335).

## Requirements

The code was developed using Python 3.9 and depends on the following libraries:

* gym 0.21.0
* numpy 1.24.2
* scipy 1.10.1
* stable-baselines3 1.8.0
* statsmodels 0.13.5
* for plotting: matplotlib 3.7.1
