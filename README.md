# Tor Myth Breaker

**Because running Tor is not the same as being anonymous.**

Tor Myth Breaker is a small diagnostic tool designed to challenge a widespread misconception in security and privacy communities:

> If Tor is running, you are anonymous.

That statement is false.

This project does not attack Tor.  
It tests *your OPSEC*.

---

## What This Tool Is

Tor Myth Breaker is a **reality check**.

It inspects a few critical system level signals to determine whether Tor is actually isolating your traffic  or whether your operating system is still behaving like a normal, trackable machine.

The checks are intentionally minimal and opinionated.  
If these fail, more complex setups will fail too.

---

## What This Tool Checks

 Whether the Tor process is actually running
 Whether system traffic is still routed through the default gateway
 Whether IPv6 is enabled (Tor does not protect IPv6 by default)

These are not edge cases.  
They are common failure points.

---

## What This Tool Does *Not* Do

| It does not deanonymize you
| It does not exploit Tor
| It does not claim Tor is useless
| It does not provide anonymity

Tor Myth Breaker only answers one question:

**Is Tor enforcing isolation, or are you assuming it is?**

---

## Example Output

When Tor is running but the system is still leaking if you see what i mean :)) :


## License

This project is released under the MIT License.

You are free to use, study, modify, and redistribute the tool.
The goal is transparency, education, and better operational security just enjoy.
