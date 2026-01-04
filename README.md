# Tor Myth Breaker

**Tor running does not mean you are anonymous.**  
If that sentence makes you uncomfortable, good.

Tor Myth Breaker is a small diagnostic tool built to challenge one of the most repeated  and most dangerous  assumptions in privacy and security circles:

> **“If Tor is running, I’m safe.”**

That belief is false more often than people want to admit.

This project does **not** attack Tor.  
It tests **your system, your routing, and your assumptions**.

---

## What This Tool Is

**Tor Myth Breaker is a reality check, not a comfort tool.**

It inspects a small number of critical, system level signals that decide whether Tor is actually enforcing isolation  or whether your operating system is still behaving like a normal, identifiable machine with Tor merely running in the background.

The checks are intentionally simple.

If these fail, no amount of browser hardening, extensions, or “advanced setups” will save you.

---

## What This Tool Checks

- Whether the **Tor process** is actually running  
- Whether **system traffic** still exits through the default network gateway  
- Whether **IPv6** is enabled (Tor does **not** protect IPv6 by default)

These are not rare misconfigurations.  
They are **the default state on most systems**.

---

## What This Tool Does **NOT** Do

- ❌ It does not deanonymize you  
- ❌ It does not exploit Tor  
- ❌ It does not claim Tor is useless  
- ❌ It does not provide anonymity  

Tor Myth Breaker answers **one question only**:

> **Is Tor enforcing isolation  or are you trusting it blindly?**

---

## Example Output

When Tor is running but your system routing and network stack are unchanged, the tool will say so.

No theory.  
No hand waving.  
No “it should be fine”.

Just the state your machine is actually in.

---

## Why This Exists

Most OPSEC failures are not caused by attackers.  
They are caused by **false confidence**.

Tor hides network paths.  
It does **not** magically fix:

- system routing  
- protocol leaks  
- identity correlation  
- timing signals  
- operating system behavior  

Assuming otherwise is not privacy.  
It is risk.

---

## Philosophy

Tor Myth Breaker is opinionated by design.

If basic isolation fails, advanced setups fail harder.

The goal is not to scare users.  
The goal is to **force accurate threat modeling**.

---

## License

**MIT License**

You are free to use, study, modify, audit, and redistribute this tool in clear enjoy.

The goal is not fear.  
The goal is **clarity**.
