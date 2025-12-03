<h1 align="center">🌿🌿🌿 BASIL 🌿🌿🌿</h1>
<h1 align="center">Better Actuation of Spot Ignited at LAU</h1>

### Model-Based Quadruped Control Meta-Workspace

`🌿BASIL🌿` is a meta-repository that ties together:

- A fork of the MIT **Underactuated Robotics** `underactuated` repo, and  
- A forked **Spot** playground with our own controllers and trajectory optimization code,

into a single workspace for studying **model-based control and trajectory optimization** for Boston Dynamics’ Spot using Drake.

In this project we:

- Stabilize Spot in place using **joint-level PD** and **LQR** around a nominal standing pose.  
- Generate an **underactuated multi-step trot** using centroidal trajectory optimization with passive knees.  
- Build and validate a **joint-space linear model** as a candidate prediction model for a future MPC controller.  

All of our custom code lives in the **`external/spot`** submodule, but it depends directly on modified files in the **`external/underactuated`** fork. You must therefore initialize **both** submodules (recursively) before running anything.

---

## Repository Structure

At a high level:

```text
basil/
├── external/
│   ├── spot/            # Fork with all 🌿BASIL🌿 Spot controllers, sims, Docker, etc.
│   └── underactuated/   # Fork of MIT Underactuated repo, with local modifications
├── requirements.txt     # Python dependencies for non-Docker usage
└── ...                  # (optional) extra configs, scripts, notes
```

Think of `🌿basil🌿` as the umbrella workspace:

- The top level manages submodules, Python environment, and documentation.
- `external/spot` is where you actually run sims (via Docker or local Python).
- `external/underactuated` provides the Drake plus utilities infrastructure that `spot` builds on.

---

## Quick Start

### 1. Clone 🌿BASIL🌿 with All Submodules

This repo uses nested submodules (Spot and Underactuated, plus whatever they contain), so you must clone recursively:

```bash
git clone --recurse-submodules git@github.com:wgtayar/basil.git basil
cd basil
```

If you prefer a different folder name, replace the final `🌿basil🌿` argument with whatever you like.

---

### 2. If You Already Cloned Without Submodules

If you previously ran a plain `git clone` and now `external/spot` or `external/underactuated` look empty or incomplete:

```bash
cd basil    # or whatever your clone directory is called
git submodule update --init --recursive
```

This will:

- Initialize all top-level submodules (`external/spot`, `external/underactuated`), and  
- Recursively initialize all of their nested submodules as well.

---

### 3. Set Up a Python Environment (Non-Docker Users) (Also we highly recommend using Docker :) )

If you still want to run things outside Docker, we recommend:

```bash
cd basil

# Optional but recommended: create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies (Drake plus scientific stack)
pip install --upgrade pip
pip install -r requirements.txt
```

The `requirements.txt` here is a minimal environment inspired by the official underactuated requirements, including `drake`, `numpy`, `scipy`, `matplotlib`, and a few supporting libraries.

---

### 4. Running the Actual Spot Experiments

All the interesting 🌿BASIL🌿 experiments live in the Spot submodule:

```bash
cd basil/external/spot
```

From here:

- If you want a Docker-based workflow (recommended!!), follow the instructions in `external/spot/README.md` (it explains how to build the `spot-sim` image and run Meshcat-based sims).
- If you want to run locally (no Docker, not recommened!!), make sure you have installed `basil/requirements.txt`, then follow any non-Docker instructions in the `spot` README.

Examples that live in `external/spot` include:

- PD standing and disturbance rejection  
- Joint-space LQR standing  
- Full-state LQR experiments
- MPC Control of Spot
- Underactuated multi-step trot playback

---

### 5. Updating 🌿BASIL🌿 (and All Submodules)

To pull new changes and keep both submodules in sync:

```bash
cd basil
git pull
git submodule update --init --recursive
```

If you want Git to always recurse into submodules when pulling:

```bash
git config --global submodule.recurse true
```

After that, a normal:

```bash
git pull
```

will also update `external/spot`, `external/underactuated`, and their nested submodules.

---

### 6. Checking Submodule Status

To verify that everything is initialized and on the expected commits:

```bash
cd basil
git submodule status
```

- A leading space means clean and at the recorded commit.  
- `+` means the submodule has diverged (ahead or behind).  
- `-` means it is not yet initialized.

---

## Notes and Best Practices

- Always use `--recurse-submodules` when cloning or `git submodule update --init --recursive` after pulling.  
- Treat `🌿basil🌿` as the control tower and `external/spot` as the flight deck where you actually run experiments.  
- If something behaves strangely after a `git pull`, it is often fixed by:

  ```bash
  git submodule update --init --recursive
  ```

- For reproducible non-Docker runs, use a fresh virtual environment and `pip install -r requirements.txt`.

---

*Enjoy exploring model-based quadruped control with BASIL 🌿*
