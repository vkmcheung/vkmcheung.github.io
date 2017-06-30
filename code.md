# Some useful code

---

This page contains some MATLAB/Octave code that I wrote for various things during my scientific endeavours (ha!) for which you might find helpful. 

### testpport.m

This script reads the parallel port and returns the state of the pins in terms of a decimal code. It is used for example when trying to read a trigger from an MRI scanner delivered through the parallel port to initiate an experiment.

Requires: Octave, instrument-control package, PsychToolbox3 

### calcA.m

[A is a](https://en.wikipedia.org/wiki/Law_of_identity) non-parametric [sensitivity](https://en.wikipedia.org/wiki/Detection_theory#Sensitivity_or_discriminability) measure that estimates the area under the receiver operating characteristic (ROC) given a hit rate and a false alarm rate. It was proposed by [Zhang and Mueller](https://doi.org/10.1007/s11336-003-1119-8) as a correction to its predecessor, A-prime. You can read more about it [here](https://sites.google.com/a/mtu.edu/whynotaprime/).

Requires: MATLAB/Octave


<br><br>(Back to [home](index.md)) 
