# Data Distribution

## Difference in distributions

- Parametric Tests - Z score test, t test

Mean is not always a good measure of data.
Parametric tests fail for such distributions.

- Non-Parametric Test - Used for non-normally distributed distros
    - Wilcoxon test
    - MWV Test

Powerlaws 

### Mann Whitney Test

1. Sort the union of S1 and S2
2. Sum the ranks by label = $R_i$
3. Calculate $$w_i = n_1*n_2 + n_i(n_i+1)/2 - R_i$$
4. $U = min(u_1, u_2)$
5. $$Z = \frac{u - \frac{n_1n_2}{2}}{\sqrt{n_1n_2- (n_1+n_2+1)/12}}$$

Other tests
- Chi^2 test
- T tests
- ANOVA



# Data Scaling

Data in different columns can be scaled to different values, which can skew results if not rescaled properly. 

## Fixed Rescale

$$x' = a + \frac{x - \min(x)}{\max(x)-\min(x)} (b-a)$$

## Mean/Median polishing

$$x' = x-\bar{x}$$

To normalize rows AND columns together, row operations followed by column operations will not set both to 0. Repeating the process will bring to mean = 0. This is polishing/centering.


$$Z = \frac{x-\bar{x}}{\sigma}$$

This sets $\sigma(Z) = 1$

## Quantile Normalization

Assumption: 
- No global change, even if some local changes
- Small data only

1. Sort each column while keeping tags
2. Take mean along new rows between different labels
3. Then, re-sort according to data labels

Called q-normalized.

## Log Transform

$$x' = log(x)$$

# Bias

- Correlation graphs followed by clustering allows to find dependant variables
    - Correlograms
    - Heatmap can be plotted

# Kind of plots
- Stem and leaf plot
- violin plot
- beeswarm
- Raincloud

# Categorical data


