# Dimension Reduction

- Reduce space
- Simplified understanding

# Correlation matrix

$A_{ij} = E[Y_i-\bar{Y_i}Y_j-\bar{Y_j}] = E[Y_i' Y_j'] = 1/n(\gamma\gamma^T$

Take linear combination such that vectors are orthogonal, or that correlations are 0. This is done by diagonalization.

Find $Y  = PX$ such that $C_Y = \frac{1}{n} YY^T$ is diagonalizable.

# PCA

$C_Y = YY^T$
$C_Y = PC_XP^T$

Decompose $C_x$ as $EDE^T$ where D is diagonalized and $E$ is unitary

Then, 

$P=E^-1=E^T$

Hence

$P$'s rows are eigenvectors of $C_x$

Higher eigenvalues of $C_Y$ is kept, others ignored.

Now, we can take $y * P^T$ to find the cooefficients in that basis.


## SVD

SVD is used to find $P^T$, where the LEFT Unitary matrix is $P^T$

# LDA 

Linear Discriminant Analysis

- Maximize class separation

Finding the subspace of data such that in-class variance is minimized and distance of class is minimised

Maximize $\frac{M_1-M_2}{\sigma_1 +\sigma_2}$

$S_w = \frac{[cov_a] + [cov_b]}{2}$

$S_b = S_t - S_w$ 

Hence, we maximize $\frac{S_b}{S_w} = S_w-1 S_b$ which is given by $S_wS_bv_1 = \lambda_1 v_1$

