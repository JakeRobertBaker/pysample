# Hypergeometric Distribution

Suppose we have $N$ items that are either good or bad with $K$ good ones. Let's sample $n$ items. There are $K\choose x$ possible samples with $x$ good items. By the multiplication prinnciple:

$$
\begin{align*}
    \text{[\# ways to sample x good and n-x bad items]} &= \text{[\# ways to sample x good]}
    \times
    \text{[\# ways to sample n-x bad items]} \\
    &= {K \choose x} \times {N-K \choose n-x}
\end{align*}
$$

Therefore the distribution of $X$, the number of good items in a sample is:
$$
\mathbb{P}(X=x) = \frac{{K \choose x} {N-K \choose n-x}}{N \choose n}
$$

Note:

Our sample has at most $\min(n,K)$ good items and at most $\min(n,N-K)$ bad items.

In other words: $x \leq \min(n.K)$ and 

$n-x \leq \min(n, N-K)\iff x \geq n-\min(n, N-K) = n+\max(-n,K-N) = \max(0,n+K-N)$

# Distribution Of Sample Ballots
Suppose we have $N$ ballots with $K$ Labour ballots in grand total where we sample $n$ ballots from a mixed box. Therefore the distribution of labour votes in our sample is precisely the Hypogeometric distribution above.


Now lets **Bayes It Up!**
# Distribution of Actual ballots
Let us consider where we know $N$, have a size $n$ sample with $x$ Labour votes, but $K$ is unknown. What is the distribution of $K$, the true Labour total?

Currently we have:

$$
\mathbb{P}(x \text{ sample}|K \text{actual}) = \frac{{K \choose x} {N-K \choose n-x}}{N \choose n}
$$

Now by doing our standard bayes hokus pokus:

$$
 


\begin{align*}
    \mathbb{P}(K \text{actual} | x \text{ sample}) 
    &=
    \frac
    {\mathbb{P}(x \text{ sample} | K \text{actual}) \mathbb{P}(K \text{actual})}
    {\mathbb{P}(x\text{ sample})} 
    \\ \\
    &=
    \frac
    {\mathbb{P}(x \text{ sample} | K \text{actual}) \mathbb{P}(K \text{actual})}
    {\sum_{r=0}^N \mathbb{P}(x \text{ sample} | r \text{ actual}) \mathbb{P}(r \text{ actual})}
    \\ \\
    &=
    \frac
    {{K \choose x} {N-K \choose n-x} \mathbb{P}(K \text{ actual})}
    {\sum_{r=0}^N {r \choose x} {N-r \choose n-x} \mathbb{P}(r \text{ actual})}
    \\ \\
    &=
    \frac
    {\frac{K!}{x!(K-x)!} \frac{(N-K)!}{(n-x)!(N-K -n+x)!} \mathbb{P}(K \text{ actual})}
    {\sum_{r=0}^N 
    \frac{r!}{x!(r-x)!} 
    \frac{(N-r)!}{(n-x)!(N-r -n+x)!}
    \mathbb{P}(r \text{ actual})}
    \\ \\
    &=
    \frac
    {\frac{K!}{(K-x)!} \frac{(N-K)!}{(N-K -n+x)!} \mathbb{P}(K \text{ actual})}
    {\sum_{r=0}^N 
    \frac{r!}{(r-x)!} 
    \frac{(N-r)!}{(N-r -n+x)!}
    \mathbb{P}(r \text{ actual})}
\end{align*}
$$

If we take logs thenn


$$
\begin{align*}
    \log \mathbb{P}(K \text{actual} | x \text{ sample})
    &=
    \log \mathbb{P}(x \text{ sample} | K \text{actual}) +
    \log \mathbb{P}(K \text{actual})
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