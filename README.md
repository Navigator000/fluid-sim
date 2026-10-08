# What is this?
This project is a Python x RStudio hybrid program that uses RStudio to create a static image of a simulation of fluid movement around an object.

In this instance, the object used is a hollow cylinder. We use GCI metrics to calculate numerical error.

# What are the GCI Error Values?
Below are some numerical error values I have been able to note using details.py.

| Mesh Resolution | Lift / Value | GCI Error Rate | *
| :--- | :---: | :---: | :--- |
| **Coarse (20x20)** | 1.879 | 15.50% |
| **Medium (40x40)** | 1.908 | 6.89% |
| **Fine (80x80)** | 1.931 | 5.16% |
| **Ultra-Fine (160x160)** | 1.947 | 3.88% |

# When was this made?
This was originally programmed 6 months ago as of writing this, but has been published today as a result of some backlogs and schoolwork.

# Why was this made?
This project exists because I wanted to find a gateway into fluid mechanics and understand it more deeply. I hope this simulation does the same for you as well :)
