::: {.problem #prob-cs221hw-2-q2 origin="external" source="cs221hw-2-q2"}
In the previous problem, we used bag-of-words features for sentiment classification. It is now an outdated method of representing texts in machine learning due to many limitations. For example, it doesn't capture word relationships (e.g., "amazing" and "wonderful" are similar but treated as completely different features) and creates very sparse, high-dimensional vectors. In this problem, we'll explore how neural networks with word embeddings can address these issues.

We'll use the same set of tweets from Problem 1, but now represent each word with a dense 2-dimensional embedding vector. For simplicity, assume we have the following pre-trained word embeddings:

  Word       Embedding
  ---------- ----------------
  amazing    [0.8, 0.6]
  day        [0.2, 0.1]
  scared     [-0.5, -0.7]
  of         [0.0, 0.0]
  spiders    [-0.3, -0.4]
  love       [0.9, 0.4]
  this       [0.0, 0.0]
  so         [0.1, 0.0]
  angry      [-0.6, -0.8]
  worried    [-0.3, -0.6]
  about      [0.0, -0.1]
  tomorrow   [0.2, -0.2]
  hate       [-0.8, -0.5]
  waiting    [-0.1, -0.3]

For simplicity, we will focus on **binary sentiment classification (positive or negative)** instead of three-class classification for this problem only.

(a) **Embeddings via averaging:** One simple approach is to represent each tweet as the average of its word embeddings. Compute the averaged embedding representation for "so angry", showing your work. Comment on one advantage and one disadvantage of this approach.

*Expected:* 1.  A 2-dimensional averaged embedding vector, with your calculation shown
2.  Discuss one benefit and one limitation of creating embeddings for a text by averaging embeddings of its component words (2-3 sentences)

(b) **Forward pass:** Using the averaged representation for "so angry" from part (a), perform a forward pass step-by-step to find the predicted label $\hat{y}$. Show your intermediate calculations by filling in the table below.

For the sake of simplicity, we'll use a 2-input, 2-hidden neuron, 1-output architecture consisting of:

1.  **Input layer:** Word embeddings $\mathbf{x}$
2.  **Hidden layer:** 2 neurons with ReLU activation, where $\text{ReLU}(\mathbf{x}) = \max(0, \mathbf{x})$
3.  **Output layer:** 1 neuron (binary sentiment classification) with sigmoid activation

The forward pass equations are: $$\mathbf{h} = \text{ReLU}(\mathbf{W}^{(1)} \mathbf{x} + \mathbf{b}^{(1)})$$ $$z = \mathbf{W}^{(2)} \mathbf{h} + b^{(2)}$$ $$\hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}$$ where $\mathbf{x} = [x_1, x_2]^T$ is the 2D input representation, $\hat{y}$ is the predicted label, $\mathbf{W}^{(1)} \in \mathbb{R}^{2 \times 2}$, $\mathbf{b}^{(1)} \in \mathbb{R}^{2}$, $\mathbf{W}^{(2)} \in \mathbb{R}^{1 \times 2}$, and $b^{(2)} \in \mathbb{R}$.

**Network parameters:**
$$\mathbf{W}^{(1)} = \begin{bmatrix} 1.0 & 0.5 \\ -0.5 & 1.0 \end{bmatrix}, \quad \mathbf{b}^{(1)} = \begin{bmatrix} 0.1 \\ -0.2 \end{bmatrix}$$ $$\mathbf{W}^{(2)} = \begin{bmatrix} 0.8 & -0.6 \end{bmatrix}, \quad b^{(2)} = 0.3$$

**You should write your answers by copying and pasting the table below and filling its cells, or using bullet points to clearly state the value of each cell. Round numerical values to 3 decimal places.**

  Node/Variable     Formula/Computation   Value
  ----------------- --------------------- -------
  $x$             NA                    
  $\mathbf{h}$                         
  $z$                                   
  $\hat{y}$                            

*Expected:* 1.  Compute forward pass values at each node. Show your calculations for each step by filling in the table above

(c) **Backpropagation:** Using the same weights, bias and input vector as in part (b), first compute the loss value $L$. Then, perform backpropagation to compute gradients $\frac{\partial L}{\partial \mathbf{W}^{(1)}}$, $\frac{\partial L}{\partial \mathbf{b}^{(1)}}$, $\frac{\partial L}{\partial \mathbf{W}^{(2)}}$, and $\frac{\partial L}{\partial b^{(2)}}$. Assume the true label is $y_{\text{true}} = 0$ (negative sentiment) and we're using binary cross-entropy loss: $$L = -[y_{\text{true}} \log(\hat{y}) + (1 - y_{\text{true}}) \log(1 - \hat{y})]$$

**You should write your answers by copying and pasting the tables below and filling their cells, or using bullet points to clearly state the value of each cell. Round numerical values to 3 decimal places.**

  Variable   Formula/Computation   Value
  ---------- --------------------- -------
  $L$                            

  Gradient                                                Formula (Chain Rule)   Value
  ------------------------------------------------------- ---------------------- -------
  $\frac{\partial L}{\partial \hat{y}}$                                    
  $\frac{\partial L}{\partial z}$                                           
  $\frac{\partial L}{\partial \mathbf{h}}$                                 
  $\frac{\partial L}{\partial \mathbf{W}^{(2)}}$                          
  $\frac{\partial L}{\partial b^{(2)}}$                                    
  $\frac{\partial L}{\partial \mathbf{W}^{(1)}}$                          
  $\frac{\partial L}{\partial \mathbf{b}^{(1)}}$                          

*Expected:* 1.  Compute the loss value $L$, showing your calculation in the Formula/Computation column
2.  Starting from $\frac{\partial L}{\partial \hat{y}}$, compute gradients for each node working backwards and fill out the table given above. For the formula column, you should express each partial in terms of partials above it in the table (recall [backpropagation](https://stanford-cs221.github.io/lectures/?trace=backpropagation) from lecture!)
3.  Feel free to reuse values you already computed in part b

(d) **Embedding analysis:** Looking at the provided word embeddings, identify patterns in how positive emotion words (amazing, love), negative emotion words (scared, hate, angry), and neutral words (this, about, of) are positioned in the 2D embedding space. You don't have to plot anything for this problem; simply observe the patterns. What does this suggest about how word embeddings capture semantic relationships? Explain why embeddings might be more meaningful than the bag-of-words approach for capturing semantic relationships.

*Expected:* 1.  Describe the spatial clustering of different word types (1-2 sentences)
2.  Explain how embeddings capture semantic similarity and its advantage over the bag-of-words approach (1-2 sentences)

*Note (these notes):* Only the written parts of this handout problem are given here; its programming parts are left out (SPEC §17.13.1, item 4).
:::
