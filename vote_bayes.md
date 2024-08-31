# Hypergeometric Distribution

Suppose we have $N$ items that are either good or bad with $K$ good ones. Let's sample $n$ items. There are $K\choose k$ possible samples with $k$ good items. By the multiplication prinnciple:

$$
\begin{align*}
    \text{[\# ways to sample k good and n-k bad items]} &= \text{[\# ways to sample k good]}
    \times
    \text{[\# ways to sample n-k bad items]} \\
    &= {K \choose k} \times {N-K \choose n-k}
\end{align*}
$$

Therefore the distribution of $X$, the number of good items in a sample is:
$$
\mathbb{P}(X=k) = \frac{{K \choose k} {N-K \choose n-k}}{N \choose n}
$$

Note:

Our sample has at most $\min(n,K)$ good items and at most $\min(n,N-K)$ bad items.

In other words: $k \leq \min(n.K)$ and 

$n-k \leq \min(n, N-K)\iff k \geq n-\min(n, N-K) = n+\max(-n,K-N) = \max(0,n+K-N)$

# Distribution Of Sample Ballots
Suppose we have $N$ ballots with $K$ Labour ballots in grand total where we sample $n$ ballots from a mixed box. Therefore the distribution of labour votes in our sample is precisely the Hypogeometric distribution above.


Now lets **Bayes It Up!**
# Distribution of Actual ballots
Let us consider where we know $N$, have a size $n$ sample with $k$ Labour votes, but $K$ is unknown. What is the distribution of $K$, the true Labour total?

Currently we have:

$$
\mathbb{P}(k \text{ sample}|K \text{actual}) = \frac{{K \choose k} {N-K \choose n-k}}{N \choose n}
$$

Now by doing our standard bayes hokus pokus:

$$
 


\begin{align*}
    \mathbb{P}(K \text{actual} | k \text{ sample}) 
    &=
    \frac
    {\mathbb{P}(k \text{ sample} | K \text{actual}) \mathbb{P}(K \text{actual})}
    {\mathbb{P}(k\text{ sample})} 
    \\ \\
    &=
    \frac
    {\mathbb{P}(k \text{ sample} | K \text{actual}) \mathbb{P}(K \text{actual})}
    {\sum_{r=0}^N \mathbb{P}(k \text{ sample} | r \text{ actual}) \mathbb{P}(r \text{ actual})}
    \\ \\
    &=
    \frac
    {{K \choose k} {N-K \choose n-k} \mathbb{P}(K \text{ actual})}
    {\sum_{r=0}^N {r \choose k} {N-r \choose n-k} \mathbb{P}(r \text{ actual})}
    \\ \\
    &=
    \frac
    {\frac{K!}{k!(K-k)!} \frac{(N-K)!}{(n-k)!(N-K -n+k)!} \mathbb{P}(K \text{ actual})}
    {\sum_{r=0}^N 
    \frac{r!}{k!(r-k)!} 
    \frac{(N-r)!}{(n-k)!(N-r -n+k)!}
    \mathbb{P}(r \text{ actual})}
    \\ \\
    &=
    \frac
    {\frac{K!}{(K-k)!} \frac{(N-K)!}{(N-K -n+k)!} \mathbb{P}(K \text{ actual})}
    {\sum_{r=0}^N 
    \frac{r!}{(r-k)!} 
    \frac{(N-r)!}{(N-r -n+k)!}
    \mathbb{P}(r \text{ actual})}
\end{align*}
$$

If we take logs thenn


$$
\begin{align*}
    \log \mathbb{P}(K \text{actual} | k \text{ sample})
    &=
    \log \mathbb{P}(k \text{ sample} | K \text{actual}) +
    \log \mathbb{P}(K \text{actual})
    -
    \log (
    \sum_{r=0}^N \mathbb{P}(k \text{ sample} | r \text{ actual}) \mathbb{P}(r \text{ actual})
    )
    \\ \\
\end{align*}
$$