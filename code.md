# Some useful code

---

This page contains some MATLAB/Octave code that I wrote for things related to my experiments, some of which you might find helpful:

### [testpport.m](http://vkmcheung.github.io/code/testpport.m)

Reads the parallel port and returns the state of all pins in terms of a decimal code. It is for example used when trying to read a trigger pulse from an MRI scanner in order to initiate an experiment.

*Requirements: Octave, Octave instrument-control package, (PsychToolbox3)

<br>

### calcA.m

**A** is a non-parametric [sensitivity](https://en.wikipedia.org/wiki/Detection_theory#Sensitivity_or_discriminability) measure that estimates the area under the receiver operating characteristic (ROC). It was proposed by [Zhang and Mueller](https://doi.org/10.1007/s11336-003-1119-8) as a correction to its predecessors, *A'* and *A''*. You can read more about it [here](https://sites.google.com/a/mtu.edu/whynotaprime/).

*Requirements: MATLAB/Octave

<br><br>[Back to [home](index.md)]
