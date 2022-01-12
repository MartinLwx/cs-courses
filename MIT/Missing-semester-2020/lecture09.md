## Lecture 09. Security and Cryptography

---

### Entropy

> Suppose a password is chosen as a concatenation of four lower-case dictionary words, where each word is selected uniformly at random from a dictionary of size 100,000. An example of such a password is `correcthorsebatterystaple`. How many bits of entropy does this have?

In order to calculate the bits of entropy, we need to know how many possibilites there. 



We can easily know the combinations count are $100000^4$ and the bits of entropy are $log_2 (100000^4)\approx 66\ bit$ :hugs:

> Consider an alternative scheme where a password is chosen as a sequence of 8 random alphanumeric characters (including both lower-case and upper-case letters). An example is `rg8Ql34g`. How many bits of entropy does this have?

We can calcaulte the bits of entropy are $log_2(62^8)\approx 47\ bit$ :hugs:

> Which is the stronger password?

Apprarenty, `correcthorsebatterystaple` is the stronger one(its entropy is higher), which is kind of counter-intuitive. From a human perspective, `rg8Ql34g` is harder to memorize :thinking:.

> Suppose an attacker can try guessing 10,000 passwords per second. On average, how long will it take to break each of the passwords?

`correcthorsebatterystaple`: $100000^4/10000=10^{16}\ seconds\approx317097919\ years$ :sneezing_face:

`rg8Ql34g`: $64^8/10000\approx892\ years$

### **Cryptographic hash functions**

> Download a Debian image from a [mirror](https://www.debian.org/CD/http-ftp/)(e.g. [from this Argentinean mirror](http://debian.xfree.com.ar/debian-cd/current/amd64/iso-cd/)). Cross-check the hash (e.g. using the `sha256sum` command) with the hash retrieved from the official Debian site (e.g. [this file](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/SHA256SUMS) hosted at `debian.org`, if you’ve downloaded the linked file from the Argentinean mirror).

```bash
> shasum -a -256 debian-mac-11.2.0-amd64-netinst.iso
# 011f6754601985f46fcc670ce02faabcc8b5b8aadf51bc3d3fcfa3185b96b1df  debian-mac-11.2.0-amd64-netinst.iso

# correct one
# 011f6754601985f46fcc670ce02faabcc8b5b8aadf51bc3d3fcfa3185b96b1df  debian-mac-11.2.0-amd64-netinst.iso

# you can check them manually, or you do something like this
> diff <(shasum -a 256 debian-mac-11.2.0-amd64-netinst.iso) <(echo "011f6754601985f46fcc670ce02faabcc8b5b8aadf51bc3d3fcfa3185b96b1df  debian-mac-11.2.0-amd64-netinst.iso")
```

### **Symmetric cryptography**

> Encrypt a file with AES encryption, using[OpenSSL](https://www.openssl.org/): `openssl aes-256-cbc -salt -in {input filename} -out {output filename}`. Look at the contents using `cat` or `hexdump`. Decrypt it with `openssl aes-256-cbc -d -in {input filename} -out {output filename}` and confirm that the contents match the original using `cmp`

```bash
> echo "Hello world" >> sample.txt
> openssl aes-256-cbc -salt -in sample.txt -out sample.enc.txt     
# I use `password` as my password
> cat sample.enc.txt
# Salted__n��siZ�>o;w>����k��.%
> openssl aes-256-cbc -d --in sample.enc.txt  --out recover.txt
# Enter `password`
> cmp sample.txt  recover.txt
```

> 1. Set up [SSH keys](https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2) on a computer you have access to (not Athena, because Kerberos interacts weirdly with SSH keys). Make sure your private key is encrypted with a passphrase, so it is protected at rest.
> 2. [Set up GPG](https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages)
> 3. Send Anish an encrypted email ([public key](https://keybase.io/anish)).
> 4. Sign a Git commit with `git commit -S` or create a signed Git tag with`git tag -s`. Verify the signature on the commit with `git show --show-signature` or on the tag with `git tag -v`.

1. I have tried this.
2. Skip :)
3. Skip :)
4. Skip :)