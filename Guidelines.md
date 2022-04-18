# OO Python - Stack

Object-oriented Python, translation of Java's `StackOfNonNegativeIntegers` class, complete code.

## What to do?

With the help of:
- _Sphinx_ **documentation** in `docs` directory
- _Stack_ **specification**, available [here](http://pedago.sebastienjean.fr/INFO1/BUT-INFO_R2-01/Cours/04_Synthese/CM_Synthese.pdf) 
- OO Python basics, available [here](http://pedago.sebastienjean.fr/INFO1/BUT-INFO_R2-01/Cours/10_PythonObjet/CM_PythonObjet.pdf)

Use `pyCharm` IDE to:

1. define `StackOfNonNegativeIntegers` class, in appropriate package/module (cf. Sphinx documentation)


2. write a test application, in `main.py` (outside any package)

To go further:

3. apply **inheritance** mechanism:
   - define `StackOfNonNegativeIntegersWithSum` subclass
     - see _Stack with sum specification_, available [here](http://pedago.sebastienjean.fr/INFO1/BUT-INFO_R2-01/Cours/06_Heritage-(fin)-Enumerations/CM_Heritage-(fin)-Enumerations.pdf)
     - update `main.py`

     
4. apply interface mechanism:
   - rename `StackOfNonNegativeIntegers` to `ArrayStackOfNonNegativeIntegers`
   - define `StackOfNonNegativeIntegers` as an interface
   - make `ArrayStackOfNonNegativeIntegers` implementing this interface
   - update `main.py`