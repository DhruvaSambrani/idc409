# Learning

- Data (historical) Classes
- pattern exists, but is unknown

Learn from pattern in data and predict.

Let f, g such that $f,g: X\limit Y$

g is called hypothesis $g\in H$ where $H$ is hypothesis space, f is called target function. f is unknown and g is varied to find a good approximation to f

$ML: Data \rightarrow H$

# Perception Learning Algorithm

Aim is to cut the space by a hyperplane such that classification is best

$k = \sum_{i} w_i x_i = w^T x$

Here, $w^T$ is the normal to the guess hyperplane

$g(k) = 1 \text{if} k > T \text{else} -1$

$h(x) = sign(k - T)$

Same way, 

$h(x) = sign(w^Tx)$

where $h$ is the hypothesis

## Learning Step

- pick misclassified point
- Update $w^T \leftarrow w^T + yx_n$
    - This rotates the cut plane along the correct direction
- Repeat until $\delta w^T<\epsilon$

# SVM

- Max margin classifier

- Take two lines perpendicular to each other such that all x+ are above one and all x- are below the other.
- Then, $x+ = x- + \lambda w$
- Hence, $d=\lambda ||w|| = \frac{2}{||w||}$ needs to be maximised
- $\max \frac{2}{\sqrt{w^tw}}$ but must be constrained to $y w^T x > 0$

SVM only works on linear data. But what about nonlinear data? That is, what if the data cannot be classified by a single plane cut?

Then we can find a function $K$ such that $K(x)$ IS linearly separable (single plane cut). Effectively, we project the data UP a dimension and find the plane cut in THAT space.

Is this always possible?




# Confusion matrix

**!!!!!!! IMPORTANT**

| TP  | FN  |
| --- | --- |
| FP  | TN  |

Accuracy = $\frac{T}{Total}$

Precision = $\frac{TP}{P}$

Recall = $\frac{TP}{T}$

Specificity = $\frac{TN}{N}$

FPR = $\frac{FP}{F}$

TPR = $\frac{TP}{T}$

FDR = $\frac{FP}{P}$

# Decision Tree

- Bisect the space and find accuracy of classification
- Keep bisecting until node has no inaccurate cells
- OR Information Gain - $H(I) = H(A)+H(B)$ where H is entropy(?)
- OR wait until error in limit
