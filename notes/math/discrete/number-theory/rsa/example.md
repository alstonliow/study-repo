::: {#exm-rsa-small .example name="RSA with small numbers" level="easy"}
Take $p=5$, $q=11$, so $N=55$ and $(p-1)(q-1)=40$. Choose $e=3$, which is coprime to $40$; then $d=3^{-1}\bmod40=27$, since $3\cdot27=81\equiv1$. The public key is $(55,3)$. The message $x=13$ is encrypted as $13^3\bmod55=2197\bmod55=52$, and decrypted as $52^{27}\bmod55=13$.
:::
