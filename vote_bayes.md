# Hypergeometric Distribution

Suppose we have $N$ items that are either good or bad with $K=k$ good ones. Let's sample $n$ items. There are $k\choose x$ possible samples with $x$ good items. By the multiplication prinnciple:

$$
\begin{align*}
    \text{[\# ways to sample x good and n-x bad items]} &= \text{[\# ways to sample x good]}
    \times
    \text{[\# ways to sample n-x bad items]} \\
    &= {k \choose x} \times {N-k \choose n-x}
\end{align*}
$$

Therefore the distribution of $X$, the number of good items in a sample is:
$$
\mathbb{P}(X=x) = \frac{{k \choose x} {N-k \choose n-x}}{N \choose n}
$$

Note:
    
We are assuming, $K=k$. If $K$ is an an unknown random variable then the above is $\mathbb{P}(X=x|K=k)$, not $\mathbb{P}(X=x)$.

Our sample has at most $\min(n,k)$ good items and at most $\min(n,N-k)$ bad items.

In other words: $x \leq \min(n.k)$ and 

$n-x \leq \min(n, N-k)\iff x \geq n-\min(n, N-k) = n+\max(-n,k-N) = \max(0,n+k-N)$

# Distribution Of Sample Ballots
Suppose we have $N$ ballots with $k$ Labour ballots in grand total where we sample $n$ ballots from a mixed box. Therefore the distribution of labour votes in our sample is precisely the Hypogeometric distribution above.


Now lets **Bayes It Up!**
# Distribution of Actual ballots
Let us consider where we know $N$, have a size $n$ sample with $x$ Labour votes, but $k$ is unknown. What is the distribution of $k$, the true Labour total?

Currently we have:
$$
\mathbb{P}(x \text{ sample}|k \text{ actual}) = 
\frac{{k \choose x} {N-k \choose n-x}}{N \choose n}
\stackrel{\text{(via  Vandermonde's identity swapping n and k is legal)}}{=}
\frac{{n \choose x} {N-n \choose k-x}}{N \choose k}
$$

Now by doing our standard bayes hokus pokus:

$$
\begin{align*}
    \mathbb{P}(K=k | X=x)  =
    \mathbb{P}(k \text{ actual} | x \text{ sample}) 
    &=
    \frac
    {\mathbb{P}(x \text{ sample} | k \text{ actual}) \mathbb{P}(k \text{ actual})}
    {\mathbb{P}(x\text{ sample})} 
    &=
    \frac
    {\mathbb{P}(x \text{ sample} | k \text{ actual}) \mathbb{P}(k \text{ actual})}
    {\sum_{r=0}^N \mathbb{P}(x \text{ sample} | r \text{ actual}) \mathbb{P}(r \text{ actual})}
    \\\\
    &=
    \frac
    {{k \choose x} {N-k \choose n-x} \mathbb{P}(k \text{ actual})}
    {\sum_{r=0}^N {r \choose x} {N-r \choose n-x} \mathbb{P}(r \text{ actual})}
    &=
    \frac
    {\frac{k!}{x!(k-x)!} \frac{(N-k)!}{(n-x)!(N-k -n+x)!} \mathbb{P}(k \text{ actual})}
    {\sum_{r=0}^N 
    \frac{r!}{x!(r-x)!} 
    \frac{(N-r)!}{(n-x)!(N-r -n+x)!}
    \mathbb{P}(r \text{ actual})}
    \\\\
    &=
    \frac
    {\frac{k!}{(k-x)!} \frac{(N-k)!}{(N-k -n+x)!} \mathbb{P}(k \text{ actual})}
    {\sum_{r=0}^N 
    \frac{r!}{(r-x)!} 
    \frac{(N-r)!}{(N-r -n+x)!}
    \mathbb{P}(r \text{ actual})}
\end{align*}
$$

If we take logs thenn


$$
\begin{align*}
    \log \mathbb{P}(k \text{ actual} | x \text{ sample})
    &=
    \log \mathbb{P}(x \text{ sample} | k \text{ actual}) +
    \log \mathbb{P}(k \text{ actual})
    -
    \log (
    \sum_{r=0}^N \mathbb{P}(x \text{ sample} | r \text{ actual}) \mathbb{P}(r \text{ actual})
    )
    \\ \\
\end{align*}
$$

If we have a vector that is a scaler multiple of,
$$
[
\mathbb{P}(x \text{ sample} | r \text{ actual}) \mathbb{P}(r \text{ actual})
]_{r=0}^N
$$

then we just need to normalise it to get our posterior.

# Conjugate Prior

## Beta Binomial Disribution

Define the following distribution via pmf supporting $x \in \set{0,1,...,n}$

$$
\begin{align*}
    f(x|n,\alpha, \beta) &= {n \choose x} \frac{B(x+\alpha, n-x+\beta)}{B(\alpha, \beta)}
    \\ &= 
    {n \choose x} 
    \frac{\Gamma(x+\alpha) \Gamma(n-x+\beta) \Gamma(\alpha+\beta)}
    {\Gamma(n+\alpha+\beta) \Gamma(\alpha) \Gamma(\beta)}
    \\ &= 
    \frac{\Gamma(n+1)}{\Gamma(x+1) \Gamma(n-x+1)}
    \frac{\Gamma(x+\alpha) \Gamma(n-x+\beta) \Gamma(\alpha+\beta)}
    {\Gamma(n+\alpha+\beta) \Gamma(\alpha) \Gamma(\beta)}
    
\end{align*}
$$

This distribution arises from a binomial where $\mathbb{P}(\text{success})=\theta$ for beta distributed $\theta$. Hence this is a legal distribution.
## Transform it to define a slightly differnt distribution.
If we replace:

$n$ with $N-n$, $x$ with $k-x$, $\alpha$ with $\alpha + x$, $\beta$ with $\beta + n-x$,

We get a pmf that supports $k-x \in \set{0,1,...,N-n}$, equivalent to, $k \in \set{x,1,...,N-n+x}$.

$$
\begin{align*}
f(k-x|N-n,\alpha + x, \beta +n-x) &= 
{N-n \choose k-x} \frac{B(k-x+\alpha+x, N-n-k+x+\beta+n-x)}{B(\alpha+x, \beta+n-x)}
\\ &=
{N-n \choose k-x} \frac{B(k+\alpha, N-k+\beta)}{B(\alpha+x, \beta+n-x)}
\\ &=
{N-n \choose k-x} \frac{\Gamma(k+\alpha) \Gamma(N-k+\beta) \Gamma(n+\alpha+\beta)}
{\Gamma(\alpha+x) \Gamma(\beta+n-x) \Gamma(N+\alpha+\beta)}
\\ &=
\Gamma(k+\alpha) \Gamma(N-k+\beta)
{N-n \choose k-x} \frac{ \Gamma(n+\alpha+\beta)}
{\Gamma(\alpha+x) \Gamma(\beta+n-x) \Gamma(N+\alpha+\beta)}
\end{align*}

$$

Okay, so all I have done is define a distribution plucked out the air. Now I shalls how that it is in fact the posterior in our ballot sampling!

Let's keep a rearangment of above in our backpocket.
$$
f(k-x|N-n,\alpha + x, \beta +n-x)
\frac{\Gamma(\alpha+x) \Gamma(\beta+n-x) \Gamma(N+\alpha+\beta)}
{ \Gamma(n+\alpha+\beta)}
=
\textcolor{teal}{
    \Gamma(k+\alpha) \Gamma(N-k+\beta)
    {N-n \choose k-x}
}


$$

## Posterior.

We want to show that our posterior probability of there being $k$ ballots is a constant times the above distribution. This constant must be independant from $k$.

To do this we put a nice prior on $K$...

$$
\mathbb{P}(K=k) = f(k|N,\alpha, \beta)
$$

Then,

$$
\begin{align*}
    \mathbb{P}(K=k|X=x) = 
    \frac{\mathbb{P}(X=x|K=k) \mathbb{P}(K=k)}
    {\sum_{r=x}^{N-n+x} \mathbb{P}(X=x|K=r) \mathbb{P}(K=r)}
\end{align*}
$$

Let's look at the numerator:

$$
\begin{align*}
    \mathbb{P}(X=x|K=k) \mathbb{P}(K=k) 
    &=
    {k \choose x} {N-k \choose n-x}  f(k|N,\alpha, \beta)
    \\ \\ 
    &=
    {k \choose x} {N-k \choose n-x} 
    {N \choose k}
    \frac{\Gamma(k+\alpha) \Gamma(N-k+\beta) \Gamma(\alpha+\beta)}
    {\Gamma(N+\alpha+\beta) \Gamma(\alpha) \Gamma(\beta)}
    \\
    \\
    \Bigg[
    \text{Recall Vandermonde:}
    {k \choose x} {N-k \choose n-x}
    =
    \frac{{n \choose x} {N-n \choose k-x} {N \choose n}}{N \choose k}
    \Bigg]
    &=
    \frac{{n \choose x} {N-n \choose k-x} {N \choose n}}{N \choose k}
    {N \choose k}
    \frac{\Gamma(k+\alpha) \Gamma(N-k+\beta) \Gamma(\alpha+\beta)}
    {\Gamma(N+\alpha+\beta) \Gamma(\alpha) \Gamma(\beta)}
    \\
    &=
    {n \choose x} {N-n \choose k-x} {N \choose n}
    \frac{\Gamma(k+\alpha) \Gamma(N-k+\beta) \Gamma(\alpha+\beta)}
    {\Gamma(N+\alpha+\beta) \Gamma(\alpha) \Gamma(\beta)}
    \\ &=
    \textcolor{teal}{
        \Gamma(k+\alpha) \Gamma(N-k+\beta)
        {N-n \choose k-x}
    }
    
    {n \choose x} {N \choose n}
    \frac{ \Gamma(\alpha+\beta)}
    {\Gamma(N+\alpha+\beta) \Gamma(\alpha) \Gamma(\beta)}
    \\ &= 
    f(k-x|N-n,\alpha + x, \beta +n-x)
    \frac{\Gamma(\alpha+x) \Gamma(\beta+n-x) \Gamma(N+\alpha+\beta)}
    {\Gamma(n+\alpha+\beta)}
    {n \choose x} {N \choose n}
    \frac{ \Gamma(\alpha+\beta)}
    {\Gamma(N+\alpha+\beta) \Gamma(\alpha) \Gamma(\beta)}
    
    \\ &= 
    f(k-x|N-n,\alpha + x, \beta +n-x)
    \textcolor{pink}{
        \frac{\Gamma(\alpha+x) \Gamma(\beta+n-x) }
        {\Gamma(n+\alpha+\beta)}
        {n \choose x} {N \choose n}
        \frac{ \Gamma(\alpha+\beta)}
        {\Gamma(\alpha) \Gamma(\beta)}
    }
    
    \\
    \\ 
    \mathbb{P}(X=x|K=k) \mathbb{P}(K=k) &=
    f(k-x|N-n,\alpha + x, \beta +n-x)
    \textcolor{pink}{c(N,n,x,\alpha,\beta)}
\end{align*}
$$

This is enough to show that our prior distribution is $f(k-x|N-n,\alpha + x, \beta +n-x)$

More explicitly:

$$
\begin{align*}
    \mathbb{P}(K=k|X=x) 
    &= 
    \frac{\mathbb{P}(X=x|K=k) \mathbb{P}(K=k)}
    {\sum_{r=x}^{N-n+x} \mathbb{P}(X=x|K=r) \mathbb{P}(K=r)}
    \\
    \\
    &=
    \frac{
        f(k-x|N-n,\alpha + x, \beta +n-x)
        \textcolor{pink}{c(N,n,x,\alpha,\beta)}}
    {
        \sum_{r=x}^{N-n+x} f(r-x|N-n,\alpha + x, \beta +n-x)
        \textcolor{pink}{c(N,n,x,\alpha,\beta)}
        }
    \\
    \\
    &=
    \frac{
        f(k-x|N-n,\alpha + x, \beta +n-x)
        \textcolor{pink}{c(N,n,x,\alpha,\beta)}}
    {
        \textcolor{pink}{c(N,n,x,\alpha,\beta)}
        \sum_{r=x}^{N-n+x} f(r-x|N-n,\alpha + x, \beta +n-x)
        }
    \\
    \\
    &=
    \frac{f(k-x|N-n,\alpha + x, \beta +n-x)}
    {\sum_{r=x}^{N-n+x} f(r-x|N-n,\alpha + x, \beta +n-x)}
    \\
    \\
    &=
    f(k-x|N-n,\alpha + x, \beta +n-x)
\end{align*}
$$