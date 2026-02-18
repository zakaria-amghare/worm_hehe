# 🧬 Malware Evolution Lab: File Replication & Mutation

[![Safety](https://img.shields.io/badge/Environment-Sandbox_Only-red.svg)](#-ethical--safety-notice)
[![Purpose](https://img.shields.io/badge/Purpose-Cybersecurity_Education-blue.svg)](#-objectives)
[![Topic](https://img.shields.io/badge/Focus-Malware_Analysis-orange.svg)](#-learning-focus)

This repository functions as a **step-by-step cybersecurity learning lab**. It documents the evolution of a self-replicating script (worm), demonstrating how minor code mutations can drastically change a program's impact on a system's file resources.

---

## ⚠️ ETHICAL & SAFETY NOTICE
**This repository contains code designed for malware analysis and educational research only.**

* **DO NOT** execute any code from this repository on production systems or personal machines.
* **ONLY** run these scripts inside a dedicated **Virtual Machine (VM)** or a **Sandboxed Environment**.
* **DISCLAIMER**: The author is not responsible for any misuse or accidental damage caused by these scripts.

---

## 🎯 Objectives
The goal of this lab is to provide a controlled environment for:
* **Analyzing Disk Resource Exhaustion**: Understanding how rapid file creation impacts OS stability.
* **Observing Code Mutation**: Analyzing how small logic changes (e.g., recursive vs. iterative) alter the speed and footprint of replication.
* **Strengthening Defensive Skills**: Developing detection patterns for unusual file-system activity.

---

## 🧠 Learning Focus


[Image of the malware life cycle]

* **File System Interaction**: How malicious scripts navigate directories and permissions.
* **Replication Mechanisms**: The difference between linear, exponential, and polymorphic replication.
* **Resource Exhaustion**: Observing the "Denial of Service" (DoS) effect on local storage.
* **Behavioral Analysis**: Monitoring system calls and CPU spikes during execution.

---

## 🔁 The Evolutionary Timeline
This repository is organized by **commits**. Each commit represents a new "generation" of the worm's logic:

| Generation | Focus | Key Change |
| :--- | :--- | :--- |
| **v1.0** | Basic Copy | Simple file duplication in a single directory. |
| **v1.1** | Recursive Spread | Logic added to traverse subdirectories. |
| **v2.0** | Payload Mutation | Files are generated with randomized names/extensions to bypass simple string detection. |
| **v3.0** | Resource Locking | Logic to prevent the user from easily deleting the replicas. |

---

## 🛠️ How to Use This Lab
1. **Prepare your Sandbox**: Set up a VM (e.g., Any.run, Flare-VM, or a basic Linux Distro).
2. **Checkout a Stage**: Navigate to a specific evolutionary step:
   ```bash
   git checkout [commit-hash]
